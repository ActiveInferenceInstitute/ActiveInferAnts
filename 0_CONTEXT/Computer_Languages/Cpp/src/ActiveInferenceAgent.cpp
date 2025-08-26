#include "ActiveInferenceAgent.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <random>
#include <cmath>
#include <sstream>

// Implementation starts here

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
    // Initialize A matrix (observation likelihood p(o|s))
    A = SimpleMatrix(config.nObservations, config.nStates);

    // Simple diagonal structure with some noise
    for (size_t o = 0; o < static_cast<size_t>(config.nObservations); ++o) {
        for (size_t s = 0; s < static_cast<size_t>(config.nStates); ++s) {
            if (o == s % static_cast<size_t>(config.nObservations)) {
                A(o, s) = 0.8;  // High probability for matching observation
            } else {
                A(o, s) = 0.2 / (static_cast<size_t>(config.nObservations) - 1);  // Low probability for others
            }
        }
    }
}

void ActiveInferenceAgent::initializeTransitionMatrices() {
    // Initialize B matrices (state transition p(s'|s,a))
    B.resize(config.nActions);

    for (int a = 0; a < config.nActions; ++a) {
        B[a] = SimpleMatrix(config.nStates, config.nStates);

        // Simple transition model with action bias
        for (size_t s = 0; s < static_cast<size_t>(config.nStates); ++s) {
            for (size_t s_next = 0; s_next < static_cast<size_t>(config.nStates); ++s_next) {
                if (s_next == (s + a + 1) % config.nStates) {
                    B[a](s_next, s) = 0.7;  // Likely to move forward by action amount
                } else if (s_next == s) {
                    B[a](s_next, s) = 0.2;  // Some probability of staying
                } else {
                    B[a](s_next, s) = 0.1 / (config.nStates - 2);  // Low probability for others
                }
            }
        }
    }
}

void ActiveInferenceAgent::initializePreferenceVector() {
    // Initialize C vector (observation preferences)
    C = SimpleVector(config.nObservations);

    // Prefer first observation type
    for (size_t i = 0; i < static_cast<size_t>(config.nObservations); ++i) {
        C(i) = (i == 0) ? 0.0 : 0.5;  // Lower energy for preferred observations
    }
}

void ActiveInferenceAgent::initializePriorVector() {
    // Initialize D vector (prior beliefs p(s))
    D = SimpleVector(config.nStates);

    // Uniform prior
    double uniform_prob = 1.0 / config.nStates;
    for (size_t i = 0; i < static_cast<size_t>(config.nStates); ++i) {
        D(i) = uniform_prob;
    }
}

void ActiveInferenceAgent::initializeBeliefState() {
    // Initialize current beliefs to prior
    currentBeliefs = SimpleVector(config.nStates);
    for (size_t i = 0; i < static_cast<size_t>(config.nStates); ++i) {
        currentBeliefs(i) = D(i);
    }
}

SimpleVector ActiveInferenceAgent::updateBeliefs(int observation) {
    // Bayesian belief update: P(s|o) ∝ P(o|s) * P(s)
    SimpleVector likelihood = getObservationLikelihood(observation);
    SimpleVector posterior(config.nStates);

    for (size_t i = 0; i < config.nStates; ++i) {
        posterior(i) = likelihood(i) * currentBeliefs(i);
    }

    // Normalize
    currentBeliefs = normalizeVector(posterior);
    return currentBeliefs;
}

FreeEnergy ActiveInferenceAgent::calculateExpectedFreeEnergy(int action) const {
    FreeEnergy fe;
    SimpleVector predictedBeliefs = predictBeliefs(action);

    // Calculate pragmatic value (expected utility)
    fe.pragmatic = calculatePragmaticValue(predictedBeliefs);

    // Calculate epistemic value (information gain)
    fe.epistemic = calculateEpistemicValue(predictedBeliefs);

    // Expected free energy is negative pragmatic + epistemic terms
    fe.expected = -fe.pragmatic + fe.epistemic;

    return fe;
}

int ActiveInferenceAgent::selectAction() {
    int bestAction = 0;
    double minEFE = std::numeric_limits<double>::max();

    for (int action = 0; action < config.nActions; ++action) {
        FreeEnergy fe = calculateExpectedFreeEnergy(action);
        if (fe.expected < minEFE) {
            minEFE = fe.expected;
            bestAction = action;
        }
    }

    return bestAction;
}

int ActiveInferenceAgent::step(int observation) {
    updateBeliefs(observation);
    int action = selectAction();
    recordHistory(action, observation);
    return action;
}

SimpleVector ActiveInferenceAgent::getObservationLikelihood(int observation) const {
    SimpleVector likelihood(config.nStates);
    for (size_t i = 0; i < config.nStates; ++i) {
        likelihood(i) = A(observation, i);
    }
    return likelihood;
}

SimpleVector ActiveInferenceAgent::predictBeliefs(int action) const {
    SimpleVector predicted(config.nStates, 0.0);

    for (size_t s_next = 0; s_next < config.nStates; ++s_next) {
        for (size_t s = 0; s < config.nStates; ++s) {
            predicted(s_next) += B[action](s_next, s) * currentBeliefs(s);
        }
    }

    return predicted;
}

double ActiveInferenceAgent::calculatePragmaticValue(const SimpleVector& predictedBeliefs) const {
    double pragmatic = 0.0;
    for (size_t i = 0; i < config.nObservations; ++i) {
        double expectedObs = 0.0;
        for (size_t j = 0; j < config.nStates; ++j) {
            expectedObs += A(i, j) * predictedBeliefs(j);
        }
        pragmatic += expectedObs * C(i);
    }
    return pragmatic;
}

double ActiveInferenceAgent::calculateEpistemicValue(const SimpleVector& predictedBeliefs) const {
    double epistemic = 0.0;
    for (size_t i = 0; i < config.nStates; ++i) {
        if (predictedBeliefs(i) > 0.0) {
            epistemic -= predictedBeliefs(i) * std::log(predictedBeliefs(i));
        }
    }
    return config.uncertaintyWeight * epistemic;
}

double ActiveInferenceAgent::calculateEntropy(const SimpleVector& beliefs) const {
    double entropy = 0.0;
    for (size_t i = 0; i < beliefs.size(); ++i) {
        if (beliefs(i) > 0.0) {
            entropy -= beliefs(i) * std::log(beliefs(i));
        }
    }
    return entropy;
}

double ActiveInferenceAgent::calculateVariationalFreeEnergy() const {
    double fe = 0.0;

    // Calculate expected free energy under current beliefs
    for (int action = 0; action < config.nActions; ++action) {
        FreeEnergy action_fe = calculateExpectedFreeEnergy(action);
        fe += action_fe.expected;
    }

    fe /= config.nActions;
    return fe;
}

void ActiveInferenceAgent::reset() {
    initializeGenerativeModel();
    initializeBeliefState();
    history.clear();
}

void ActiveInferenceAgent::log(const std::string& message) const {
    if (config.verbose) {
        std::cout << "[LOG] " << message << std::endl;
    }
}

void ActiveInferenceAgent::recordHistory(int action, int observation) {
    history.beliefs.push_back(currentBeliefs);
    history.actions.push_back(action);
    history.observations.push_back(observation);
    history.freeEnergy.push_back(calculateVariationalFreeEnergy());
    history.timestamps.push_back(std::chrono::system_clock::now());
}

std::string ActiveInferenceAgent::getStatisticsString() const {
    std::stringstream ss;
    ss << "Active Inference Agent Statistics:\n";
    ss << "States: " << config.nStates << "\n";
    ss << "Observations: " << config.nObservations << "\n";
    ss << "Actions: " << config.nActions << "\n";
    ss << "Total steps: " << history.size() << "\n";

    if (!history.beliefs.empty()) {
        ss << "Final beliefs: [";
        for (size_t i = 0; i < currentBeliefs.size(); ++i) {
            ss << std::fixed << std::setprecision(3) << currentBeliefs(i);
            if (i < currentBeliefs.size() - 1) ss << ", ";
        }
        ss << "]\n";
    }

    return ss.str();
}

// End of implementation
