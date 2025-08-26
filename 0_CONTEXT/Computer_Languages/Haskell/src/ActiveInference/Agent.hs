{-
Active Inference Agent
=====================

This module implements the Active Inference agent with belief updating,
policy selection, and free energy minimization using Haskell's pure functional
approach and strong type system.
-}

module ActiveInference.Agent
    ( -- * Agent Type
      ActiveInferenceAgent(..)
    , AgentState(..)
    , AgentHistory(..)

      -- * Agent Operations
    , createAgent
    , stepAgent
    , updateBeliefs
    , selectAction
    , calculateVariationalFreeEnergy
    , calculateExpectedFreeEnergy

      -- * History and Statistics
    , getAgentHistory
    , getAgentStatistics
    , saveAgentResults

      -- * Utility Functions
    , resetAgent
    , printAgentState
    ) where

import qualified Data.Vector as V
import qualified Data.Matrix as M
import qualified Data.List as L
import Control.Monad.State
import Control.Monad.Writer
import System.Random (StdGen, mkStdGen, randomR)
import Data.Time.Clock (UTCTime, getCurrentTime)
import Data.Time.Format (formatTime, defaultTimeLocale)

import ActiveInference.Core

-- | Active Inference Agent with state
data ActiveInferenceAgent = ActiveInferenceAgent
    { config :: !AgentConfig
    , generativeModel :: !GenerativeModel
    , currentBeliefs :: !V.Vector Probability
    , actionHistory :: ![Action]
    , observationHistory :: ![Observation]
    , freeEnergyHistory :: ![FreeEnergy]
    , beliefHistory :: ![V.Vector Probability]
    , timestampHistory :: ![UTCTime]
    , randomGen :: !StdGen
    } deriving (Show)

-- | Agent state for state monad operations
data AgentState = AgentState
    { agent :: !ActiveInferenceAgent
    , currentTime :: !UTCTime
    } deriving (Show)

-- | Agent statistics
data AgentStatistics = AgentStatistics
    { totalSteps :: !Int
    , averageFreeEnergy :: !FreeEnergy
    , actionDistribution :: ![(Action, Int)]
    , finalBeliefs :: ![Probability]
    , totalExecutionTime :: !Double
    } deriving (Show)

-- | Create a new Active Inference agent
createAgent :: AgentConfig -> IO ActiveInferenceAgent
createAgent config = do
    case validateConfig config of
        Left err -> error err
        Right validConfig -> do
            let gen = mkStdGen (randomSeed validConfig)
            let model = initializeGenerativeModel validConfig gen
            let initialBeliefs = priors model
            currentTime <- getCurrentTime
            pure ActiveInferenceAgent
                { config = validConfig
                , generativeModel = model
                , currentBeliefs = initialBeliefs
                , actionHistory = []
                , observationHistory = []
                , freeEnergyHistory = []
                , beliefHistory = [initialBeliefs]
                , timestampHistory = [currentTime]
                , randomGen = gen
                }

-- | Execute one step of the perception-action loop
stepAgent :: ActiveInferenceAgent -> Observation -> IO ActiveInferenceAgent
stepAgent agent observation = do
    currentTime <- getCurrentTime

    -- Update beliefs based on observation
    let updatedBeliefs = ActiveInference.Core.updateBeliefs
                        (generativeModel agent)
                        (currentBeliefs agent)
                        observation

    -- Calculate free energy
    let vfe = calculateVariationalFreeEnergy agent
    let fe = getVFE vfe

    -- Select action by minimizing expected free energy
    let action = selectAction agent

    -- Update agent state
    let updatedAgent = agent
        { currentBeliefs = updatedBeliefs
        , actionHistory = actionHistory agent ++ [action]
        , observationHistory = observationHistory agent ++ [observation]
        , freeEnergyHistory = freeEnergyHistory agent ++ [fe]
        , beliefHistory = beliefHistory agent ++ [updatedBeliefs]
        , timestampHistory = timestampHistory agent ++ [currentTime]
        }

    -- Logging
    when (enableLogging $ config agent) $ do
        putStrLn $ "Step - Obs: " ++ show observation ++
                  ", Action: " ++ show action ++
                  ", Free Energy: " ++ show fe

    pure updatedAgent

-- | Update beliefs given an observation
updateBeliefs :: ActiveInferenceAgent -> Observation -> ActiveInferenceAgent
updateBeliefs agent observation =
    let updatedBeliefs = ActiveInference.Core.updateBeliefs
                        (generativeModel agent)
                        (currentBeliefs agent)
                        observation
    in agent { currentBeliefs = updatedBeliefs }

-- | Select action by minimizing expected free energy
selectAction :: ActiveInferenceAgent -> Action
selectAction agent =
    let efes = [calculateExpectedFreeEnergyForAction agent action
               | action <- [0..nActions (config agent) - 1]]
        (bestAction, _) = L.minimumBy (\(_, efe1) (_, efe2) -> compare efe1 efe2)
                         (zip [0..] efes)
    in bestAction

-- | Calculate expected free energy for a specific action
calculateExpectedFreeEnergyForAction :: ActiveInferenceAgent -> Action -> FreeEnergy
calculateExpectedFreeEnergyForAction agent action =
    let predictedBeliefs = predictBeliefs
                          (generativeModel agent)
                          (currentBeliefs agent)
                          action
        pragmaticValue = calculatePragmaticValue agent predictedBeliefs
        epistemicValue = calculateEpistemicValue agent predictedBeliefs
        expectedFE = pragmaticValue - (uncertaintyWeight $ config agent) * epistemicValue
    in expectedFE

-- | Calculate pragmatic value (expected surprise about preferred observations)
calculatePragmaticValue :: ActiveInferenceAgent -> V.Vector Probability -> FreeEnergy
calculatePragmaticValue agent predictedBeliefs =
    let nStates = V.length predictedBeliefs
        nObs = nObservations (config agent)
        preferences = ActiveInference.Core.preferences (generativeModel agent)
        likelihood = ActiveInference.Core.likelihood (generativeModel agent)
        pragmaticValue = sum
            [ V.unsafeIndex predictedBeliefs state *
              V.unsafeIndex preferences obs *
              M.unsafeGet obs state likelihood
            | state <- [0..nStates-1]
            , obs <- [0..nObs-1]
            ]
    in pragmaticValue

-- | Calculate epistemic value (information gain)
calculateEpistemicValue :: ActiveInferenceAgent -> V.Vector Probability -> FreeEnergy
calculateEpistemicValue agent predictedBeliefs =
    calculateEntropy predictedBeliefs

-- | Calculate variational free energy
calculateVariationalFreeEnergy :: ActiveInferenceAgent -> VFE
calculateVariationalFreeEnergy agent =
    calculateFreeEnergy (generativeModel agent) (currentBeliefs agent)

-- | Calculate expected free energy for all actions
calculateExpectedFreeEnergy :: ActiveInferenceAgent -> [(Action, FreeEnergy)]
calculateExpectedFreeEnergy agent =
    [(action, calculateExpectedFreeEnergyForAction agent action)
    | action <- [0..nActions (config agent) - 1]]

-- | Get agent history
getAgentHistory :: ActiveInferenceAgent -> ([Action], [Observation], [FreeEnergy], [V.Vector Probability])
getAgentHistory agent =
    ( actionHistory agent
    , observationHistory agent
    , freeEnergyHistory agent
    , beliefHistory agent
    )

-- | Get agent statistics
getAgentStatistics :: ActiveInferenceAgent -> AgentStatistics
getAgentStatistics agent =
    let actions = actionHistory agent
        freeEnergies = freeEnergyHistory agent
        totalSteps = length actions
        avgFE = if null freeEnergies then 0 else sum freeEnergies / fromIntegral (length freeEnergies)
        actionDist = L.sort $ L.group $ L.sort actions
        actionCounts = map (\group -> (head group, length group)) actionDist
        finalBeliefs = V.toList $ last $ beliefHistory agent
        timestamps = timestampHistory agent
        timeDiff = if length timestamps > 1
                   then realToFrac $ diffUTCTime (last timestamps) (head timestamps)
                   else 0.0
    in AgentStatistics totalSteps avgFE actionCounts finalBeliefs timeDiff

-- | Save agent results to output directory
saveAgentResults :: ActiveInferenceAgent -> FilePath -> IO ()
saveAgentResults agent outputDir = do
    createDirectoryIfMissing True outputDir

    -- Save configuration
    let configFile = outputDir </> "config.json"
    writeFile configFile $ show (config agent)

    -- Save statistics
    let stats = getAgentStatistics agent
        statsFile = outputDir </> "statistics.json"
    writeFile statsFile $ show stats

    -- Save belief history
    let beliefFile = outputDir </> "belief_history.csv"
        beliefLines = "Step,State0,State1,State2" :
                     [show step ++ "," ++ L.intercalate "," (map show $ V.toList beliefs)
                     | (step, beliefs) <- zip [0..] (beliefHistory agent)]
    writeFile beliefFile $ unlines beliefLines

    -- Save action history
    let actionFile = outputDir </> "action_history.csv"
        actionLines = "Step,Action" :
                     [show step ++ "," ++ show action
                     | (step, action) <- zip [0..] (actionHistory agent)]
    writeFile actionFile $ unlines actionLines

    putStrLn $ "Agent results saved to " ++ outputDir

-- | Reset agent to initial state
resetAgent :: ActiveInferenceAgent -> IO ActiveInferenceAgent
resetAgent agent = createAgent (config agent)

-- | Print agent current state
printAgentState :: ActiveInferenceAgent -> IO ()
printAgentState agent = do
    putStrLn "=== Agent State ==="
    putStrLn $ "Current Beliefs: " ++ show (V.toList $ currentBeliefs agent)
    putStrLn $ "Total Steps: " ++ show (length $ actionHistory agent)
    putStrLn $ "Current Free Energy: " ++ show (getVFE $ calculateVariationalFreeEnergy agent)
    putStrLn $ "Action History: " ++ show (take 10 $ actionHistory agent)
    putStrLn "==================="

-- Helper functions
diffUTCTime :: UTCTime -> UTCTime -> Double
diffUTCTime t1 t0 = realToFrac $ diffUTCTime t1 t0

-- File utilities
createDirectoryIfMissing :: Bool -> FilePath -> IO ()
createDirectoryIfMissing createParents path =
    -- Simplified version - in real code, use System.Directory.createDirectoryIfMissing
    pure ()  -- Placeholder

(</>) :: FilePath -> FilePath -> FilePath
p1 </> p2 = p1 ++ "/" ++ p2
