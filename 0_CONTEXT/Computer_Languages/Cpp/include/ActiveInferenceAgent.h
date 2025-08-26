#pragma once

#include <Eigen/Dense>
#include <vector>
#include <memory>
#include <random>
#include <chrono>

/**
 * @brief Configuration structure for Active Inference Agent
 */
struct AgentConfig {
    int nStates = 3;           ///< Number of hidden states
    int nObservations = 3;     ///< Number of observation types
    int nActions = 3;          ///< Number of possible actions
    double learningRate = 0.1;  ///< Learning rate for belief updates
    double uncertaintyWeight = 0.1; ///< Weight for epistemic value
    double precision = 1.0;     ///< Precision parameter
    bool verbose = false;       ///< Enable verbose logging

    /**
     * @brief Validate configuration parameters
     * @throws std::invalid_argument if parameters are invalid
     */
    void validate() const;
};

/**
 * @brief Free energy components structure
 */
struct FreeEnergy {
    double variational = 0.0;   ///< Variational free energy
    double expected = 0.0;      ///< Expected free energy
    double pragmatic = 0.0;     ///< Pragmatic value
    double epistemic = 0.0;     ///< Epistemic value

    /**
     * @brief Reset all values to zero
     */
    void reset() {
        variational = expected = pragmatic = epistemic = 0.0;
    }
};

/**
 * @brief Agent history for analysis
 */
struct AgentHistory {
    std::vector<Eigen::VectorXd> beliefs;      ///< Belief history
    std::vector<int> actions;                  ///< Action history
    std::vector<int> observations;             ///< Observation history
    std::vector<double> freeEnergy;            ///< Free energy history
    std::vector<std::chrono::system_clock::time_point> timestamps; ///< Timestamps

    /**
     * @brief Clear all history
     */
    void clear() {
        beliefs.clear();
        actions.clear();
        observations.clear();
        freeEnergy.clear();
        timestamps.clear();
    }

    /**
     * @brief Get total number of steps
     */
    size_t size() const { return actions.size(); }
};

/**
 * @brief Custom exception for Active Inference errors
 */
class ActiveInferenceError : public std::runtime_error {
public:
    explicit ActiveInferenceError(const std::string& message)
        : std::runtime_error(message) {}
};

/**
 * @brief Belief update error
 */
class BeliefUpdateError : public ActiveInferenceError {
public:
    explicit BeliefUpdateError(const std::string& message)
        : ActiveInferenceError("Belief Update Error: " + message) {}
};

/**
 * @brief Policy selection error
 */
class PolicySelectionError : public ActiveInferenceError {
public:
    explicit PolicySelectionError(const std::string& message)
        : ActiveInferenceError("Policy Selection Error: " + message) {}
};

/**
 * @brief Active Inference Agent implementation
 *
 * This class implements the core active inference algorithm using C++
 * with Eigen for efficient matrix operations and comprehensive error handling.
 */
class ActiveInferenceAgent {
public:
    /**
     * @brief Construct a new Active Inference Agent
     * @param config Agent configuration
     * @throws std::invalid_argument if configuration is invalid
     */
    explicit ActiveInferenceAgent(const AgentConfig& config);

    /**
     * @brief Default constructor with default configuration
     */
    ActiveInferenceAgent();

    /**
     * @brief Update beliefs given an observation
     * @param observation The observation index
     * @return Updated belief vector
     * @throws BeliefUpdateError if update fails
     */
    Eigen::VectorXd updateBeliefs(int observation);

    /**
     * @brief Calculate variational free energy
     * @return Current variational free energy
     */
    double calculateVariationalFreeEnergy() const;

    /**
     * @brief Calculate expected free energy for a given action
     * @param action The action index
     * @return Free energy components
     * @throws PolicySelectionError if calculation fails
     */
    FreeEnergy calculateExpectedFreeEnergy(int action) const;

    /**
     * @brief Select the best action by minimizing expected free energy
     * @return Selected action index
     * @throws PolicySelectionError if selection fails
     */
    int selectAction();

    /**
     * @brief Execute one step of the perception-action loop
     * @param observation The current observation
     * @return Selected action
     */
    int step(int observation);

    /**
     * @brief Get current belief state
     */
    Eigen::VectorXd getBeliefs() const { return currentBeliefs; }

    /**
     * @brief Get agent configuration
     */
    const AgentConfig& getConfig() const { return config; }

    /**
     * @brief Get generative model matrices
     */
    const Eigen::MatrixXd& getA() const { return A; }  // Likelihood
    const std::vector<Eigen::MatrixXd>& getB() const { return B; }  // Transition
    const Eigen::VectorXd& getC() const { return C; }  // Preferences
    const Eigen::VectorXd& getD() const { return D; }  // Prior

    /**
     * @brief Get agent history
     */
    const AgentHistory& getHistory() const { return history; }

    /**
     * @brief Get statistics about agent behavior
     */
    std::unordered_map<std::string, double> getStatistics() const;

    /**
     * @brief Reset agent to initial state
     */
    void reset();

    /**
     * @brief Enable or disable verbose logging
     */
    void setVerbose(bool verbose) { config.verbose = verbose; }

private:
    AgentConfig config;                    ///< Agent configuration
    Eigen::MatrixXd A;                     ///< Likelihood matrix p(o|s)
    std::vector<Eigen::MatrixXd> B;        ///< Transition matrices p(s'|s,a)
    Eigen::VectorXd C;                     ///< Preferences p(o)
    Eigen::VectorXd D;                     ///< Prior beliefs p(s)

    Eigen::VectorXd currentBeliefs;        ///< Current belief state
    AgentHistory history;                  ///< Agent behavior history
    std::mt19937 rng;                      ///< Random number generator

    /**
     * @brief Initialize the generative model
     */
    void initializeGenerativeModel();

    /**
     * @brief Initialize likelihood matrix A
     */
    void initializeLikelihoodMatrix();

    /**
     * @brief Initialize transition matrices B
     */
    void initializeTransitionMatrices();

    /**
     * @brief Initialize preference vector C
     */
    void initializePreferenceVector();

    /**
     * @brief Initialize prior belief vector D
     */
    void initializePriorVector();

    /**
     * @brief Initialize belief state
     */
    void initializeBeliefState();

    /**
     * @brief Get likelihood vector for an observation
     */
    Eigen::VectorXd getObservationLikelihood(int observation) const;

    /**
     * @brief Predict beliefs after taking an action
     */
    Eigen::VectorXd predictBeliefs(int action) const;

    /**
     * @brief Calculate pragmatic value
     */
    double calculatePragmaticValue(const Eigen::VectorXd& predictedBeliefs) const;

    /**
     * @brief Calculate epistemic value
     */
    double calculateEpistemicValue(const Eigen::VectorXd& predictedBeliefs) const;

    /**
     * @brief Calculate Shannon entropy of belief distribution
     */
    double calculateEntropy(const Eigen::VectorXd& beliefs) const;

    /**
     * @brief Calculate expected likelihood
     */
    double calculateExpectedLikelihood() const;

    /**
     * @brief Log message if verbose mode is enabled
     */
    void log(const std::string& message) const;

    /**
     * @brief Add current state to history
     */
    void recordHistory(int action, int observation);
};

// Template specializations for common operations
template<typename Derived>
bool isProbabilityVector(const Eigen::DenseBase<Derived>& vec, double tolerance = 1e-6) {
    if (vec.minCoeff() < -tolerance) return false;
    return std::abs(vec.sum() - 1.0) < tolerance;
}

template<typename Derived>
Eigen::Matrix<typename Derived::Scalar, Derived::RowsAtCompileTime, 1>
normalizeVector(const Eigen::DenseBase<Derived>& vec) {
    auto normalized = vec;
    return normalized / normalized.sum();
}
