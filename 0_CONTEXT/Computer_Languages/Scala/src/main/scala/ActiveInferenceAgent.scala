package activeinference

import scala.collection.mutable.ArrayBuffer
import scala.math.{exp, log, max, min}
import scala.util.Random

/**
 * Active Inference Agent Implementation in Scala
 *
 * This implementation demonstrates the Active Inference framework using Scala's
 * functional programming capabilities, immutable data structures, and type safety.
 */

// Core data types
case class GenerativeModel(
  aMatrix: Vector[Vector[Double]], // Likelihood P(o|s)
  bMatrix: Vector[Vector[Vector[Double]]], // Transition P(s'|s,a)
  cVector: Vector[Double], // Preferences P(o)
  dVector: Vector[Double]  // Prior beliefs P(s)
)

case class AgentState(
  beliefs: Vector[Double],
  observations: Vector[Int],
  actions: Vector[Int],
  freeEnergy: Vector[Double]
)

case class AgentConfig(
  nStates: Int = 4,
  nObservations: Int = 3,
  nActions: Int = 2,
  precision: Double = 1.0,
  learningRate: Double = 0.1,
  maxIterations: Int = 100
) {
  require(nStates > 0, "Number of states must be positive")
  require(nObservations > 0, "Number of observations must be positive")
  require(nActions > 0, "Number of actions must be positive")
  require(precision > 0, "Precision must be positive")
  require(learningRate > 0 && learningRate <= 1, "Learning rate must be in (0, 1]")
}

/**
 * Active Inference Agent
 */
class ActiveInferenceAgent(config: AgentConfig) {

  private val random = new Random()

  // Initialize generative model
  private val generativeModel = initializeGenerativeModel()
  private var currentBeliefs = generativeModel.dVector
  private var history = AgentState(
    beliefs = Vector.empty,
    observations = Vector.empty,
    actions = Vector.empty,
    freeEnergy = Vector.empty
  )

  /**
   * Initialize the generative model matrices
   */
  private def initializeGenerativeModel(): GenerativeModel = {
    // A-matrix: Likelihood P(o|s)
    val aMatrix = Vector.tabulate(config.nObservations, config.nStates) { (o, s) =>
      val isDiagonal = (s % config.nObservations) == o
      val baseProb = if (isDiagonal) 0.8 else 0.2 / (config.nObservations - 1)
      val noise = random.nextDouble() * 0.2 - 0.1 // ±0.1 noise
      max(0.0, min(1.0, baseProb + noise))
    }

    // Normalize A-matrix rows
    val normalizedAMatrix = aMatrix.map { row =>
      val sum = row.sum
      if (sum > 0) row.map(_ / sum) else row
    }

    // B-matrix: State transitions P(s'|s,a)
    val bMatrix = Vector.tabulate(config.nActions, config.nStates, config.nStates) { (a, s, sNext) =>
      val transitionType = (sNext - s + config.nStates) % config.nStates
      (a, transitionType) match {
        case (0, 0) => 0.6  // Stay action
        case (1, 1) => 0.6  // Right action (forward)
        case (2, _) if config.nActions > 2 && transitionType == config.nStates - 1 => 0.6  // Left action
        case _ => 1.0 / config.nStates  // Random exploration
      }
    }

    // Normalize B-matrix
    val normalizedBMatrix = bMatrix.map { actionMatrix =>
      actionMatrix.map { stateRow =>
        val sum = stateRow.sum
        if (sum > 0) stateRow.map(_ / sum) else stateRow
      }
    }

    // C-vector: Observation preferences
    val cVector = Vector.tabulate(config.nObservations) { o =>
      if (o < config.nObservations / 2) 1.0 else 0.1
    }

    // D-vector: Prior beliefs
    val dVector = Vector.fill(config.nStates)(1.0 / config.nStates)

    GenerativeModel(normalizedAMatrix, normalizedBMatrix, cVector, dVector)
  }

  /**
   * Update beliefs based on observation using Bayesian inference
   */
  def updateBeliefs(observation: Int): Vector[Double] = {
    require(observation >= 0 && observation < config.nObservations,
      s"Invalid observation: $observation")

    // Get likelihood for this observation
    val likelihood = generativeModel.aMatrix(observation)

    // Bayesian update: posterior ∝ likelihood × prior
    val posterior = likelihood.zip(currentBeliefs).map { case (l, b) => l * b }

    // Normalize
    val sum = posterior.sum
    currentBeliefs = if (sum > 0) posterior.map(_ / sum) else posterior

    // Update history
    history = history.copy(beliefs = history.beliefs :+ currentBeliefs)

    currentBeliefs
  }

  /**
   * Calculate expected free energy for an action
   */
  def calculateExpectedFreeEnergy(action: Int): Double = {
    require(action >= 0 && action < config.nActions, s"Invalid action: $action")

    // Predict next beliefs
    val predictedBeliefs = predictBeliefs(action)

    // Calculate pragmatic value (surprise about preferred observations)
    val pragmaticValue = calculatePragmaticValue(predictedBeliefs)

    // Calculate epistemic value (information gain)
    val epistemicValue = calculateEpistemicValue(predictedBeliefs)

    // Expected free energy
    pragmaticValue - config.precision * epistemicValue
  }

  /**
   * Select action by minimizing expected free energy
   */
  def selectAction(): Int = {
    val efes = (0 until config.nActions).map { action =>
      action -> calculateExpectedFreeEnergy(action)
    }

    // Select action with minimum EFE
    val (bestAction, _) = efes.minBy(_._2)
    bestAction
  }

  /**
   * Execute one perception-action cycle
   */
  def step(observation: Int): (Int, Double) = {
    // Update beliefs
    updateBeliefs(observation)

    // Calculate free energy
    val fe = calculateVariationalFreeEnergy()
    history = history.copy(freeEnergy = history.freeEnergy :+ fe)

    // Select action
    val action = selectAction()
    history = history.copy(actions = history.actions :+ action)
    history = history.copy(observations = history.observations :+ observation)

    (action, fe)
  }

  /**
   * Predict beliefs after taking an action
   */
  private def predictBeliefs(action: Int): Vector[Double] = {
    val bAction = generativeModel.bMatrix(action)

    // Compute predicted beliefs: P(s') = sum_s P(s'|s,a) * P(s)
    Vector.tabulate(config.nStates) { sNext =>
      (0 until config.nStates).map { s =>
        bAction(s)(sNext) * currentBeliefs(s)
      }.sum
    }
  }

  /**
   * Calculate pragmatic value (expected surprise about preferred observations)
   */
  private def calculatePragmaticValue(predictedBeliefs: Vector[Double]): Double = {
    var pragmaticValue = 0.0

    for (state <- 0 until config.nStates) {
      if (predictedBeliefs(state) > 0) {
        for (obs <- 0 until config.nObservations) {
          val obsProb = generativeModel.aMatrix(obs)(state)
          val preference = generativeModel.cVector(obs)
          pragmaticValue += predictedBeliefs(state) * obsProb * preference
        }
      }
    }

    pragmaticValue
  }

  /**
   * Calculate epistemic value (information gain)
   */
  private def calculateEpistemicValue(predictedBeliefs: Vector[Double]): Double = {
    calculateEntropy(predictedBeliefs)
  }

  /**
   * Calculate variational free energy
   */
  def calculateVariationalFreeEnergy(): Double = {
    val expectedLikelihood = calculateExpectedLikelihood()
    val entropy = calculateEntropy(currentBeliefs)
    -expectedLikelihood - entropy
  }

  /**
   * Calculate expected likelihood
   */
  private def calculateExpectedLikelihood(): Double = {
    var expectedLikelihood = 0.0

    for (obs <- 0 until config.nObservations) {
      val likelihood = generativeModel.aMatrix(obs)
      val expectedObsProb = likelihood.zip(currentBeliefs).map { case (l, b) => l * b }.sum

      if (expectedObsProb > 0) {
        expectedLikelihood += expectedObsProb * log(expectedObsProb)
      }
    }

    expectedLikelihood
  }

  /**
   * Calculate entropy of belief distribution
   */
  private def calculateEntropy(beliefs: Vector[Double]): Double = {
    -beliefs.filter(_ > 0).map(p => p * log(p)).sum
  }

  /**
   * Learn from experience (simplified)
   */
  def learn(observation: Int, action: Int, nextObservation: Int): Unit = {
    // Simple learning: reinforce the most likely state
    val maxState = currentBeliefs.zipWithIndex.maxBy(_._1)._2

    // Update A-matrix (observation likelihood)
    val currentProb = generativeModel.aMatrix(observation)(maxState)
    val newProb = currentProb + config.learningRate
    // Note: In a full implementation, you'd create a new GenerativeModel
    // For simplicity, we're not updating the immutable model here
  }

  /**
   * Get current beliefs
   */
  def getBeliefs: Vector[Double] = currentBeliefs

  /**
   * Get agent history
   */
  def getHistory: AgentState = history

  /**
   * Get agent statistics
   */
  def getStatistics: Map[String, Any] = {
    Map(
      "totalSteps" -> history.actions.length,
      "currentBeliefs" -> currentBeliefs,
      "totalObservations" -> history.observations.length,
      "averageFreeEnergy" -> (if (history.freeEnergy.nonEmpty) history.freeEnergy.sum / history.freeEnergy.length else 0.0),
      "beliefEntropy" -> calculateEntropy(currentBeliefs),
      "config" -> config
    )
  }

  /**
   * Print agent statistics
   */
  def printStatistics(): Unit = {
    val stats = getStatistics()
    println("Active Inference Agent Statistics:")
    println("===================================")
    println(s"States: ${config.nStates}, Observations: ${config.nObservations}, Actions: ${config.nActions}")
    println(f"Precision: ${config.precision}%.2f, Learning Rate: ${config.learningRate}%.2f")
    println(s"Total steps: ${stats("totalSteps")}")
    print("Final beliefs: [")
    currentBeliefs.zipWithIndex.foreach { case (belief, i) =>
      print(f"$belief%.3f")
      if (i < currentBeliefs.length - 1) print(", ")
    }
    println("]")
    println(f"Average free energy: ${stats("averageFreeEnergy")}%.4f")
    println(f"Belief entropy: ${stats("beliefEntropy")}%.4f")
  }
}

/**
 * Demonstration object
 */
object ActiveInferenceDemo {
  def run(): Unit = {
    println("🧠 Active Inference Scala Implementation")
    println("=======================================")
    println()

    // Create agent
    val config = AgentConfig(nStates = 3, nObservations = 3, nActions = 2)
    val agent = new ActiveInferenceAgent(config)

    println(s"Creating agent with ${config.nStates} states, ${config.nObservations} observations, ${config.nActions} actions...")
    println()

    // Print initial beliefs
    val initialBeliefs = agent.getBeliefs
    print("Initial beliefs: [")
    initialBeliefs.zipWithIndex.foreach { case (belief, i) =>
      print(f"$belief%.3f")
      if (i < initialBeliefs.length - 1) print(", ")
    }
    println("]")
    println()

    // Run simulation
    val nSteps = 10
    println(s"Running simulation for $nSteps steps...")
    println()

    for (step <- 1 to nSteps) {
      // Generate random observation
      val observation = random.nextInt(config.nObservations)

      println(s"Step $step:")
      println(s"  Observation: $observation")

      // Execute perception-action cycle
      val (action, freeEnergy) = agent.step(observation)

      println(s"  Selected action: $action")

      // Print current beliefs
      val currentBeliefs = agent.getBeliefs
      print("  Updated beliefs: [")
      currentBeliefs.zipWithIndex.foreach { case (belief, i) =>
        print(f"$belief%.3f")
        if (i < currentBeliefs.length - 1) print(", ")
      }
      println("]")
      println(f"  Free energy: $freeEnergy%.4f")
      println()
    }

    // Print final statistics
    println()
    agent.printStatistics()

    println()
    println("✅ Scala Active Inference simulation completed!")
  }

  def runMultiAgentDemo(): Unit = {
    println()
    println("🐜 Multi-Agent Scala Demo")
    println("=========================")
    println()

    val nAgents = 3
    val agents = (1 to nAgents).map(_ => new ActiveInferenceAgent(AgentConfig()))

    // Run multi-agent simulation
    for (step <- 1 to 5) {
      println(s"Multi-agent Step $step:")

      agents.zipWithIndex.foreach { case (agent, i) =>
        val observation = random.nextInt(3)
        val (action, _) = agent.step(observation)

        val beliefs = agent.getBeliefs
        val maxBelief = beliefs.max

        println(f"  Agent ${i + 1}: Obs=$observation, Action=$action, Best Belief=$maxBelief%.3f")
      }
      println()
    }

    println("✅ Multi-agent simulation completed!")
  }

  // Run demo if this file is executed directly
  def main(args: Array[String]): Unit = {
    run()
    runMultiAgentDemo()
  }
}
