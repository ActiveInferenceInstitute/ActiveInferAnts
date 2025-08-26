#include "ActiveInferenceAgent.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <numeric>

// AgentConfig validation
void AgentConfig::validate() const {
    if (nStates <= 0) {
        throw std::invalid_argument("Number of states must be positive");
    }
    if (nObservations <= 0) {
        throw std::invalid_argument("Number of observations must be positive");
    }
    if (nActions <= 0) {
        throw std::invalid_argument("Number of actions must be positive");
    }
    if (learningRate <= 0.0 || learningRate > 1.0) {
        throw std::invalid_argument("Learning rate must be in (0, 1]");
    }
    if (uncertaintyWeight < 0.0) {
        throw std::invalid_argument("Uncertainty weight must be non-negative");
    }
    if (precision <= 0.0) {
        throw std::invalid_argument("Precision must be positive");
    }
}

// ActiveInferenceAgent implementation
ActiveInferenceAgent::ActiveInferenceAgent(const AgentConfig& config)
    : config(config), rng(std::random_device{}()) {
    this->config.validate();
    initializeGenerativeModel();
    initializeBeliefState();
}

ActiveInferenceAgent::ActiveInferenceAgent()
    : ActiveInferenceAgent(AgentConfig{}) {
}

void ActiveInferenceAgent::initializeGenerativeModel() {
    log("Initializing generative model...");

    initializeLikelihoodMatrix();
    initializeTransitionMatrices();
    initializePreferenceVector();
    initializePriorVector();

    log("Generative model initialized successfully");
}

void ActiveInferenceAgent::initializeLikelihoodMatrix() {
    A = Eigen::MatrixXd(config.nObservations, config.nStates);

    // Initialize with diagonal structure plus noise
    std::uniform_real_distribution<double> dist(-0.1, 0.1);

    for (int obs = 0; obs < config.nObservations; ++obs) {
        for (int state = 0; state < config.nStates; ++state) {
            double baseProb = (obs == state % config.nObservations) ? 0.7 : 0.1;
            double noise = dist(rng);
            A(obs, state) = std::max(0.0, std::min(1.0, baseProb + noise));
        }
        // Normalize row
        double sum = A.row(obs).sum();
        A.row(obs) /= sum;
    }

    log("Likelihood matrix A initialized");
}

void ActiveInferenceAgent::initializeTransitionMatrices() {
    B.resize(config.nActions);

    std::uniform_real_distribution<double> dist(0.05, 0.15);

    for (int action = 0; action < config.nActions; ++action) {
        B[action] = Eigen::MatrixXd(config.nStates, config.nStates);

        for (int fromState = 0; fromState < config.nStates; ++fromState) {
            Eigen::VectorXd row = Eigen::VectorXd::Constant(config.nStates, 0.1);

            // Action-specific transition patterns
            if (action == 0) {
                // Stay/move left
                row(fromState) = 0.6; // Stay
                if (fromState > 0) {
                    row(fromState - 1) = 0.3; // Move left
                }
            } else if (action == 1) {
                // Move right
                if (fromState < config.nStates - 1) {
                    row(fromState + 1) = 0.6; // Move right
                } else {
                    row(fromState) = 0.6; // Stay if at boundary
                }
            } else {
                // Random exploration
                row = Eigen::VectorXd::Constant(config.nStates, 1.0 / config.nStates);
            }

            // Normalize row
            double sum = row.sum();
            row /= sum;

            B[action].row(fromState) = row.transpose();
        }
    }

    log("Transition matrices B initialized");
}

void ActiveInferenceAgent::initializePreferenceVector() {
    C = Eigen::VectorXd(config.nObservations);

    // Prefer certain observations (e.g., food, safety)
    for (int obs = 0; obs < config.nObservations; ++obs) {
        C(obs) = (obs < config.nObservations / 2) ? 1.0 : 0.1;
    }

    log("Preference vector C initialized");
}

void ActiveInferenceAgent::initializePriorVector() {
    D = Eigen::VectorXd::Constant(config.nStates, 1.0 / config.nStates);
    log("Prior vector D initialized");
}

void ActiveInferenceAgent::initializeBeliefState() {
    currentBeliefs = D;
    history.clear();
    log("Belief state initialized");
}

Eigen::VectorXd ActiveInferenceAgent::updateBeliefs(int observation) {
    try {
        if (observation < 0 || observation >= config.nObservations) {
            throw BeliefUpdateError("Invalid observation index: " + std::to_string(observation));
        }

        // Get likelihood for this observation
        Eigen::VectorXd likelihood = getObservationLikelihood(observation);

        // Bayesian update: posterior = prior * likelihood
        Eigen::VectorXd posterior = currentBeliefs.cwiseProduct(likelihood);

        // Normalize
        double sum = posterior.sum();
        if (sum == 0.0) {
            throw BeliefUpdateError("Invalid likelihood - posterior sums to zero");
        }

        currentBeliefs = posterior / sum;

        // Record in history
        history.beliefs.push_back(currentBeliefs);
        history.timestamps.push_back(std::chrono::system_clock::now());

        log("Beliefs updated successfully for observation " + std::to_string(observation));
        return currentBeliefs;

    } catch (const std::exception& e) {
        throw BeliefUpdateError(std::string("Failed to update beliefs: ") + e.what());
    }
}

double ActiveInferenceAgent::calculateVariationalFreeEnergy() const {
    // F = E_q[ln q(s) - ln p(o|s)] = -E_q[ln p(o|s)] + E_q[ln q(s)]
    double expectedLikelihood = calculateExpectedLikelihood();
    double entropy = calculateEntropy(currentBeliefs);

    return -expectedLikelihood - entropy;
}

FreeEnergy ActiveInferenceAgent::calculateExpectedFreeEnergy(int action) const {
    try {
        if (action < 0 || action >= config.nActions) {
            throw PolicySelectionError("Invalid action index: " + std::to_string(action));
        }

        // Predict next beliefs
        Eigen::VectorXd predictedBeliefs = predictBeliefs(action);

        // Calculate pragmatic value (surprise about preferred observations)
        double pragmaticValue = calculatePragmaticValue(predictedBeliefs);

        // Calculate epistemic value (information gain)
        double epistemicValue = calculateEpistemicValue(predictedBeliefs);

        // Total EFE
        double expectedFE = pragmaticValue - config.uncertaintyWeight * epistemicValue;

        FreeEnergy fe;
        fe.variational = calculateVariationalFreeEnergy();
        fe.expected = expectedFE;
        fe.pragmatic = pragmaticValue;
        fe.epistemic = epistemicValue;

        return fe;

    } catch (const std::exception& e) {
        throw PolicySelectionError(std::string("Failed to calculate expected free energy: ") + e.what());
    }
}

int ActiveInferenceAgent::selectAction() {
    try {
        std::vector<FreeEnergy> efes(config.nActions);

        // Calculate EFE for each action
        for (int action = 0; action < config.nActions; ++action) {
            efes[action] = calculateExpectedFreeEnergy(action);
        }

        // Select action with minimum expected free energy
        auto minElement = std::min_element(efes.begin(), efes.end(),
            [](const FreeEnergy& a, const FreeEnergy& b) {
                return a.expected < b.expected;
            });

        int bestAction = std::distance(efes.begin(), minElement);

        log("Action " + std::to_string(bestAction) + " selected");
        return bestAction;

    } catch (const std::exception& e) {
        throw PolicySelectionError(std::string("Failed to select action: ") + e.what());
    }
}

int ActiveInferenceAgent::step(int observation) {
    // Update beliefs based on observation
    updateBeliefs(observation);

    // Calculate free energy
    double fe = calculateVariationalFreeEnergy();
    history.freeEnergy.push_back(fe);

    // Select and return action
    int action = selectAction();
    recordHistory(action, observation);

    return action;
}

Eigen::VectorXd ActiveInferenceAgent::getObservationLikelihood(int observation) const {
    return A.row(observation).transpose();
}

Eigen::VectorXd ActiveInferenceAgent::predictBeliefs(int action) const {
    return currentBeliefs.transpose() * B[action];
}

double ActiveInferenceAgent::calculatePragmaticValue(const Eigen::VectorXd& predictedBeliefs) const {
    double pragmaticValue = 0.0;

    for (int state = 0; state < config.nStates; ++state) {
        double stateProb = predictedBeliefs(state);
        if (stateProb > 0.0) {
            // Expected surprise about preferred observations
            for (int obs = 0; obs < config.nObservations; ++obs) {
                double obsProb = A(obs, state);
                double preference = C(obs);
                pragmaticValue += stateProb * obsProb * preference;
            }
        }
    }

    return pragmaticValue;
}

double ActiveInferenceAgent::calculateEpistemicValue(const Eigen::VectorXd& predictedBeliefs) const {
    return calculateEntropy(predictedBeliefs);
}

double ActiveInferenceAgent::calculateEntropy(const Eigen::VectorXd& beliefs) const {
    double entropy = 0.0;

    for (int i = 0; i < beliefs.size(); ++i) {
        double prob = beliefs(i);
        if (prob > 0.0) {
            entropy -= prob * std::log2(prob);
        }
    }

    return entropy;
}

double ActiveInferenceAgent::calculateExpectedLikelihood() const {
    double expectedLikelihood = 0.0;

    for (int obs = 0; obs < config.nObservations; ++obs) {
        Eigen::VectorXd likelihood = getObservationLikelihood(obs);
        double expectedObsProb = currentBeliefs.dot(likelihood);
        if (expectedObsProb > 0.0) {
            expectedLikelihood += expectedObsProb * std::log(expectedObsProb);
        }
    }

    return expectedLikelihood;
}

std::unordered_map<std::string, double> ActiveInferenceAgent::getStatistics() const {
    std::unordered_map<std::string, double> stats;

    if (history.actions.empty()) {
        stats["message"] = std::numeric_limits<double>::quiet_NaN();
        return stats;
    }

    stats["totalSteps"] = static_cast<double>(history.size());

    // Average free energy
    double avgFE = std::accumulate(history.freeEnergy.begin(), history.freeEnergy.end(), 0.0)
                   / history.freeEnergy.size();
    stats["averageFreeEnergy"] = avgFE;

    // Action distribution
    std::vector<int> actionCounts(config.nActions, 0);
    for (int action : history.actions) {
        if (action >= 0 && action < config.nActions) {
            actionCounts[action]++;
        }
    }

    for (int i = 0; i < config.nActions; ++i) {
        stats["action" + std::to_string(i) + "Count"] = static_cast<double>(actionCounts[i]);
        stats["action" + std::to_string(i) + "Frequency"] =
            static_cast<double>(actionCounts[i]) / history.actions.size();
    }

    // Final beliefs
    for (int i = 0; i < config.nStates; ++i) {
        stats["finalBelief" + std::to_string(i)] = currentBeliefs(i);
    }

    return stats;
}

void ActiveInferenceAgent::reset() {
    currentBeliefs = D;
    history.clear();
    log("Agent reset to initial state");
}

void ActiveInferenceAgent::log(const std::string& message) const {
    if (config.verbose) {
        std::cout << "[ActiveInferenceAgent] " << message << std::endl;
    }
}

void ActiveInferenceAgent::recordHistory(int action, int observation) {
    history.actions.push_back(action);
    history.observations.push_back(observation);
}
