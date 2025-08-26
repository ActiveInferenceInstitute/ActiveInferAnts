// Active Inference Implementation in Odin

package main

import "core:fmt"
import "core:math"
import "core:math/rand"
import "core:slice"

// Simple matrix operations (since Odin doesn't have built-in matrix library)
Matrix :: struct {
    data: []f64,
    rows: int,
    cols: int,
}

matrix_create :: proc(rows, cols: int, allocator := context.allocator) -> Matrix {
    return Matrix{
        data = make([]f64, rows * cols, allocator),
        rows = rows,
        cols = cols,
    }
}

matrix_get :: proc(m: Matrix, row, col: int) -> f64 {
    return m.data[row * m.cols + col]
}

matrix_set :: proc(m: Matrix, row, col: int, value: f64) {
    m.data[row * m.cols + col] = value
}

matrix_row :: proc(m: Matrix, row: int, allocator := context.allocator) -> []f64 {
    result := make([]f64, m.cols, allocator)
    for col in 0..<m.cols {
        result[col] = matrix_get(m, row, col)
    }
    return result
}

matrix_normalize_row :: proc(m: ^Matrix, row: int) {
    start_idx := row * m.cols
    end_idx := start_idx + m.cols

    // Calculate sum
    sum: f64 = 0.0
    for i in start_idx..<end_idx {
        sum += m.data[i]
    }

    // Normalize if sum > 0
    if sum > 0.0 {
        for i in start_idx..<end_idx {
            m.data[i] /= sum
        }
    }
}

// Active Inference Agent
Active_Inference_Agent :: struct {
    beliefs: []f64,
    a_matrix: Matrix,  // Likelihood P(o|s)
    b_matrices: []Matrix, // Transition P(s'|s,a) for each action
    c_vector: []f64,   // Preferences P(o)
    d_vector: []f64,   // Prior beliefs P(s)
    precision: f64,
    learning_rate: f64,
    n_states: int,
    n_observations: int,
    n_actions: int,
}

create_agent :: proc(n_states, n_observations, n_actions: int, allocator := context.allocator) -> Active_Inference_Agent {
    agent := Active_Inference_Agent{
        beliefs = make([]f64, n_states, allocator),
        a_matrix = matrix_create(n_observations, n_states, allocator),
        b_matrices = make([]Matrix, n_actions, allocator),
        c_vector = make([]f64, n_observations, allocator),
        d_vector = make([]f64, n_states, allocator),
        precision = 1.0,
        learning_rate = 0.1,
        n_states = n_states,
        n_observations = n_observations,
        n_actions = n_actions,
    }

    // Initialize B matrices
    for &b_matrix in agent.b_matrices {
        b_matrix = matrix_create(n_states, n_states, allocator)
    }

    initialize_generative_model(&agent)
    initialize_beliefs(&agent)

    return agent
}

initialize_generative_model :: proc(agent: ^Active_Inference_Agent) {
    // Initialize A matrix (observation likelihood)
    for obs in 0..<agent.n_observations {
        for state in 0..<agent.n_states {
            // Diagonal structure with noise
            is_diagonal := obs == state % agent.n_observations
            base_prob: f64 = is_diagonal ? 0.7 : 0.1
            noise := (rand.float64() - 0.5) * 0.2
            prob := math.max(0.0, math.min(1.0, base_prob + noise))
            matrix_set(agent.a_matrix, obs, state, prob)
        }
        matrix_normalize_row(&agent.a_matrix, obs)
    }

    // Initialize B matrices (state transitions)
    for action in 0..<agent.n_actions {
        for from_state in 0..<agent.n_states {
            for to_state in 0..<agent.n_states {
                prob: f64
                if action == 0 {
                    // Stay action
                    prob = to_state == from_state ? 0.8 : 0.05
                } else if action == 1 {
                    // Move action
                    prob = to_state == (from_state + 1) % agent.n_states ? 0.7 : 0.05
                } else {
                    // Random action
                    prob = 1.0 / f64(agent.n_states)
                }
                matrix_set(agent.b_matrices[action], from_state, to_state, prob)
            }
            matrix_normalize_row(&agent.b_matrices[action], from_state)
        }
    }

    // Initialize C vector (preferences)
    for obs in 0..<agent.n_observations {
        agent.c_vector[obs] = obs < agent.n_observations / 2 ? 1.0 : 0.1
    }

    // Initialize D vector (prior beliefs)
    for state in 0..<agent.n_states {
        agent.d_vector[state] = 1.0 / f64(agent.n_states)
    }
}

initialize_beliefs :: proc(agent: ^Active_Inference_Agent) {
    for i in 0..<agent.n_states {
        agent.beliefs[i] = agent.d_vector[i]
    }
}

normalize_vector :: proc(vector: []f64) {
    sum: f64 = 0.0
    for val in vector {
        sum += val
    }

    if sum > 0.0 {
        for &val in vector {
            val /= sum
        }
    }
}

update_beliefs :: proc(agent: ^Active_Inference_Agent, observation: int) {
    likelihood := matrix_row(agent.a_matrix, observation)

    // Bayesian update: posterior = prior * likelihood
    for i in 0..<len(agent.beliefs) {
        agent.beliefs[i] *= likelihood[i]
    }

    // Normalize
    normalize_vector(agent.beliefs)

    delete(likelihood)
}

calculate_expected_free_energy :: proc(agent: Active_Inference_Agent, action: int) -> f64 {
    // Simplified EFE calculation using entropy
    efe: f64 = 0.0
    for belief in agent.beliefs {
        if belief > 0.0 {
            efe -= belief * math.ln(belief)
        }
    }
    return efe
}

select_action :: proc(agent: Active_Inference_Agent) -> int {
    min_efe := math.F64_MAX
    best_action := 0

    for action in 0..<agent.n_actions {
        efe := calculate_expected_free_energy(agent, action)
        if efe < min_efe {
            min_efe = efe
            best_action = action
        }
    }

    return best_action
}

step :: proc(agent: ^Active_Inference_Agent, observation: int) -> int {
    update_beliefs(agent, observation)
    return select_action(agent^)
}

print_beliefs :: proc(agent: Active_Inference_Agent) {
    fmt.print("Beliefs: [")
    for i in 0..<len(agent.beliefs) {
        fmt.printf("%.3f", agent.beliefs[i])
        if i < len(agent.beliefs) - 1 {
            fmt.print(", ")
        }
    }
    fmt.println("]")
}

run_simulation :: proc() {
    fmt.println("🧠 Odin Language Active Inference Demo")
    fmt.println("======================================")

    // Create agent
    agent := create_agent(4, 3, 2)

    // Show initial beliefs
    fmt.print("Initial ")
    print_beliefs(agent)

    // Run perception-action cycles
    for cycle in 0..<10 {
        // Simulate observation
        observation := rand.int_max(agent.n_observations)

        fmt.printf("\nStep %d:\n", cycle + 1)
        fmt.printf("  Observation: %d\n", observation)

        // Execute perception-action cycle
        action := step(&agent, observation)
        fmt.printf("  Action: %d\n", action)

        fmt.print("  ")
        print_beliefs(agent)

        // Calculate and show free energy
        free_energy := calculate_expected_free_energy(agent, action)
        fmt.printf("  Free Energy: %.3f\n", free_energy)
    }

    fmt.println("\n✅ Odin simulation completed successfully!")
}

main :: proc() {
    run_simulation()
}
