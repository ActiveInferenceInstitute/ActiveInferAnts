#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define NUM_AGENTS 5
#define NUM_STATES 3
#define NUM_ACTIONS 2
#define NUM_OBSERVATIONS 2

// Agent structure
typedef struct {
    double beliefs[NUM_STATES];
    double transition_model[NUM_STATES][NUM_ACTIONS][NUM_STATES];
    double observation_model[NUM_STATES][NUM_OBSERVATIONS];
    double action_prior[NUM_ACTIONS];
} Agent;

// Function prototypes
void initialize_agent(Agent *agent);
int select_action(Agent *agent);
void update_beliefs(Agent *agent, int action, int observation);
int get_observation(int true_state);
void simulate_step(Agent *agents, int *true_states);

// Main simulation loop
int main() {
    srand(time(NULL));
    
    Agent agents[NUM_AGENTS];
    int true_states[NUM_AGENTS];
    
    // Initialize agents and true states
    for (int i = 0; i < NUM_AGENTS; i++) {
        initialize_agent(&agents[i]);
        true_states[i] = rand() % NUM_STATES;
    }
    
    // Run simulation for 100 steps
    for (int step = 0; step < 100; step++) {
        printf("Step %d:\n", step);
        simulate_step(agents, true_states);
        printf("\n");
    }
    
    return 0;
}

// Initialize agent with random beliefs and models
void initialize_agent(Agent *agent) {
    // Initialize beliefs
    double sum = 0;
    for (int i = 0; i < NUM_STATES; i++) {
        agent->beliefs[i] = (double)rand() / RAND_MAX;
        sum += agent->beliefs[i];
    }
    for (int i = 0; i < NUM_STATES; i++) {
        agent->beliefs[i] /= sum;
    }
    
    // Initialize transition model
    for (int s = 0; s < NUM_STATES; s++) {
        for (int a = 0; a < NUM_ACTIONS; a++) {
            sum = 0;
            for (int s_next = 0; s_next < NUM_STATES; s_next++) {
                agent->transition_model[s][a][s_next] = (double)rand() / RAND_MAX;
                sum += agent->transition_model[s][a][s_next];
            }
            for (int s_next = 0; s_next < NUM_STATES; s_next++) {
                agent->transition_model[s][a][s_next] /= sum;
            }
        }
    }
    
    // Initialize observation model
    for (int s = 0; s < NUM_STATES; s++) {
        sum = 0;
        for (int o = 0; o < NUM_OBSERVATIONS; o++) {
            agent->observation_model[s][o] = (double)rand() / RAND_MAX;
            sum += agent->observation_model[s][o];
        }
        for (int o = 0; o < NUM_OBSERVATIONS; o++) {
            agent->observation_model[s][o] /= sum;
        }
    }
    
    // Initialize action prior
    sum = 0;
    for (int a = 0; a < NUM_ACTIONS; a++) {
        agent->action_prior[a] = (double)rand() / RAND_MAX;
        sum += agent->action_prior[a];
    }
    for (int a = 0; a < NUM_ACTIONS; a++) {
        agent->action_prior[a] /= sum;
    }
}

// Select action based on current beliefs
int select_action(Agent *agent) {
    double expected_free_energy[NUM_ACTIONS] = {0};
    
    for (int a = 0; a < NUM_ACTIONS; a++) {
        for (int s_next = 0; s_next < NUM_STATES; s_next++) {
            double transition_prob = 0;
            for (int s = 0; s < NUM_STATES; s++) {
                transition_prob += agent->beliefs[s] * agent->transition_model[s][a][s_next];
            }
            
            double kl_divergence = 0;
            for (int o = 0; o < NUM_OBSERVATIONS; o++) {
                double p_o = 0;
                for (int s = 0; s < NUM_STATES; s++) {
                    p_o += agent->observation_model[s][o] * transition_prob;
                }
                if (p_o > 0) {
                    kl_divergence += p_o * log(p_o / agent->observation_model[s_next][o]);
                }
            }
            
            expected_free_energy[a] += transition_prob * (kl_divergence - log(agent->action_prior[a]));
        }
    }
    
    // Select action with lowest expected free energy
    int best_action = 0;
    for (int a = 1; a < NUM_ACTIONS; a++) {
        if (expected_free_energy[a] < expected_free_energy[best_action]) {
            best_action = a;
        }
    }
    
    return best_action;
}

// Update agent's beliefs based on action and observation
void update_beliefs(Agent *agent, int action, int observation) {
    double new_beliefs[NUM_STATES] = {0};
    
    for (int s_next = 0; s_next < NUM_STATES; s_next++) {
        double transition_prob = 0;
        for (int s = 0; s < NUM_STATES; s++) {
            transition_prob += agent->beliefs[s] * agent->transition_model[s][action][s_next];
        }
        new_beliefs[s_next] = transition_prob * agent->observation_model[s_next][observation];
    }
    
    // Normalize new beliefs
    double sum = 0;
    for (int s = 0; s < NUM_STATES; s++) {
        sum += new_beliefs[s];
    }
    for (int s = 0; s < NUM_STATES; s++) {
        agent->beliefs[s] = new_beliefs[s] / sum;
    }
}

// Get observation based on true state
int get_observation(int true_state) {
    // Simplified observation model: 70% chance of correct observation
    return (rand() % 100 < 70) ? true_state % NUM_OBSERVATIONS : (true_state + 1) % NUM_OBSERVATIONS;
}

// Simulate one step for all agents
void simulate_step(Agent *agents, int *true_states) {
    for (int i = 0; i < NUM_AGENTS; i++) {
        int action = select_action(&agents[i]);
        int observation = get_observation(true_states[i]);
        
        update_beliefs(&agents[i], action, observation);
        
        // Update true state (simplified environment dynamics)
        true_states[i] = (true_states[i] + action) % NUM_STATES;
        
        printf("Agent %d: Action %d, Observation %d, True State %d\n", i, action, observation, true_states[i]);
    }
}