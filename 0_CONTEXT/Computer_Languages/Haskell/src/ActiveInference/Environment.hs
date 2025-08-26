{-
Active Inference Environment
============================

This module implements multi-agent environments for Active Inference,
including ant colony simulations with pheromone communication.
-}

module ActiveInference.Environment
    ( -- * Environment Types
      Environment(..)
    , Position(..)
    , PheromoneLevels(..)
    , AntAgent(..)
    , EnvironmentConfig(..)
    , SimulationResults(..)
    , SimulationStep(..)

      -- * Environment Operations
    , createEnvironment
    , stepEnvironment
    , runSimulation
    , generateObservation
    , executeAction
    , layPheromone

      -- * Utility Functions
    , getTotalPheromones
    , getAverageFreeEnergy
    , checkConvergence
    , saveEnvironmentResults
    ) where

import qualified Data.Vector as V
import qualified Data.Matrix as M
import qualified Data.List as L
import Control.Monad (forM, forM_, when)
import System.Random (StdGen, mkStdGen, randomR)
import Data.Time.Clock (UTCTime, getCurrentTime)
import Data.Time.Format (formatTime, defaultTimeLocale)

import ActiveInference.Core
import ActiveInference.Agent

-- | Position in 2D space
data Position = Position { x :: !Int, y :: !Int }
    deriving (Show, Eq, Ord)

-- | Pheromone levels at a grid cell
data PheromoneLevels = PheromoneLevels
    { home :: !Double
    , food :: !Double
    } deriving (Show, Eq, Ord)

-- | Ant agent in the environment
data AntAgent = AntAgent
    { antId :: !Int
    , position :: !Position
    , agent :: !ActiveInferenceAgent
    , carryingFood :: !Bool
    , energy :: !Double
    } deriving (Show)

-- | Environment configuration
data EnvironmentConfig = EnvironmentConfig
    { gridSize :: !Int
    , nAnts :: !Int
    , foodSources :: !Int
    , pheromoneDecay :: !Double
    , maxSteps :: !Int
    , outputDirectory :: !FilePath
    } deriving (Show, Eq)

-- | Simulation step data
data SimulationStep = SimulationStep
    { stepNumber :: !Int
    , totalPheromones :: !Double
    , foodCollected :: !Int
    , antPositions :: ![Position]
    , averageFreeEnergy :: !Double
    , timestamp :: !UTCTime
    } deriving (Show)

-- | Complete simulation results
data SimulationResults = SimulationResults
    { configuration :: !EnvironmentConfig
    , steps :: ![SimulationStep]
    , finalAnts :: ![AntAgent]
    , totalExecutionTime :: !Double
    , convergenceAchieved :: !Bool
    } deriving (Show)

-- | Environment state
data Environment = Environment
    { config :: !EnvironmentConfig
    , pheromoneGrid :: !(V.Vector (V.Vector PheromoneLevels))
    , foodGrid :: !(V.Vector (V.Vector Double))
    , ants :: ![AntAgent]
    , foodLocations :: ![Position]
    , currentStep :: !Int
    , randomGen :: !StdGen
    } deriving (Show)

-- | Create a new environment
createEnvironment :: EnvironmentConfig -> IO Environment
createEnvironment config = do
    gen <- mkStdGen 42  -- Fixed seed for reproducibility

    -- Initialize grids
    let pheromoneGrid = V.replicate (gridSize config) $
                       V.replicate (gridSize config) $
                       PheromoneLevels 0.0 0.0

    let foodGrid = V.replicate (gridSize config) $
                  V.replicate (gridSize config) 0.0

    -- Create food sources
    let (foodLocations, gen') = createFoodSources (gridSize config) (foodSources config) gen

    -- Place food in grid
    let foodGrid' = placeFood foodGrid foodLocations

    -- Create ants
    ants <- createAnts (nAnts config) (gridSize config) gen'

    pure Environment
        { config = config
        , pheromoneGrid = pheromoneGrid
        , foodGrid = foodGrid'
        , ants = ants
        , foodLocations = foodLocations
        , currentStep = 0
        , randomGen = gen'
        }

-- | Create food sources randomly
createFoodSources :: Int -> Int -> StdGen -> ([Position], StdGen)
createFoodSources gridSize nFood gen =
    let positions = [Position x y | x <- [0..gridSize-1], y <- [0..gridSize-1]]
        (selected, gen') = selectRandom nFood positions gen
    in (selected, gen')

-- | Select n random elements from list
selectRandom :: Int -> [a] -> StdGen -> ([a], StdGen)
selectRandom n xs gen = go n xs gen []
  where
    go 0 _ gen acc = (reverse acc, gen)
    go _ [] gen acc = (reverse acc, gen)
    go n (x:xs) gen acc =
        let (r, gen') = randomR (0.0, 1.0) gen
        in if r < fromIntegral n / fromIntegral (length xs + n)
           then go (n-1) xs gen' (x:acc)
           else go n xs gen' acc

-- | Place food at specified locations
placeFood :: V.Vector (V.Vector Double) -> [Position] -> V.Vector (V.Vector Double)
placeFood grid locations = L.foldl' placeFoodAt grid locations
  where
    placeFoodAt grid pos =
        let row = grid V.! y pos
            updatedRow = row V.// [(x pos, 10.0)]  -- 10 units of food
        in grid V.// [(y pos, updatedRow)]

-- | Create ants with active inference agents
createAnts :: Int -> Int -> StdGen -> IO [AntAgent]
createAnts nAnts gridSize gen = do
    let positions = [Position (x `mod` gridSize) (x `div` gridSize) | x <- [0..nAnts-1]]

    forM (zip [0..nAnts-1] positions) $ \(antId, pos) -> do
        let agentConfig = AgentConfig
                { nStates = 4
                , nObservations = 3
                , nActions = 4
                , learningRate = 0.1
                , uncertaintyWeight = 0.2
                , precision = 1.0
                , enableLogging = False
                , outputDirectory = "output/ants"
                , randomSeed = antId + 42
                }

        agent <- createAgent agentConfig

        pure AntAgent
            { antId = antId
            , position = pos
            , agent = agent
            , carryingFood = False
            , energy = 100.0
            }

-- | Execute one environment step
stepEnvironment :: Environment -> IO Environment
stepEnvironment env = do
    currentTime <- getCurrentTime

    -- Update pheromone decay
    let decayedPheromones = decayPheromones (pheromoneDecay $ config env) (pheromoneGrid env)

    -- Update ants
    updatedAnts <- forM (ants env) $ \ant -> do
        -- Generate observation
        let observation = generateObservation env ant

        -- Step agent
        updatedAgent <- stepAgent (agent ant) observation

        -- Execute action
        let newPosition = executeAction (position ant) (last $ actionHistory updatedAgent) (gridSize $ config env)

        -- Lay pheromone
        let newPheromoneGrid = layPheromone decayedPheromones ant newPosition

        -- Check for food
        let (carryingFood', energy', newFoodGrid) = checkFood (foodGrid env) newPosition ant

        pure (ant { position = newPosition, agent = updatedAgent, carryingFood = carryingFood', energy = energy' }, newFoodGrid, newPheromoneGrid)

    -- Combine updates
    let (ants', foodGrids, pheromoneGrids) = unzip3 updatedAnts
    let finalFoodGrid = L.foldl1' (V.zipWith (V.zipWith (+))) foodGrids  -- Merge food updates
    let finalPheromoneGrid = L.foldl1' (V.zipWith (V.zipWith combinePheromones)) pheromoneGrids

    pure env
        { pheromoneGrid = finalPheromoneGrid
        , foodGrid = finalFoodGrid
        , ants = ants'
        , currentStep = currentStep env + 1
        }

-- | Generate observation for an ant
generateObservation :: Environment -> AntAgent -> Observation
generateObservation env ant =
    let pos = position ant
        gridSize = gridSize $ config env

        -- Check neighboring cells for food and pheromones
        neighbors = [(x + dx, y + dy) | dx <- [-1..1], dy <- [-1..1]]
        validNeighbors = [(x, y) | (x, y) <- neighbors,
                                 x >= 0, x < gridSize, y >= 0, y < gridSize]

        foodNearby = any (> 0.0) [foodGrid env V.! y V.! x | (x, y) <- validNeighbors]
        homePheromone = maximum [home $ pheromoneGrid env V.! y V.! x | (x, y) <- validNeighbors]
        foodPheromone = maximum [food $ pheromoneGrid env V.! y V.! x | (x, y) <- validNeighbors]

    in case (foodNearby, homePheromone > 0.5, foodPheromone > 0.5) of
        (True, _, _) -> 0  -- Food present
        (_, True, _) -> 1  -- Strong home pheromone
        (_, _, True) -> 2  -- Strong food pheromone
        _ -> 0             -- Default observation

-- | Execute action and return new position
executeAction :: Position -> Action -> Int -> Position
executeAction (Position x y) action gridSize =
    case action of
        0 -> Position x (max 0 (y-1))                    -- North
        1 -> Position (min (gridSize-1) (x+1)) y         -- East
        2 -> Position x (min (gridSize-1) (y+1))         -- South
        3 -> Position (max 0 (x-1)) y                    -- West
        _ -> Position x y                                 -- Stay

-- | Lay pheromone at position
layPheromone :: V.Vector (V.Vector PheromoneLevels) -> AntAgent -> Position -> V.Vector (V.Vector PheromoneLevels)
layPheromone grid ant (Position x y) =
    let currentLevels = grid V.! y V.! x
        newLevels = if carryingFood ant
                    then currentLevels { food = min 1.0 (food currentLevels + 0.1) }
                    else currentLevels { home = min 1.0 (home currentLevels + 0.1) }
        updatedRow = grid V.! y V.// [(x, newLevels)]
    in grid V.// [(y, updatedRow)]

-- | Decay pheromones
decayPheromones :: Double -> V.Vector (V.Vector PheromoneLevels) -> V.Vector (V.Vector PheromoneLevels)
decayPheromones decayRate grid =
    V.map (V.map decay) grid
  where
    decay levels = levels { home = home levels * decayRate, food = food levels * decayRate }

-- | Check for food at position and update ant state
checkFood :: V.Vector (V.Vector Double) -> Position -> AntAgent -> (Bool, Double, V.Vector (V.Vector Double))
checkFood foodGrid (Position x y) ant =
    let currentFood = foodGrid V.! y V.! x
    in if currentFood > 0.0
       then (True, min 100.0 (energy ant + 20.0), updateFoodGrid foodGrid (Position x y) (currentFood - 1.0))
       else (carryingFood ant, max 0.0 (energy ant - 1.0), foodGrid)

-- | Update food grid
updateFoodGrid :: V.Vector (V.Vector Double) -> Position -> Double -> V.Vector (V.Vector Double)
updateFoodGrid grid (Position x y) newAmount =
    let row = grid V.! y
        updatedRow = row V.// [(x, newAmount)]
    in grid V.// [(y, updatedRow)]

-- | Combine pheromone levels (for merging updates)
combinePheromones :: PheromoneLevels -> PheromoneLevels -> PheromoneLevels
combinePheromones p1 p2 = PheromoneLevels
    { home = home p1 + home p2
    , food = food p1 + food p2
    }

-- | Run complete simulation
runSimulation :: Environment -> IO SimulationResults
runSimulation env = do
    startTime <- getCurrentTime

    let runSteps 0 env _ = pure ([], env)
        runSteps n env steps = do
            stepData <- createSimulationStep env
            updatedEnv <- stepEnvironment env
            (remainingSteps, finalEnv) <- runSteps (n-1) updatedEnv (steps ++ [stepData])
            pure (steps ++ [stepData] ++ remainingSteps, finalEnv)

    (steps, finalEnv) <- runSteps (maxSteps $ config env) env []

    endTime <- getCurrentTime
    let executionTime = realToFrac $ diffUTCTime endTime startTime
    let convergence = checkConvergence steps

    pure SimulationResults
        { configuration = config env
        , steps = steps
        , finalAnts = ants finalEnv
        , totalExecutionTime = executionTime
        , convergenceAchieved = convergence
        }

-- | Create simulation step data
createSimulationStep :: Environment -> IO SimulationStep
createSimulationStep env = do
    currentTime <- getCurrentTime
    let totalPheromones = getTotalPheromones env
    let foodCollected = length $ filter carryingFood (ants env)
    let antPositions = map position (ants env)
    let avgFreeEnergy = getAverageFreeEnergy env

    pure SimulationStep
        { stepNumber = currentStep env
        , totalPheromones = totalPheromones
        , foodCollected = foodCollected
        , antPositions = antPositions
        , averageFreeEnergy = avgFreeEnergy
        , timestamp = currentTime
        }

-- | Get total pheromone levels
getTotalPheromones :: Environment -> Double
getTotalPheromones env =
    V.sum $ V.map (V.sum . V.map (\p -> home p + food p)) (pheromoneGrid env)

-- | Get average free energy across all agents
getAverageFreeEnergy :: Environment -> Double
getAverageFreeEnergy env =
    let freeEnergies = map (getVFE . calculateVariationalFreeEnergy . agent) (ants env)
    in if null freeEnergies then 0.0 else sum freeEnergies / fromIntegral (length freeEnergies)

-- | Check if simulation has converged
checkConvergence :: [SimulationStep] -> Bool
checkConvergence steps =
    if length steps < 10 then False
    else let recent = take 10 $ reverse steps
             avgPheromones = average $ map totalPheromones recent
             variance = average $ map (\s -> (totalPheromones s - avgPheromones)^2) recent
         in variance < 1.0  -- Low variance indicates convergence
  where
    average xs = sum xs / fromIntegral (length xs)

-- | Save environment results
saveEnvironmentResults :: SimulationResults -> FilePath -> IO ()
saveEnvironmentResults results outputDir = do
    createDirectoryIfMissing True outputDir

    -- Save simulation results
    writeFile (outputDir </> "simulation_results.json") (show results)

    -- Save pheromone grid (final step)
    let finalStep = last $ steps results
    writeFile (outputDir </> "final_pheromones.csv") $
        "Y,X,HomePheromone,FoodPheromone\n" ++
        concatMap (\(y, row) -> concatMap (\(x, p) ->
            show y ++ "," ++ show x ++ "," ++
            show (home p) ++ "," ++ show (food p) ++ "\n") (zip [0..] $ V.toList row))
        (zip [0..] $ V.toList $ V.replicate (gridSize $ configuration results) (V.empty :: V.Vector PheromoneLevels))

    -- Save food grid
    writeFile (outputDir </> "final_food.csv") $
        "Y,X,FoodAmount\n" ++
        concatMap (\(y, row) -> concatMap (\(x, food) ->
            show y ++ "," ++ show x ++ "," ++ show food ++ "\n") (zip [0..] $ V.toList row))
        (zip [0..] $ V.toList $ V.replicate (gridSize $ configuration results) (V.empty :: V.Vector Double))

    putStrLn $ "Environment results saved to " ++ outputDir

-- Utility functions
diffUTCTime :: UTCTime -> UTCTime -> Double
diffUTCTime t1 t0 = realToFrac $ diffUTCTime t1 t0

createDirectoryIfMissing :: Bool -> FilePath -> IO ()
createDirectoryIfMissing _ _ = pure ()  -- Placeholder

(</>) :: FilePath -> FilePath -> FilePath
p1 </> p2 = p1 ++ "/" ++ p2

-- | Unzip3 for triples
unzip3 :: [(a, b, c)] -> ([a], [b], [c])
unzip3 xs = (map (\(a,_,_) -> a) xs, map (\(_,b,_) -> b) xs, map (\(_,_,c) -> c) xs)
