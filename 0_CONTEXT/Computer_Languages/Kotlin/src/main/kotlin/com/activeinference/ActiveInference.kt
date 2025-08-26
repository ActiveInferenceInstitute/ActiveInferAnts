package com.activeinference

import kotlinx.coroutines.*
import org.apache.commons.math3.linear.*
import java.io.File
import java.io.PrintWriter
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import kotlin.math.*
import kotlin.random.Random

// Core data classes
data class AgentConfig(
    val nStates: Int = 3,
    val nObservations: Int = 3,
    val nActions: Int = 3,
    val learningRate: Double = 0.1,
    val uncertaintyWeight: Double = 0.1,
    val precision: Double = 1.0,
    val enableLogging: Boolean = false,
    val outputDirectory: String = "output/single_agent",
    val randomSeed: Int = 42
) {
    init {
        require(nStates > 0) { "Number of states must be positive" }
        require(nObservations > 0) { "Number of observations must be positive" }
        require(nActions > 0) { "Number of actions must be positive" }
        require(learningRate > 0.0 && learningRate <= 1.0) { "Learning rate must be in (0, 1]" }
        require(uncertaintyWeight >= 0.0) { "Uncertainty weight must be non-negative" }
        require(precision > 0.0) { "Precision must be positive" }
    }
}

data class FreeEnergy(
    val variational: Double = 0.0,
    val expected: Double = 0.0,
    val pragmatic: Double = 0.0,
    val epistemic: Double = 0.0
) {
    companion object {
        val ZERO = FreeEnergy()
    }
}

data class AgentStatistics(
    val totalSteps: Int = 0,
    val averageFreeEnergy: Double = 0.0,
    val actionDistribution: Map<Int, Int> = emptyMap(),
    val finalBeliefs: List<Double> = emptyList(),
    val totalExecutionTime: Double = 0.0,
    val timestamp: LocalDateTime = LocalDateTime.now()
)

// Custom exceptions
class ActiveInferenceException(message: String) : Exception(message)
class BeliefUpdateError(message: String) : ActiveInferenceException(message)
class PolicySelectionError(message: String) : ActiveInferenceException(message)

// Active Inference Agent
class ActiveInferenceAgent(private val config: AgentConfig) {

    // Generative model matrices
    private val A: RealMatrix // Likelihood matrix p(o|s)
    private val B: List<RealMatrix> // Transition matrices p(s'|s,a)
    private val C: RealVector // Preferences p(o)
    private val D: RealVector // Prior beliefs p(s)

    // Current state
    private var currentBeliefs: RealVector

    // History tracking
    private val beliefHistory = mutableListOf<RealVector>()
    private val actionHistory = mutableListOf<Int>()
    private val observationHistory = mutableListOf<Int>()
    private val freeEnergyHistory = mutableListOf<Double>()
    private val timestampHistory = mutableListOf<LocalDateTime>()

    // Random number generator
    private val random = Random(config.randomSeed)

    init {
        log("Initializing Active Inference Agent...")

        A = initializeLikelihoodMatrix()
        B = initializeTransitionMatrices()
        C = initializePreferenceVector()
        D = initializePriorVector()
        currentBeliefs = D.copy()

        // Record initial state
        beliefHistory.add(currentBeliefs.copy())
        timestampHistory.add(LocalDateTime.now())

        log("Agent initialized with ${config.nStates} states, ${config.nObservations} observations, ${config.nActions} actions")
    }

    // Initialize likelihood matrix A (p(o|s))
    private fun initializeLikelihoodMatrix(): RealMatrix {
        val matrix = Array2DRowRealMatrix(config.nObservations, config.nStates)

        for (obs in 0 until config.nObservations) {
            val row = DoubleArray(config.nStates) { state ->
                // Diagonal structure with noise
                val isDiagonal = obs == state % config.nObservations
                val baseProb = if (isDiagonal) 0.7 else 0.1
                val noise = random.nextDouble(-0.1, 0.1)
                max(0.0, min(1.0, baseProb + noise))
            }

            // Normalize row
            val sum = row.sum()
            val normalizedRow = row.map { it / sum }
            matrix.setRow(obs, normalizedRow)
        }

        return matrix
    }

    // Initialize transition matrices B (p(s'|s,a))
    private fun initializeTransitionMatrices(): List<RealMatrix> {
        return List(config.nActions) { action ->
            val matrix = Array2DRowRealMatrix(config.nStates, config.nStates)

            for (fromState in 0 until config.nStates) {
                val row = DoubleArray(config.nStates) { toState ->
                    when {
                        action == 0 && fromState == toState -> 0.6  // Stay action
                        action == 1 && toState == min(config.nStates - 1, fromState + 1) -> 0.6  // Right action
                        action == 2 && fromState > 0 && toState == fromState - 1 -> 0.6  // Left action
                        else -> 1.0 / config.nStates  // Random exploration
                    }
                }

                // Normalize row
                val sum = row.sum()
                val normalizedRow = row.map { it / sum }
                matrix.setRow(fromState, normalizedRow)
            }

            matrix
        }
    }

    // Initialize preference vector C (p(o))
    private fun initializePreferenceVector(): RealVector {
        val preferences = DoubleArray(config.nObservations) { obs ->
            if (obs < config.nObservations / 2) 1.0 else 0.1
        }
        return ArrayRealVector(preferences)
    }

    // Initialize prior vector D (p(s))
    private fun initializePriorVector(): RealVector {
        val uniformProb = 1.0 / config.nStates
        return ArrayRealVector(DoubleArray(config.nStates) { uniformProb })
    }

    // Update beliefs given observation (synchronous)
    fun updateBeliefs(observation: Int): RealVector {
        require(observation in 0 until config.nObservations) {
            "Invalid observation index: $observation"
        }

        try {
            // Get likelihood for this observation
            val likelihood = A.getRowVector(observation)

            // Bayesian update: posterior = prior * likelihood
            val posterior = currentBeliefs.ebeMultiply(likelihood)

            // Normalize
            val sum = posterior.l1Norm
            if (sum == 0.0) {
                throw BeliefUpdateError("Invalid likelihood - posterior sums to zero")
            }

            currentBeliefs = posterior.mapDivide(sum)

            // Record in history
            beliefHistory.add(currentBeliefs.copy())
            timestampHistory.add(LocalDateTime.now())

            if (config.enableLogging) {
                log("Beliefs updated for observation $observation")
            }

            return currentBeliefs.copy()

        } catch (e: Exception) {
            throw BeliefUpdateError("Failed to update beliefs: ${e.message}")
        }
    }

    // Update beliefs given observation (asynchronous)
    suspend fun updateBeliefsAsync(observation: Int): RealVector = withContext(Dispatchers.Default) {
        updateBeliefs(observation)
    }

    // Calculate variational free energy
    fun calculateVariationalFreeEnergy(): Double {
        val expectedLikelihood = calculateExpectedLikelihood()
        val entropy = calculateEntropy(currentBeliefs)
        return -expectedLikelihood - entropy
    }

    // Calculate expected free energy for an action
    fun calculateExpectedFreeEnergy(action: Int): FreeEnergy {
        require(action in 0 until config.nActions) {
            "Invalid action index: $action"
        }

        try {
            // Predict next beliefs
            val predictedBeliefs = predictBeliefs(action)

            // Calculate pragmatic value (surprise about preferred observations)
            val pragmaticValue = calculatePragmaticValue(predictedBeliefs)

            // Calculate epistemic value (information gain)
            val epistemicValue = calculateEpistemicValue(predictedBeliefs)

            // Total EFE
            val expectedFE = pragmaticValue - config.uncertaintyWeight * epistemicValue

            return FreeEnergy(
                variational = calculateVariationalFreeEnergy(),
                expected = expectedFE,
                pragmatic = pragmaticValue,
                epistemic = epistemicValue
            )

        } catch (e: Exception) {
            throw PolicySelectionError("Failed to calculate expected free energy: ${e.message}")
        }
    }

    // Select action by minimizing expected free energy (synchronous)
    fun selectAction(): Int {
        try {
            val efes = (0 until config.nActions).map { action ->
                action to calculateExpectedFreeEnergy(action).expected
            }

            // Select action with minimum expected free energy
            val (bestAction, minEFE) = efes.minByOrNull { it.second }!!

            if (config.enableLogging) {
                log("Action $bestAction selected with EFE $minEFE")
            }

            return bestAction

        } catch (e: Exception) {
            throw PolicySelectionError("Failed to select action: ${e.message}")
        }
    }

    // Select action by minimizing expected free energy (asynchronous)
    suspend fun selectActionAsync(): Int = withContext(Dispatchers.Default) {
        selectAction()
    }

    // Execute one step of the perception-action loop (synchronous)
    fun step(observation: Int): Int {
        updateBeliefs(observation)

        // Calculate free energy
        val fe = calculateVariationalFreeEnergy()
        freeEnergyHistory.add(fe)

        // Select and return action
        val action = selectAction()
        recordHistory(action, observation)

        return action
    }

    // Execute one step of the perception-action loop (asynchronous)
    suspend fun stepAsync(observation: Int): Int = coroutineScope {
        val deferredUpdate = async { updateBeliefsAsync(observation) }
        val deferredAction = async { selectActionAsync() }

        deferredUpdate.await()

        // Calculate free energy
        val fe = calculateVariationalFreeEnergy()
        freeEnergyHistory.add(fe)

        // Select action
        val action = deferredAction.await()
        recordHistory(action, observation)

        action
    }

    // Get agent statistics
    fun getStatistics(): AgentStatistics {
        if (actionHistory.isEmpty()) {
            return AgentStatistics(finalBeliefs = currentBeliefs.toArray().toList())
        }

        val totalSteps = actionHistory.size
        val avgFE = freeEnergyHistory.average()
        val actionDist = actionHistory.groupingBy { it }.eachCount()

        val timestamps = timestampHistory.map { it.toEpochSecond(java.time.ZoneOffset.UTC) }
        val timeDiff = if (timestamps.size > 1) {
            (timestamps.last() - timestamps.first()).toDouble()
        } else 0.0

        return AgentStatistics(
            totalSteps = totalSteps,
            averageFreeEnergy = avgFE,
            actionDistribution = actionDist,
            finalBeliefs = currentBeliefs.toArray().toList(),
            totalExecutionTime = timeDiff,
            timestamp = LocalDateTime.now()
        )
    }

    // Save results to output directory
    suspend fun saveResults() = withContext(Dispatchers.IO) {
        try {
            val outputDir = File(config.outputDirectory)
            outputDir.mkdirs()

            // Save configuration
            val configFile = File(outputDir, "config.json")
            configFile.writeText("""
                {
                    "nStates": ${config.nStates},
                    "nObservations": ${config.nObservations},
                    "nActions": ${config.nActions},
                    "learningRate": ${config.learningRate},
                    "uncertaintyWeight": ${config.uncertaintyWeight},
                    "precision": ${config.precision}
                }
            """.trimIndent())

            // Save statistics
            val stats = getStatistics()
            val statsFile = File(outputDir, "statistics.json")
            statsFile.writeText("""
                {
                    "totalSteps": ${stats.totalSteps},
                    "averageFreeEnergy": ${stats.averageFreeEnergy},
                    "actionDistribution": {${stats.actionDistribution.entries.joinToString(",") { "\"${it.key}\": ${it.value}" }}},
                    "finalBeliefs": [${stats.finalBeliefs.joinToString(",")}],
                    "totalExecutionTime": ${stats.totalExecutionTime}
                }
            """.trimIndent())

            // Save belief history
            val beliefFile = File(outputDir, "belief_history.csv")
            beliefFile.printWriter().use { writer ->
                writer.println("Step,State0,State1,State2") // Assuming 3 states
                beliefHistory.forEachIndexed { step, beliefs ->
                    writer.print("$step")
                    beliefs.toArray().forEach { belief ->
                        writer.print(",${belief}")
                    }
                    writer.println()
                }
            }

            // Save action history
            val actionFile = File(outputDir, "action_history.csv")
            actionFile.printWriter().use { writer ->
                writer.println("Step,Action,Observation")
                actionHistory.forEachIndexed { step, action ->
                    val observation = observationHistory.getOrNull(step) ?: 0
                    writer.println("$step,$action,$observation")
                }
            }

            // Save free energy history
            val feFile = File(outputDir, "free_energy_history.csv")
            feFile.printWriter().use { writer ->
                writer.println("Step,FreeEnergy")
                freeEnergyHistory.forEachIndexed { step, fe ->
                    writer.println("$step,$fe")
                }
            }

            if (config.enableLogging) {
                log("Results saved to ${config.outputDirectory}")
            }

        } catch (e: Exception) {
            throw ActiveInferenceException("Failed to save results: ${e.message}")
        }
    }

    // Helper methods
    private fun predictBeliefs(action: Int): RealVector {
        val bMatrix = B[action]
        return currentBeliefs.transpose() * bMatrix
    }

    private fun calculatePragmaticValue(predictedBeliefs: RealVector): Double {
        var pragmaticValue = 0.0

        for (state in 0 until config.nStates) {
            val stateProb = predictedBeliefs.getEntry(state)
            if (stateProb > 0.0) {
                for (obs in 0 until config.nObservations) {
                    val obsProb = A.getEntry(obs, state)
                    val preference = C.getEntry(obs)
                    pragmaticValue += stateProb * obsProb * preference
                }
            }
        }

        return pragmaticValue
    }

    private fun calculateEpistemicValue(predictedBeliefs: RealVector): Double {
        return calculateEntropy(predictedBeliefs)
    }

    private fun calculateEntropy(beliefs: RealVector): Double {
        var entropy = 0.0
        for (i in 0 until beliefs.dimension) {
            val prob = beliefs.getEntry(i)
            if (prob > 0.0) {
                entropy -= prob * ln(prob) / ln(2.0)
            }
        }
        return entropy
    }

    private fun calculateExpectedLikelihood(): Double {
        var expectedLikelihood = 0.0

        for (obs in 0 until config.nObservations) {
            val likelihood = A.getRowVector(obs)
            val expectedObsProb = currentBeliefs.dotProduct(likelihood)
            if (expectedObsProb > 0.0) {
                expectedLikelihood += expectedObsProb * ln(expectedObsProb)
            }
        }

        return expectedLikelihood
    }

    private fun recordHistory(action: Int, observation: Int) {
        actionHistory.add(action)
        observationHistory.add(observation)
    }

    private fun log(message: String) {
        if (config.enableLogging) {
            println("[ActiveInferenceAgent] $message")
        }
    }

    // Public properties for access
    val currentBeliefsVector: RealVector
        get() = currentBeliefs.copy()

    val generativeModel: Triple<RealMatrix, List<RealMatrix>, RealVector>
        get() = Triple(A.copy(), B.map { it.copy() }, C.copy())
}
