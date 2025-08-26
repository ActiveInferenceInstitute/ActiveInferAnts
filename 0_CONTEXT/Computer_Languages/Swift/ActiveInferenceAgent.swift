import Foundation

/**
 * Active Inference Implementation in Swift
 *
 * This implementation demonstrates the Active Inference framework using Swift's
 * modern language features, type safety, and performance optimizations.
 */

// MARK: - Core Data Structures

struct GenerativeModel {
    let aMatrix: [[Double]]  // Likelihood P(o|s)
    let bMatrix: [[[Double]]] // Transition P(s'|s,a)
    let cVector: [Double]    // Preferences P(o)
    let dVector: [Double]    // Prior beliefs P(s)

    init(aMatrix: [[Double]], bMatrix: [[[Double]]], cVector: [Double], dVector: [Double]) {
        self.aMatrix = aMatrix
        self.bMatrix = bMatrix
        self.cVector = cVector
        self.dVector = dVector
    }
}

struct AgentState {
    var beliefs: [Double]
    var observations: [Int]
    var actions: [Int]
    var freeEnergy: [Double]

    init(beliefs: [Double] = [], observations: [Int] = [], actions: [Int] = [], freeEnergy: [Double] = []) {
        self.beliefs = beliefs
        self.observations = observations
        self.actions = actions
        self.freeEnergy = freeEnergy
    }
}

struct AgentConfig {
    let nStates: Int
    let nObservations: Int
    let nActions: Int
    let precision: Double
    let learningRate: Double
    let maxIterations: Int

    init(nStates: Int = 4, nObservations: Int = 3, nActions: Int = 2,
         precision: Double = 1.0, learningRate: Double = 0.1, maxIterations: Int = 100) {
        precondition(nStates > 0, "Number of states must be positive")
        precondition(nObservations > 0, "Number of observations must be positive")
        precondition(nActions > 0, "Number of actions must be positive")
        precondition(precision > 0, "Precision must be positive")
        precondition(learningRate > 0 && learningRate <= 1, "Learning rate must be in (0, 1]")

        self.nStates = nStates
        self.nObservations = nObservations
        self.nActions = nActions
        self.precision = precision
        self.learningRate = learningRate
        self.maxIterations = maxIterations
    }
}

// MARK: - Active Inference Agent

class ActiveInferenceAgent {
    private let config: AgentConfig
    private let generativeModel: GenerativeModel
    private var currentBeliefs: [Double]
    private var history: AgentState

    init(config: AgentConfig = AgentConfig()) {
        self.config = config
        self.generativeModel = Self.initializeGenerativeModel(config: config)
        self.currentBeliefs = generativeModel.dVector
        self.history = AgentState(beliefs: [generativeModel.dVector])
    }

    // MARK: - Generative Model Initialization

    private static func initializeGenerativeModel(config: AgentConfig) -> GenerativeModel {
        // A-matrix: Likelihood P(o|s)
        let aMatrix = (0..<config.nObservations).map { o in
            (0..<config.nStates).map { s -> Double in
                // Diagonal structure with noise
                let isDiagonal = (s % config.nObservations) == o
                let baseProb = isDiagonal ? 0.8 : 0.2 / Double(config.nObservations - 1)
                let noise = Double.random(in: -0.1...0.1) // ±0.1 noise
                return max(0.0, min(1.0, baseProb + noise))
            }
        }

        // Normalize A-matrix rows
        let normalizedAMatrix = aMatrix.map { row in
            let sum = row.reduce(0, +)
            return sum > 0 ? row.map { $0 / sum } : row
        }

        // B-matrix: State transitions P(s'|s,a)
        let bMatrix = (0..<config.nActions).map { a in
            (0..<config.nStates).map { s in
                (0..<config.nStates).map { sNext -> Double in
                    let transitionType = (sNext - s + config.nStates) % config.nStates
                    switch (a, transitionType) {
                    case (0, 0): return 0.6  // Stay action
                    case (1, 1): return 0.6  // Right action (forward)
                    case (2, _) where config.nActions > 2 && transitionType == config.nStates - 1: return 0.6  // Left action
                    default: return 1.0 / Double(config.nStates)  // Random exploration
                    }
                }
            }
        }

        // Normalize B-matrix
        let normalizedBMatrix = bMatrix.map { actionMatrix in
            actionMatrix.map { stateRow in
                let sum = stateRow.reduce(0, +)
                return sum > 0 ? stateRow.map { $0 / sum } : stateRow
            }
        }

        // C-vector: Observation preferences
        let cVector = (0..<config.nObservations).map { o -> Double in
            o < config.nObservations / 2 ? 1.0 : 0.1
        }

        // D-vector: Prior beliefs
        let dVector = Array(repeating: 1.0 / Double(config.nStates), count: config.nStates)

        return GenerativeModel(
            aMatrix: normalizedAMatrix,
            bMatrix: normalizedBMatrix,
            cVector: cVector,
            dVector: dVector
        )
    }

    // MARK: - Core Active Inference Methods

    /// Update beliefs based on observation using Bayesian inference
    func updateBeliefs(observation: Int) -> [Double] {
        precondition(observation >= 0 && observation < config.nObservations,
                    "Invalid observation: \(observation)")

        // Get likelihood for this observation
        let likelihood = generativeModel.aMatrix[observation]

        // Bayesian update: posterior ∝ likelihood × prior
        let posterior = zip(likelihood, currentBeliefs).map { $0 * $1 }

        // Normalize
        let sum = posterior.reduce(0, +)
        currentBeliefs = sum > 0 ? posterior.map { $0 / sum } : posterior

        // Update history
        history.beliefs.append(currentBeliefs)

        return currentBeliefs
    }

    /// Calculate expected free energy for an action
    func calculateExpectedFreeEnergy(action: Int) -> Double {
        precondition(action >= 0 && action < config.nActions, "Invalid action: \(action)")

        // Predict next beliefs
        let predictedBeliefs = predictBeliefs(action: action)

        // Calculate pragmatic value (surprise about preferred observations)
        let pragmaticValue = calculatePragmaticValue(predictedBeliefs: predictedBeliefs)

        // Calculate epistemic value (information gain)
        let epistemicValue = calculateEpistemicValue(predictedBeliefs: predictedBeliefs)

        // Expected free energy
        return pragmaticValue - config.precision * epistemicValue
    }

    /// Select action by minimizing expected free energy
    func selectAction() -> Int {
        let efes = (0..<config.nActions).map { action -> (Int, Double) in
            (action, calculateExpectedFreeEnergy(action: action))
        }

        // Select action with minimum EFE
        let (bestAction, _) = efes.min { $0.1 < $1.1 }!
        return bestAction
    }

    /// Execute one perception-action cycle
    func step(observation: Int) -> (Int, Double) {
        // Update beliefs
        updateBeliefs(observation: observation)

        // Calculate free energy
        let fe = calculateVariationalFreeEnergy()
        history.freeEnergy.append(fe)

        // Select action
        let action = selectAction()
        history.actions.append(action)
        history.observations.append(observation)

        return (action, fe)
    }

    /// Predict beliefs after taking an action
    private func predictBeliefs(action: Int) -> [Double] {
        let bAction = generativeModel.bMatrix[action]

        // Compute predicted beliefs: P(s') = sum_s P(s'|s,a) * P(s)
        return (0..<config.nStates).map { sNext in
            (0..<config.nStates).reduce(0.0) { sum, s in
                sum + bAction[s][sNext] * currentBeliefs[s]
            }
        }
    }

    /// Calculate pragmatic value (expected surprise about preferred observations)
    private func calculatePragmaticValue(predictedBeliefs: [Double]) -> Double {
        var pragmaticValue = 0.0

        for state in 0..<config.nStates {
            if predictedBeliefs[state] > 0 {
                for obs in 0..<config.nObservations {
                    let obsProb = generativeModel.aMatrix[obs][state]
                    let preference = generativeModel.cVector[obs]
                    pragmaticValue += predictedBeliefs[state] * obsProb * preference
                }
            }
        }

        return pragmaticValue
    }

    /// Calculate epistemic value (information gain)
    private func calculateEpistemicValue(predictedBeliefs: [Double]) -> Double {
        return calculateEntropy(beliefs: predictedBeliefs)
    }

    /// Calculate variational free energy
    func calculateVariationalFreeEnergy() -> Double {
        let expectedLikelihood = calculateExpectedLikelihood()
        let entropy = calculateEntropy(beliefs: currentBeliefs)
        return -expectedLikelihood - entropy
    }

    /// Calculate expected likelihood
    private func calculateExpectedLikelihood() -> Double {
        var expectedLikelihood = 0.0

        for obs in 0..<config.nObservations {
            let likelihood = generativeModel.aMatrix[obs]
            let expectedObsProb = zip(likelihood, currentBeliefs).map { $0 * $1 }.reduce(0, +)

            if expectedObsProb > 0 {
                expectedLikelihood += expectedObsProb * log(expectedObsProb)
            }
        }

        return expectedLikelihood
    }

    /// Calculate entropy of belief distribution
    private func calculateEntropy(beliefs: [Double]) -> Double {
        return -beliefs.filter { $0 > 0 }.reduce(0.0) { $0 - $1 * log($1) }
    }

    // MARK: - Learning

    /// Learn from experience (simplified)
    func learn(observation: Int, action: Int, nextObservation: Int) {
        // Simple learning: reinforce the most likely state
        guard let maxState = currentBeliefs.enumerated().max(by: { $0.element < $1.element })?.offset else {
            return
        }

        // Update A-matrix (observation likelihood)
        let currentProb = generativeModel.aMatrix[observation][maxState]
        let newProb = currentProb + config.learningRate
        // Note: In a full implementation, you'd create a new GenerativeModel
        // For simplicity, we're not updating the immutable model here
    }

    // MARK: - Public Interface

    /// Get current beliefs
    func getBeliefs() -> [Double] {
        return currentBeliefs
    }

    /// Get agent history
    func getHistory() -> AgentState {
        return history
    }

    /// Get agent statistics
    func getStatistics() -> [String: Any] {
        return [
            "totalSteps": history.actions.count,
            "currentBeliefs": currentBeliefs,
            "totalObservations": history.observations.count,
            "averageFreeEnergy": history.freeEnergy.isEmpty ? 0.0 :
                history.freeEnergy.reduce(0, +) / Double(history.freeEnergy.count),
            "beliefEntropy": calculateEntropy(beliefs: currentBeliefs),
            "config": config
        ]
    }

    /// Print agent statistics
    func printStatistics() {
        let stats = getStatistics()
        print("Active Inference Agent Statistics:")
        print("===================================")
        print("States: \(config.nStates), Observations: \(config.nObservations), Actions: \(config.nActions)")
        print("Precision: \(String(format: "%.2f", config.precision)), Learning Rate: \(String(format: "%.2f", config.learningRate))")
        print("Total steps: \(stats["totalSteps"] as! Int)")
        print("Final beliefs: [", terminator: "")
        for (i, belief) in currentBeliefs.enumerated() {
            print(String(format: "%.3f", belief), terminator: i < currentBeliefs.count - 1 ? ", " : "")
        }
        print("]")
        print("Average free energy: \(String(format: "%.4f", stats["averageFreeEnergy"] as! Double))")
        print("Belief entropy: \(String(format: "%.4f", stats["beliefEntropy"] as! Double))")
    }
}

// MARK: - Demonstration

struct ActiveInferenceDemo {
    static func run() {
        print("🧠 Active Inference Swift Implementation")
        print("=======================================")
        print()

        // Create agent
        let config = AgentConfig(nStates: 3, nObservations: 3, nActions: 2)
        let agent = ActiveInferenceAgent(config: config)

        print("Creating agent with \(config.nStates) states, \(config.nObservations) observations, \(config.nActions) actions...")
        print()

        // Print initial beliefs
        let initialBeliefs = agent.getBeliefs()
        print("Initial beliefs: [", terminator: "")
        for (i, belief) in initialBeliefs.enumerated() {
            print(String(format: "%.3f", belief), terminator: i < initialBeliefs.count - 1 ? ", " : "")
        }
        print("]")
        print()

        // Run simulation
        let nSteps = 10
        print("Running simulation for \(nSteps) steps...")
        print()

        for step in 1...nSteps {
            // Generate random observation
            let observation = Int.random(in: 0..<config.nObservations)

            print("Step \(step):")
            print("  Observation: \(observation)")

            // Execute perception-action cycle
            let (action, freeEnergy) = agent.step(observation: observation)

            print("  Selected action: \(action)")

            // Print current beliefs
            let currentBeliefs = agent.getBeliefs()
            print("  Updated beliefs: [", terminator: "")
            for (i, belief) in currentBeliefs.enumerated() {
                print(String(format: "%.3f", belief), terminator: i < currentBeliefs.count - 1 ? ", " : "")
            }
            print("]")
            print("  Free energy: \(String(format: "%.4f", freeEnergy))")
            print()
        }

        // Print final statistics
        print()
        agent.printStatistics()

        print()
        print("✅ Swift Active Inference simulation completed!")
    }

    static func runMultiAgentDemo() {
        print()
        print("🐜 Multi-Agent Swift Demo")
        print("=========================")
        print()

        let nAgents = 3
        let agents = (0..<nAgents).map { _ in ActiveInferenceAgent() }

        // Run multi-agent simulation
        for step in 1...5 {
            print("Multi-agent Step \(step):")

            for (i, agent) in agents.enumerated() {
                let observation = Int.random(in: 0..<3)
                let (action, _) = agent.step(observation: observation)

                let beliefs = agent.getBeliefs()
                let maxBelief = beliefs.max() ?? 0.0

                print(String(format: "  Agent \(i + 1): Obs=\(observation), Action=\(action), Best Belief=%.3f", maxBelief))
            }
            print()
        }

        print("✅ Multi-agent simulation completed!")
    }
}

// MARK: - Main Execution

// Run demo if this file is executed directly
ActiveInferenceDemo.run()
ActiveInferenceDemo.runMultiAgentDemo()
