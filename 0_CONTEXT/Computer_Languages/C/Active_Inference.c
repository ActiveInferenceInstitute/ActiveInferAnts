#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

// Active Inference Agent structure
typedef struct {
    int n_states;
    int n_observations;
    int n_actions;
    double* beliefs;           // Current beliefs P(s)
    double* prior_beliefs;     // Prior beliefs D
    double** a_matrix;         // Likelihood P(o|s)
    double*** b_matrix;        // Transition P(s'|s,a)
    double* c_vector;          // Preferences P(o)
    double precision;          // Precision parameter
    double learning_rate;      // Learning rate
} ActiveInferenceAgent;

// Function prototypes
ActiveInferenceAgent* create_agent(int n_states, int n_observations, int n_actions);
void free_agent(ActiveInferenceAgent* agent);
void initialize_matrices(ActiveInferenceAgent* agent);
void update_beliefs(ActiveInferenceAgent* agent, int observation);
int select_action(ActiveInferenceAgent* agent);
double calculate_free_energy(ActiveInferenceAgent* agent);
void print_beliefs(ActiveInferenceAgent* agent);
double random_uniform();

// Create a new Active Inference Agent
ActiveInferenceAgent* create_agent(int n_states, int n_observations, int n_actions) {
    ActiveInferenceAgent* agent = (ActiveInferenceAgent*)malloc(sizeof(ActiveInferenceAgent));

    agent->n_states = n_states;
    agent->n_observations = n_observations;
    agent->n_actions = n_actions;
    agent->precision = 1.0;
    agent->learning_rate = 0.1;

    // Allocate memory for beliefs
    agent->beliefs = (double*)malloc(n_states * sizeof(double));
    agent->prior_beliefs = (double*)malloc(n_states * sizeof(double));

    // Allocate memory for matrices
    agent->a_matrix = (double**)malloc(n_observations * sizeof(double*));
    for (int i = 0; i < n_observations; i++) {
        agent->a_matrix[i] = (double*)malloc(n_states * sizeof(double));
    }

    agent->b_matrix = (double***)malloc(n_actions * sizeof(double**));
    for (int a = 0; a < n_actions; a++) {
        agent->b_matrix[a] = (double**)malloc(n_states * sizeof(double*));
        for (int s = 0; s < n_states; s++) {
            agent->b_matrix[a][s] = (double*)malloc(n_states * sizeof(double));
        }
    }

    agent->c_vector = (double*)malloc(n_observations * sizeof(double));

    initialize_matrices(agent);

    return agent;
}

// Free memory allocated for the agent
void free_agent(ActiveInferenceAgent* agent) {
    free(agent->beliefs);
    free(agent->prior_beliefs);

    for (int i = 0; i < agent->n_observations; i++) {
        free(agent->a_matrix[i]);
    }
    free(agent->a_matrix);

    for (int a = 0; a < agent->n_actions; a++) {
        for (int s = 0; s < agent->n_states; s++) {
            free(agent->b_matrix[a][s]);
        }
        free(agent->b_matrix[a]);
    }
    free(agent->b_matrix);

    free(agent->c_vector);
    free(agent);
}

// Initialize matrices with reasonable values
void initialize_matrices(ActiveInferenceAgent* agent) {
    // Initialize uniform prior beliefs
    double uniform_prob = 1.0 / agent->n_states;
    for (int i = 0; i < agent->n_states; i++) {
        agent->prior_beliefs[i] = uniform_prob;
        agent->beliefs[i] = uniform_prob;
    }

    // Initialize A matrix (observation likelihood)
    // Diagonal structure with some noise
    for (int o = 0; o < agent->n_observations; o++) {
        for (int s = 0; s < agent->n_states; s++) {
            if (o == s % agent->n_observations) {
                agent->a_matrix[o][s] = 0.8;  // High probability for matching observation
            } else {
                agent->a_matrix[o][s] = 0.2 / (agent->n_observations - 1);  // Low probability for others
            }
        }
    }

    // Initialize B matrix (state transitions)
    for (int a = 0; a < agent->n_actions; a++) {
        for (int s = 0; s < agent->n_states; s++) {
            for (int s_next = 0; s_next < agent->n_states; s_next++) {
                // Action-specific transition patterns
                if (s_next == (s + a + 1) % agent->n_states) {
                    agent->b_matrix[a][s][s_next] = 0.7;  // Likely to move forward by action amount
                } else if (s_next == s) {
                    agent->b_matrix[a][s][s_next] = 0.2;  // Some probability of staying
                } else {
                    agent->b_matrix[a][s][s_next] = 0.1 / (agent->n_states - 2);  // Low probability for others
                }
            }
        }
    }

    // Initialize C vector (observation preferences)
    for (int o = 0; o < agent->n_observations; o++) {
        agent->c_vector[o] = (o == 0) ? 0.0 : 0.5;  // Lower energy for preferred observations
    }
}

// Update beliefs based on observation using Bayesian inference
void update_beliefs(ActiveInferenceAgent* agent, int observation) {
    double* likelihood = agent->a_matrix[observation];
    double posterior[agent->n_states];

    // Compute posterior: P(s|o) ∝ P(o|s) * P(s)
    for (int s = 0; s < agent->n_states; s++) {
        posterior[s] = likelihood[s] * agent->beliefs[s];
    }

    // Normalize posterior
    double sum = 0.0;
    for (int s = 0; s < agent->n_states; s++) {
        sum += posterior[s];
    }

    if (sum > 0.0) {
        for (int s = 0; s < agent->n_states; s++) {
            agent->beliefs[s] = posterior[s] / sum;
        }
    }
}

// Select action using expected free energy minimization
int select_action(ActiveInferenceAgent* agent) {
    int best_action = 0;
    double min_efe = INFINITY;

    for (int action = 0; action < agent->n_actions; action++) {
        // Predict beliefs after action
        double predicted_beliefs[agent->n_states];

        for (int s_next = 0; s_next < agent->n_states; s_next++) {
            predicted_beliefs[s_next] = 0.0;
            for (int s = 0; s < agent->n_states; s++) {
                predicted_beliefs[s_next] += agent->b_matrix[action][s][s_next] * agent->beliefs[s];
            }
        }

        // Calculate expected free energy
        double efe = 0.0;
        for (int s = 0; s < agent->n_states; s++) {
            if (predicted_beliefs[s] > 0.0) {
                efe -= predicted_beliefs[s] * log(predicted_beliefs[s] / agent->prior_beliefs[s]);
            }
        }

        if (efe < min_efe) {
            min_efe = efe;
            best_action = action;
        }
    }

    return best_action;
}

// Calculate variational free energy
double calculate_free_energy(ActiveInferenceAgent* agent) {
    double fe = 0.0;

    for (int s = 0; s < agent->n_states; s++) {
        if (agent->beliefs[s] > 0.0) {
            fe += agent->beliefs[s] * log(agent->beliefs[s] / agent->prior_beliefs[s]);
        }
    }

    return fe;
}

// Print current beliefs
void print_beliefs(ActiveInferenceAgent* agent) {
    printf("Beliefs: [");
    for (int i = 0; i < agent->n_states; i++) {
        printf("%.3f", agent->beliefs[i]);
        if (i < agent->n_states - 1) printf(", ");
    }
    printf("]\n");
}

// Generate random number between 0 and 1
double random_uniform() {
    return (double)rand() / RAND_MAX;
}

// Main simulation function
int main() {
    srand(time(NULL));

    printf("🧠 Active Inference C Implementation\n");
    printf("===================================\n\n");

    // Create agent
    int n_states = 3, n_observations = 3, n_actions = 3;
    ActiveInferenceAgent* agent = create_agent(n_states, n_observations, n_actions);

    printf("Initial beliefs: ");
    print_beliefs(agent);

    // Run simulation
    for (int step = 0; step < 10; step++) {
        // Generate random observation
        int observation = rand() % n_observations;

        printf("\nStep %d:\n", step + 1);
        printf("  Observation: %d\n", observation);

        // Update beliefs
        update_beliefs(agent, observation);
        printf("  Updated beliefs: ");
        print_beliefs(agent);

        // Select action
        int action = select_action(agent);
        printf("  Selected action: %d\n", action);

        // Calculate free energy
        double fe = calculate_free_energy(agent);
        printf("  Free energy: %.3f\n", fe);
    }

    printf("\n✅ C Active Inference simulation completed successfully!\n");

    // Clean up
    free_agent(agent);

    return 0;
}
