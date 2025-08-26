{-
Active Inference Core Types and Functions
=========================================

This module defines the core types and fundamental functions for Active Inference
in Haskell, leveraging the language's strong type system and mathematical elegance.
-}

module ActiveInference.Core
    ( -- * Core Types
      State
    , Observation
    , Action
    , TimeStep
    , Probability
    , FreeEnergy
    , EFE(..)
    , VFE(..)

      -- * Generative Model
    , GenerativeModel(..)
    , AgentConfig(..)
    , BeliefState(..)

      -- * Matrix Types
    , Matrix
    , Vector
    , LikelihoodMatrix
    , TransitionMatrices
    , PreferenceVector
    , PriorVector

      -- * Core Functions
    , validateConfig
    , initializeGenerativeModel
    , normalizeVector
    , normalizeMatrix
    , calculateEntropy
    , calculateFreeEnergy
    , predictBeliefs
    , updateBeliefs

      -- * Utility Functions
    , matrixToList
    , vectorToList
    , listToVector
    , listToMatrix
    ) where

import qualified Data.Vector as V
import qualified Data.Matrix as M
import qualified Data.List as L
import qualified Statistics.Sample as Stats
import Control.Monad (when, unless)
import System.Random (StdGen, mkStdGen)

-- | Type synonyms for clarity and type safety
type State = Int
type Observation = Int
type Action = Int
type TimeStep = Int
type Probability = Double
type FreeEnergy = Double

-- | Expected Free Energy components
data EFE = EFE
    { expectedFE :: !FreeEnergy
    , pragmaticValue :: !FreeEnergy
    , epistemicValue :: !FreeEnergy
    } deriving (Show, Eq, Ord)

-- | Variational Free Energy
newtype VFE = VFE { getVFE :: FreeEnergy }
    deriving (Show, Eq, Ord, Num, Fractional, Floating)

-- | Generative model matrices
data GenerativeModel = GenerativeModel
    { likelihood :: !LikelihoodMatrix    -- ^ A matrix: p(o|s)
    , transitions :: !TransitionMatrices -- ^ B matrices: p(s'|s,a)
    , preferences :: !PreferenceVector   -- ^ C vector: p(o)
    , priors :: !PriorVector            -- ^ D vector: p(s)
    } deriving (Show, Eq)

-- | Agent configuration with validation
data AgentConfig = AgentConfig
    { nStates :: !Int
    , nObservations :: !Int
    , nActions :: !Int
    , learningRate :: !Probability
    , uncertaintyWeight :: !Probability
    , precision :: !Probability
    , enableLogging :: !Bool
    , outputDirectory :: !FilePath
    , randomSeed :: !Int
    } deriving (Show, Eq)

-- | Current belief state
data BeliefState = BeliefState
    { currentBeliefs :: !Vector
    , previousBeliefs :: !(Maybe Vector)
    , beliefHistory :: ![Vector]
    } deriving (Show, Eq)

-- | Matrix and vector types using efficient Data.Vector and Data.Matrix
type Matrix = M.Matrix Probability
type Vector = V.Vector Probability
type LikelihoodMatrix = Matrix
type TransitionMatrices = V.Vector Matrix  -- One matrix per action
type PreferenceVector = Vector
type PriorVector = Vector

-- | Configuration validation
validateConfig :: AgentConfig -> Either String AgentConfig
validateConfig config = do
    unless (nStates config > 0) $
        Left "Number of states must be positive"
    unless (nObservations config > 0) $
        Left "Number of observations must be positive"
    unless (nActions config > 0) $
        Left "Number of actions must be positive"
    unless (learningRate config > 0 && learningRate config <= 1) $
        Left "Learning rate must be in (0, 1]"
    unless (uncertaintyWeight config >= 0) $
        Left "Uncertainty weight must be non-negative"
    unless (precision config > 0) $
        Left "Precision must be positive"
    pure config

-- | Initialize generative model from configuration
initializeGenerativeModel :: AgentConfig -> StdGen -> GenerativeModel
initializeGenerativeModel config gen =
    let (aMatrix, gen1) = initializeLikelihoodMatrix (nObservations config) (nStates config) gen
        (bMatrices, gen2) = initializeTransitionMatrices (nStates config) (nActions config) gen1
        (cVector, gen3) = initializePreferenceVector (nObservations config) gen2
        dVector = initializePriorVector (nStates config)
    in GenerativeModel aMatrix bMatrices cVector dVector

-- | Initialize likelihood matrix A (p(o|s))
initializeLikelihoodMatrix :: Int -> Int -> StdGen -> (LikelihoodMatrix, StdGen)
initializeLikelihoodMatrix nObs nStates gen =
    let rows = replicate nObs (replicate nStates 0.1)  -- Base probabilities
        -- Add diagonal structure with noise
        matrix = M.fromLists $ zipWith addDiagonal rows [0..nObs-1]
        normalized = normalizeMatrix matrix
    in (normalized, gen)  -- Simplified, no actual random for now
  where
    addDiagonal :: [Probability] -> Int -> [Probability]
    addDiagonal row idx = [if i == idx then 0.7 else 0.1 | i <- [0..nStates-1]]

-- | Initialize transition matrices B (p(s'|s,a))
initializeTransitionMatrices :: Int -> Int -> StdGen -> (TransitionMatrices, StdGen)
initializeTransitionMatrices nStates nActions gen =
    let matrices = V.generate nActions (initializeSingleTransitionMatrix nStates)
    in (matrices, gen)

initializeSingleTransitionMatrix :: Int -> Int -> Matrix
initializeSingleTransitionMatrix nStates actionIdx =
    let baseProb = 1.0 / fromIntegral nStates
        matrix = M.matrix nStates nStates $ \(i,j) ->
            if actionIdx == 0 && i == j then 0.6      -- Stay action
            else if actionIdx == 1 && j == i+1 then 0.6  -- Right action
            else if actionIdx == 2 && i > 1 && j == i-1 then 0.6  -- Left action
            else baseProb
        normalized = normalizeMatrix matrix
    in normalized

-- | Initialize preference vector C (p(o))
initializePreferenceVector :: Int -> StdGen -> (PreferenceVector, StdGen)
initializePreferenceVector nObs gen =
    let preferences = V.generate nObs (\i -> if i < nObs `div` 2 then 1.0 else 0.1)
    in (preferences, gen)

-- | Initialize prior vector D (p(s))
initializePriorVector :: Int -> PriorVector
initializePriorVector nStates =
    let uniformProb = 1.0 / fromIntegral nStates
    in V.replicate nStates uniformProb

-- | Normalize vector to sum to 1
normalizeVector :: Vector -> Vector
normalizeVector vec =
    let total = V.sum vec
    in if total > 0 then V.map (/total) vec else vec

-- | Normalize matrix rows to sum to 1
normalizeMatrix :: Matrix -> Matrix
normalizeMatrix matrix = M.fromRows $ map normalizeVector (M.toRows matrix)

-- | Calculate Shannon entropy of a probability distribution
calculateEntropy :: Vector -> Double
calculateEntropy probs = -(V.sum $ V.map (\p -> if p > 0 then p * logBase 2 p else 0) probs)

-- | Calculate variational free energy
calculateFreeEnergy :: GenerativeModel -> Vector -> VFE
calculateFreeEnergy model beliefs =
    let expectedLikelihood = calculateExpectedLikelihood model beliefs
        entropy = calculateEntropy beliefs
    in VFE (-expectedLikelihood - entropy)

-- | Calculate expected likelihood
calculateExpectedLikelihood :: GenerativeModel -> Vector -> Double
calculateExpectedLikelihood model beliefs =
    let nObs = M.nrows (likelihood model)
        obsProbs = [expectedObsProb model beliefs obs | obs <- [0..nObs-1]]
    in sum $ map (\p -> if p > 0 then p * log p else 0) obsProbs
  where
    expectedObsProb :: GenerativeModel -> Vector -> Int -> Double
    expectedObsProb model beliefs obs =
        let obsRow = M.getRow obs (likelihood model)
            weighted = V.zipWith (*) beliefs (V.fromList obsRow)
        in V.sum weighted

-- | Predict beliefs after taking an action
predictBeliefs :: GenerativeModel -> Vector -> Action -> Vector
predictBeliefs model beliefs action =
    let bMatrix = transitions model V.! action
        predicted = M.getRow 0 (M.multStd (M.rowVector beliefs) bMatrix)
    in V.fromList predicted

-- | Update beliefs given observation using Bayesian inference
updateBeliefs :: GenerativeModel -> Vector -> Observation -> Vector
updateBeliefs model beliefs observation =
    let likelihoodRow = V.fromList $ M.getRow observation (likelihood model)
        posterior = V.zipWith (*) beliefs likelihoodRow
        normalized = normalizeVector posterior
    in normalized

-- | Utility functions for conversion
matrixToList :: Matrix -> [[Probability]]
matrixToList = M.toLists

vectorToList :: Vector -> [Probability]
vectorToList = V.toList

listToVector :: [Probability] -> Vector
listToVector = V.fromList

listToMatrix :: [[Probability]] -> Matrix
listToMatrix = M.fromLists
