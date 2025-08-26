#pragma once

#include <vector>
#include <memory>
#include <random>
#include <chrono>
#include <cmath>
#include <iostream>
#include <algorithm>

// Optional Eigen support
#ifdef USE_EIGEN
#include <Eigen/Dense>
#endif

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
    void validate() const {
        if (nStates <= 0) throw std::invalid_argument("Number of states must be positive");
        if (nObservations <= 0) throw std::invalid_argument("Number of observations must be positive");
        if (nActions <= 0) throw std::invalid_argument("Number of actions must be positive");
        if (learningRate <= 0 || learningRate > 1) throw std::invalid_argument("Learning rate must be in (0, 1]");
        if (uncertaintyWeight < 0) throw std::invalid_argument("Uncertainty weight must be non-negative");
        if (precision <= 0) throw std::invalid_argument("Precision must be positive");
    }
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
 * @brief Simple matrix class using std::vector
 */
class SimpleMatrix {
private:
    std::vector<double> data;
    size_t rows, cols;

public:
    SimpleMatrix(size_t r = 0, size_t c = 0, double init = 0.0)
        : rows(r), cols(c), data(r * c, init) {}

    double& operator()(size_t i, size_t j) { return data[i * cols + j]; }
    double operator()(size_t i, size_t j) const { return data[i * cols + j]; }

    size_t numRows() const { return rows; }
    size_t numCols() const { return cols; }

    void fill(double value) {
        std::fill(data.begin(), data.end(), value);
    }
};

/**
 * @brief Simple vector class using std::vector
 */
class SimpleVector {
private:
    std::vector<double> data;

public:
    SimpleVector(size_t n = 0, double init = 0.0) : data(n, init) {}

    double& operator()(size_t i) { return data[i]; }
    double operator()(size_t i) const { return data[i]; }
    size_t size() const { return data.size(); }

    void normalize() {
        double sum = 0.0;
        for (double val : data) sum += val;
        if (sum > 0.0) {
            for (double& val : data) val /= sum;
        }
    }

    double sum() const {
        double total = 0.0;
        for (double val : data) total += val;
        return total;
    }

    double dot(const SimpleVector& other) const {
        double result = 0.0;
        for (size_t i = 0; i < std::min(size(), other.size()); ++i) {
            result += data[i] * other.data[i];
        }
        return result;
    }
};

/**
 * @brief Agent history for analysis
 */
struct AgentHistory {
    std::vector<SimpleVector> beliefs;         ///< Belief history
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
    SimpleVector updateBeliefs(int observation);

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
    SimpleVector getBeliefs() const { return currentBeliefs; }

    /**
     * @brief Get agent configuration
     */
    const AgentConfig& getConfig() const { return config; }

    /**
     * @brief Get generative model matrices
     */
    const SimpleMatrix& getA() const { return A; }  // Likelihood
    const std::vector<SimpleMatrix>& getB() const { return B; }  // Transition
    const SimpleVector& getC() const { return C; }  // Preferences
    const SimpleVector& getD() const { return D; }  // Prior

    /**
     * @brief Get agent history
     */
    const AgentHistory& getHistory() const { return history; }

    /**
     * @brief Get comprehensive statistics as string
     */
    std::string getStatisticsString() const;

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
    SimpleMatrix A;                        ///< Likelihood matrix p(o|s)
    std::vector<SimpleMatrix> B;           ///< Transition matrices p(s'|s,a)
    SimpleVector C;                        ///< Preferences p(o)
    SimpleVector D;                        ///< Prior beliefs p(s)

    SimpleVector currentBeliefs;           ///< Current belief state
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
    SimpleVector getObservationLikelihood(int observation) const;

    /**
     * @brief Predict beliefs after taking an action
     */
    SimpleVector predictBeliefs(int action) const;

    /**
     * @brief Calculate pragmatic value
     */
    double calculatePragmaticValue(const SimpleVector& predictedBeliefs) const;

    /**
     * @brief Calculate epistemic value
     */
    double calculateEpistemicValue(const SimpleVector& predictedBeliefs) const;

    /**
     * @brief Calculate Shannon entropy of belief distribution
     */
    double calculateEntropy(const SimpleVector& beliefs) const;

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

// Utility functions for SimpleVector operations
inline bool isProbabilityVector(const SimpleVector& vec, double tolerance = 1e-6) {
    for (size_t i = 0; i < vec.size(); ++i) {
        if (vec(i) < -tolerance) return false;
    }
    return std::abs(vec.sum() - 1.0) < tolerance;
}

inline SimpleVector normalizeVector(const SimpleVector& vec) {
    SimpleVector normalized = vec;
    double sum = vec.sum();
    if (sum > 0.0) {
        for (size_t i = 0; i < normalized.size(); ++i) {
            normalized(i) /= sum;
        }
    }
    return normalized;
}
