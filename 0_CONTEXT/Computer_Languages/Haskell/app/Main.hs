#!/usr/bin/env stack
{- stack script --resolver lts-19.0 --package random --package matrix --package vector --package containers --package time
-}

{-
Active Inference Haskell Demo
============================

This is a standalone Haskell script that demonstrates Active Inference
through single agent and multi-agent simulations, saving results to output files.

To run this script:
    stack Main.hs

Or compile and run:
    stack ghc Main.hs
    ./Main
-}

module Main where

import qualified Data.Vector as V
import qualified Data.Matrix as M
import qualified Data.List as L
import Control.Monad (forM_, when)
import System.Environment (getArgs)
import System.Directory (createDirectoryIfMissing)
import Data.Time.Clock (getCurrentTime)
import Data.Time.Format (formatTime, defaultTimeLocale)

import ActiveInference.Core
import ActiveInference.Agent
import ActiveInference.Environment

-- | Main entry point
main :: IO ()
main = do
    args <- getArgs
    case args of
        ["single-agent"] -> runSingleAgentDemo
        ["ant-colony"] -> runAntColonyDemo
        ["both"] -> do
            runSingleAgentDemo
            putStrLn ""
            runAntColonyDemo
        _ -> do
            putStrLn "Usage: ./Main [single-agent|ant-colony|both]"
            putStrLn "Running both demos by default..."
            putStrLn ""
            runSingleAgentDemo
            putStrLn ""
            runAntColonyDemo

-- | Run single agent demonstration
runSingleAgentDemo :: IO ()
runSingleAgentDemo = do
    putStrLn "🧠 Haskell Single Agent Active Inference Demo"
    putStrLn "=============================================="

    -- Create agent configuration
    let config = AgentConfig
            { nStates = 3
            , nObservations = 3
            , nActions = 3
            , learningRate = 0.1
            , uncertaintyWeight = 0.1
            , precision = 1.0
            , enableLogging = True
            , outputDirectory = "output/single_agent"
            , randomSeed = 42
            }

    -- Create agent
    agent <- createAgent config

    putStrLn $ "Initial beliefs: " ++ show (V.toList $ currentBeliefs agent)
    putStrLn $ "Generative model shapes:"
    putStrLn $ "  A matrix: " ++ show (M.nrows $ likelihood $ generativeModel agent) ++ "x" ++ show (M.ncols $ likelihood $ generativeModel agent)
    putStrLn $ "  B matrices: " ++ show (length $ transitions $ generativeModel agent) ++ " matrices"
    putStrLn $ "  C vector: " ++ show (V.length $ preferences $ generativeModel agent)
    putStrLn $ "  D vector: " ++ show (V.length $ priors $ generativeModel agent)
    putStrLn ""

    -- Run simulation steps
    let observations = [1, 0, 2, 1, 0, 2, 1, 0, 2, 1]  -- Example observation sequence

    finalAgent <- foldM (\agent obs -> do
        putStrLn $ "Step - Observation: " ++ show obs
        stepAgent agent obs
        ) agent observations

    -- Show final statistics
    let stats = getAgentStatistics finalAgent
    putStrLn ""
    putStrLn "Final Statistics:"
    putStrLn $ "  Total Steps: " ++ show (totalSteps stats)
    putStrLn $ "  Average Free Energy: " ++ show (averageFreeEnergy stats)
    putStrLn $ "  Action Distribution: " ++ show (actionDistribution stats)
    putStrLn $ "  Final Beliefs: " ++ show (finalBeliefs stats)
    putStrLn $ "  Total Execution Time: " ++ show (totalExecutionTime stats) ++ " seconds"

    -- Save results
    saveAgentResults finalAgent (outputDirectory config)
    putStrLn $ "\nResults saved to " ++ outputDirectory config

-- | Run ant colony demonstration
runAntColonyDemo :: IO ()
runAntColonyDemo = do
    putStrLn "🐜 Haskell Ant Colony Active Inference Demo"
    putStrLn "==========================================="

    -- Create environment configuration
    let envConfig = EnvironmentConfig
            { gridSize = 8
            , nAnts = 5
            , foodSources = 3
            , pheromoneDecay = 0.95
            , maxSteps = 50
            , outputDirectory = "output/ant_colony"
            }

    putStrLn $ "Creating environment: " ++ show (gridSize envConfig) ++ "x" ++ show (gridSize envConfig) ++ " grid"
    putStrLn $ "Ants: " ++ show (nAnts envConfig)
    putStrLn $ "Food sources: " ++ show (foodSources envConfig)
    putStrLn ""

    -- Create and run simulation
    env <- createEnvironment envConfig
    results <- runSimulation env

    -- Show results
    putStrLn "Simulation Results:"
    putStrLn $ "  Total steps: " ++ show (length $ steps results)
    putStrLn $ "  Total execution time: " ++ show (totalExecutionTime results) ++ " seconds"
    putStrLn $ "  Convergence achieved: " ++ show (convergenceAchieved results)

    -- Show final statistics
    let finalStep = last $ steps results
    putStrLn ""
    putStrLn "Final Step Statistics:"
    putStrLn $ "  Total pheromones: " ++ show (totalPheromones finalStep)
    putStrLn $ "  Food collected: " ++ show (foodCollected finalStep)
    putStrLn $ "  Average free energy: " ++ show (averageFreeEnergy finalStep)

    -- Save results
    saveEnvironmentResults results (outputDirectory envConfig)
    putStrLn $ "\nResults saved to " ++ outputDirectory envConfig

-- | FoldM for monadic folding (not in standard Prelude)
foldM :: (Monad m) => (a -> b -> m a) -> a -> [b] -> m a
foldM _ z [] = return z
foldM f z (x:xs) = do
    z' <- f z x
    foldM f z' xs

-- | Create output directory if it doesn't exist
createOutputDirectories :: IO ()
createOutputDirectories = do
    createDirectoryIfMissing True "output"
    createDirectoryIfMissing True "output/single_agent"
    createDirectoryIfMissing True "output/ant_colony"
    createDirectoryIfMissing True "output/ants"

-- | Write data to file
writeFile :: FilePath -> String -> IO ()
writeFile path content = do
    createDirectoryIfMissing True (takeDirectory path)
    writeFile path content

-- | Take directory part of path
takeDirectory :: FilePath -> FilePath
takeDirectory = reverse . dropWhile (/= '/') . reverse

-- | Simple directory creation (simplified for this demo)
createDirectoryIfMissing :: Bool -> FilePath -> IO ()
createDirectoryIfMissing _ _ = pure ()  -- In real code, use System.Directory

-- | Enhanced environment module with file I/O
saveEnvironmentResults :: SimulationResults -> FilePath -> IO ()
saveEnvironmentResults results outputDir = do
    createDirectoryIfMissing True outputDir

    -- Save simulation results as JSON-like format
    let jsonContent = show results  -- Simplified JSON representation
    writeFile (outputDir ++ "/simulation_results.json") jsonContent

    -- Save step data as CSV
    let csvHeader = "Step,TotalPheromones,FoodCollected,AverageFreeEnergy\n"
        csvRows = map (\step ->
            show (stepNumber step) ++ "," ++
            show (totalPheromones step) ++ "," ++
            show (foodCollected step) ++ "," ++
            show (averageFreeEnergy step) ++ "\n") (steps results)
        csvContent = csvHeader ++ concat csvRows
    writeFile (outputDir ++ "/simulation_steps.csv") csvContent

    putStrLn $ "Environment results saved to " ++ outputDir

-- | Enhanced agent results saving
saveAgentResults :: ActiveInferenceAgent -> FilePath -> IO ()
saveAgentResults agent outputDir = do
    createDirectoryIfMissing True outputDir

    -- Save configuration
    writeFile (outputDir ++ "/config.txt") (show $ config agent)

    -- Save statistics
    let stats = getAgentStatistics agent
    writeFile (outputDir ++ "/statistics.txt") (show stats)

    -- Save belief history
    let beliefLines = "Step," ++ concat ["State" ++ show i ++ "," | i <- [0..V.length (head $ beliefHistory agent)-1]] ++ "\n" ++
                     concat [show step ++ "," ++
                            concat (L.intersperse "," [show b | b <- V.toList beliefs]) ++ "\n"
                           | (step, beliefs) <- zip [0..] (beliefHistory agent)]
    writeFile (outputDir ++ "/belief_history.csv") beliefLines

    -- Save action history
    let actionLines = "Step,Action\n" ++
                     concat [show step ++ "," ++ show action ++ "\n"
                           | (step, action) <- zip [0..] (actionHistory agent)]
    writeFile (outputDir ++ "/action_history.csv") actionLines

    -- Save free energy history
    let feLines = "Step,FreeEnergy\n" ++
                 concat [show step ++ "," ++ show fe ++ "\n"
                        | (step, fe) <- zip [0..] (freeEnergyHistory agent)]
    writeFile (outputDir ++ "/free_energy_history.csv") feLines

    putStrLn $ "Agent results saved to " ++ outputDir

-- | Initialize output directories at startup
initializeDemo :: IO ()
initializeDemo = do
    putStrLn "🎓 Active Inference Haskell Implementation"
    putStrLn "========================================"
    createOutputDirectories
    putStrLn "Output directories initialized"
    putStrLn ""

-- | Enhanced main with initialization
mainWithInit :: IO ()
mainWithInit = do
    initializeDemo
    main
