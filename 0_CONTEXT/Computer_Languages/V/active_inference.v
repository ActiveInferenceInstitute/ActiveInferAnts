// Active Inference Implementation in V

module main

import math
import rand

// Active Inference Agent structure
struct ActiveInferenceAgent {
    mut:
        beliefs []f64
        a_matrix [][]f64  // Likelihood P(o|s)
        b_matrix [][][]f64  // Transition P(s'|s,a)
        c_vector []f64    // Preferences P(o)
        d_vector []f64    // Prior beliefs P(s)
        precision f64
        learning_rate f64
        n_states int
        n_observations int
        n_actions int
}

// Create new Active Inference Agent
fn new_active_inference_agent(n_states int, n_observations int, n_actions int) ActiveInferenceAgent {
    mut agent := ActiveInferenceAgent{
        beliefs: []f64{len: n_states}
        a_matrix: [][]f64{len: n_observations, init: []f64{len: n_states}}
        b_matrix: [][][]f64{len: n_actions, init: [][]f64{len: n_states, init: []f64{len: n_states}}}
        c_vector: []f64{len: n_observations}
        d_vector: []f64{len: n_states}
        precision: 1.0
        learning_rate: 0.1
        n_states: n_states
        n_observations: n_observations
        n_actions: n_actions
    }

    agent.initialize_generative_model()
    agent.initialize_beliefs()

    return agent
}

// Initialize the generative model
fn (mut agent ActiveInferenceAgent) initialize_generative_model() {
    // Initialize A matrix (observation likelihood)
    for obs in 0..agent.n_observations {
        for state in 0..agent.n_states {
            // Diagonal structure with noise
            is_diagonal := obs == state % agent.n_observations
            base_prob := if is_diagonal { 0.7 } else { 0.1 }
            noise := (rand.f64() - 0.5) * 0.2
            prob := math.max(0.0, math.min(1.0, base_prob + noise))
            agent.a_matrix[obs][state] = prob
        }
        // Normalize row
        agent.normalize_row(mut agent.a_matrix[obs])
    }

    // Initialize B matrix (state transitions)
    for action in 0..agent.n_actions {
        for from_state in 0..agent.n_states {
            for to_state in 0..agent.n_states {
                // Simple transition model
                if action == 0 {
                    // Stay action
                    agent.b_matrix[action][from_state][to_state] = if to_state == from_state { 0.8 } else { 0.05 }
                } else if action == 1 {
                    // Move action
                    if to_state == (from_state + 1) % agent.n_states {
                        agent.b_matrix[action][from_state][to_state] = 0.7
                    } else {
                        agent.b_matrix[action][from_state][to_state] = 0.05
                    }
                } else {
                    // Random action
                    agent.b_matrix[action][from_state][to_state] = 1.0 / f64(agent.n_states)
                }
            }
            // Normalize row
            agent.normalize_row(mut agent.b_matrix[action][from_state])
        }
    }

    // Initialize C vector (preferences)
    for obs in 0..agent.n_observations {
        agent.c_vector[obs] = if obs < agent.n_observations / 2 { 1.0 } else { 0.1 }
    }

    // Initialize D vector (prior beliefs)
    for state in 0..agent.n_states {
        agent.d_vector[state] = 1.0 / f64(agent.n_states)
    }
}

// Initialize belief state
fn (mut agent ActiveInferenceAgent) initialize_beliefs() {
    for i in 0..agent.n_states {
        agent.beliefs[i] = agent.d_vector[i]
    }
}

// Normalize a vector to sum to 1
fn (agent ActiveInferenceAgent) normalize_row(mut row []f64) {
    mut total := 0.0
    for val in row {
        total += val
    }
    if total > 0.0 {
        for i in 0..row.len {
            row[i] /= total
        }
    }
}

// Update beliefs given observation
fn (mut agent ActiveInferenceAgent) update_beliefs(observation int) {
    likelihood := agent.a_matrix[observation].clone()

    // Bayesian update: posterior = prior * likelihood
    for i in 0..agent.beliefs.len {
        agent.beliefs[i] *= likelihood[i]
    }

    // Normalize
    mut total := 0.0
    for belief in agent.beliefs {
        total += belief
    }
    if total > 0.0 {
        for i in 0..agent.beliefs.len {
            agent.beliefs[i] /= total
        }
    }
}

// Calculate expected free energy for an action
fn (agent ActiveInferenceAgent) calculate_expected_free_energy(action int) f64 {
    // Simplified EFE calculation using entropy
    mut efe := 0.0
    for belief in agent.beliefs {
        if belief > 0.0 {
            efe -= belief * math.log(belief)
        }
    }
    return efe
}

// Select action with minimum expected free energy
fn (agent ActiveInferenceAgent) select_action() int {
    mut min_efe := math.inf(1)
    mut best_action := 0

    for action in 0..agent.n_actions {
        efe := agent.calculate_expected_free_energy(action)
        if efe < min_efe {
            min_efe = efe
            best_action = action
        }
    }

    return best_action
}

// Execute one step of perception-action cycle
fn (mut agent ActiveInferenceAgent) step(observation int) int {
    agent.update_beliefs(observation)
    return agent.select_action()
}

// Print current beliefs
fn (agent ActiveInferenceAgent) print_beliefs() {
    print("Beliefs: [")
    for i, belief in agent.beliefs {
        print("${belief:.3f}")
        if i < agent.beliefs.len - 1 {
            print(", ")
        }
    }
    println("]")
}

// Run simulation
fn run_simulation() {
    println("🧠 V Language Active Inference Demo")
    println("===================================")

    // Create agent
    mut agent := new_active_inference_agent(4, 3, 2)

    // Show initial beliefs
    print("Initial ")
    agent.print_beliefs()

    // Run perception-action cycles
    for cycle in 0..10 {
        // Simulate observation
        observation := rand.intn(agent.n_observations) or { 0 }

        println("\nStep ${cycle + 1}:")
        println("  Observation: ${observation}")

        // Execute perception-action cycle
        action := agent.step(observation)
        println("  Action: ${action}")

        print("  ")
        agent.print_beliefs()

        // Calculate and show free energy
        free_energy := agent.calculate_expected_free_energy(action)
        println("  Free Energy: ${free_energy:.3f}")
    }

    println("\n✅ V simulation completed successfully!")
}

// Main function
fn main() {
    run_simulation()
}
