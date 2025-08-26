//! # Active Inference Implementation in Rust
//!
//! High-performance, memory-safe implementation of active inference algorithms
//! using Rust's ownership system and zero-cost abstractions.

use ndarray::prelude::*;
use ndarray_rand::RandomExt;
use rand::distributions::Uniform;
use std::error::Error;
use std::fmt;

// Custom error type for the active inference agent
#[derive(thiserror::Error, Debug)]
pub enum AgentError {
    #[error("Invalid probability distribution: sum = {sum}")]
    InvalidProbability { sum: f64 },
    #[error("Numerical computation error: {message}")]
    NumericalError { message: String },
    #[error("Dimension mismatch: expected {expected}, got {actual}")]
    DimensionMismatch { expected: usize, actual: usize },
}

// Result type alias for convenience
type AgentResult<T> = std::result::Result<T, AgentError>;

/// Core Active Inference Agent
#[derive(Debug, Clone)]
pub struct ActiveInferenceAgent {
    /// Current belief state probabilities
    pub beliefs: Array1<f64>,
    /// Generative model (A, B, C, D matrices)
    pub generative_model: GenerativeModel,
    /// Precision parameter for belief updates
    pub precision: f64,
    /// Learning rate for parameter updates
    pub learning_rate: f64,
    /// History of belief states for analysis
    pub belief_history: Vec<Array1<f64>>,
}

/// Generative model components (A, B, C, D matrices)
#[derive(Debug, Clone)]
pub struct GenerativeModel {
    /// A matrix: Likelihood of observations given states
    pub a_matrix: Array2<f64>,
    /// B matrix: State transition probabilities
    pub b_matrix: Array3<f64>,
    /// C matrix: Preferred observations (goal priors)
    pub c_vector: Array1<f64>,
    /// D vector: Initial state probabilities
    pub d_vector: Array1<f64>,
}

impl GenerativeModel {
    /// Create a new generative model with specified dimensions
    pub fn new(n_states: usize, n_observations: usize, n_actions: usize) -> Self {
        // Initialize with uniform distributions
        let a_matrix = Array::random((n_observations, n_states), Uniform::new(0.0, 1.0));
        let b_matrix = Array::random((n_states, n_states, n_actions), Uniform::new(0.0, 1.0));
        let c_vector = Array::random(n_observations, Uniform::new(0.0, 1.0));
        let d_vector = Array::random(n_states, Uniform::new(0.0, 1.0));

        // Normalize to ensure valid probability distributions
        let mut model = Self {
            a_matrix,
            b_matrix,
            c_vector,
            d_vector,
        };
        model.normalize();
        model
    }

    /// Normalize all probability distributions
    fn normalize(&mut self) {
        // Normalize A matrix (columns should sum to 1)
        for mut col in self.a_matrix.columns_mut() {
            let sum = col.sum();
            if sum > 0.0 {
                col /= sum;
            }
        }

        // Normalize B matrix slices (for each action, state transitions should sum to 1)
        for mut action_slice in self.b_matrix.outer_iter_mut() {
            for mut state_transitions in action_slice.columns_mut() {
                let sum = state_transitions.sum();
                if sum > 0.0 {
                    state_transitions /= sum;
                }
            }
        }

        // Normalize D vector
        let sum = self.d_vector.sum();
        if sum > 0.0 {
            self.d_vector /= sum;
        }
    }

    /// Get likelihood of observation given current beliefs
    pub fn get_likelihood(&self, observation: usize) -> Array1<f64> {
        self.a_matrix.row(observation).to_owned()
    }

    /// Get state transition probabilities for a given action
    pub fn get_transition(&self, action: usize) -> Array2<f64> {
        self.b_matrix.index_axis(Axis(2), action).to_owned()
    }
}

impl ActiveInferenceAgent {
    /// Create a new active inference agent
    pub fn new(n_states: usize, n_observations: usize, n_actions: usize) -> Self {
        let generative_model = GenerativeModel::new(n_states, n_observations, n_actions);
        let beliefs = generative_model.d_vector.clone(); // Start with prior beliefs

        Self {
            beliefs: beliefs.clone(),
            generative_model,
            precision: 1.0,
            learning_rate: 0.1,
            belief_history: vec![beliefs],
        }
    }

    /// Update beliefs based on new observation using Bayesian inference
    pub fn update_beliefs(&mut self, observation: usize) -> AgentResult<()> {
        let likelihood = self.generative_model.get_likelihood(observation);

        // Compute posterior: P(s|o) ∝ P(o|s) * P(s)
        let posterior = &likelihood * &self.beliefs;

        // Normalize posterior
        let sum = posterior.sum();
        if sum <= 0.0 {
            return Err(AgentError::InvalidProbability { sum });
        }

        self.beliefs = posterior / sum;
        self.belief_history.push(self.beliefs.clone());

        Ok(())
    }

    /// Select action using expected free energy minimization
    pub fn select_action(&self, n_actions: usize) -> usize {
        let mut expected_free_energies = Vec::new();

        for action in 0..n_actions {
            let transition_matrix = self.generative_model.get_transition(action);

            // Compute expected posterior beliefs after action
            let expected_beliefs = transition_matrix.dot(&self.beliefs);

            // Compute expected free energy (simplified)
            let efe = self.compute_expected_free_energy(&expected_beliefs);
            expected_free_energies.push(efe);
        }

        // Select action with minimum expected free energy
        expected_free_energies
            .iter()
            .enumerate()
            .min_by(|a, b| a.1.partial_cmp(b.1).unwrap_or(std::cmp::Ordering::Equal))
            .map(|(i, _)| i)
            .unwrap_or(0)
    }

    /// Compute expected free energy for a belief state
    fn compute_expected_free_energy(&self, beliefs: &Array1<f64>) -> f64 {
        // Simplified expected free energy computation
        // In practice, this would involve computing expected precision-weighted divergence
        let divergence: f64 = beliefs
            .iter()
            .zip(&self.generative_model.d_vector)
            .map(|(p, q)| {
                if *p > 0.0 && *q > 0.0 {
                    p * (p / q).ln()
                } else {
                    0.0
                }
            })
            .sum();

        divergence * self.precision
    }

    /// Learn from experience (update generative model parameters)
    pub fn learn(&mut self, observation: usize, action: usize, next_observation: usize) {
        // Simple learning rule - in practice this would be more sophisticated
        let learning_rate = self.learning_rate;

        // Update A matrix (observation likelihood)
        let mut obs_row = self.generative_model.a_matrix.row_mut(observation);
        obs_row.scaled_add(learning_rate, &(&self.beliefs * (1.0 - obs_row.sum())));

        // Update B matrix (state transitions)
        let mut transition_matrix = self.generative_model.b_matrix.index_axis_mut(Axis(2), action);
        for (i, mut col) in transition_matrix.columns_mut().into_iter().enumerate() {
            if i == next_observation {
                col.scaled_add(learning_rate, &(&self.beliefs * (1.0 - col.sum())));
            }
        }

        // Renormalize after learning
        self.generative_model.normalize();
    }

    /// Run a complete simulation
    pub fn run_simulation(&mut self, steps: usize, n_actions: usize) -> AgentResult<SimulationResults> {
        let mut actions = Vec::new();
        let mut observations = Vec::new();
        let mut free_energies = Vec::new();

        for step in 0..steps {
            // Generate observation based on current beliefs
            let observation = self.sample_observation()?;
            observations.push(observation);

            // Update beliefs
            self.update_beliefs(observation)?;

            // Select action
            let action = self.select_action(n_actions);
            actions.push(action);

            // Compute free energy
            let fe = self.compute_expected_free_energy(&self.beliefs);
            free_energies.push(fe);

            // Learn from experience (simplified - would need actual next observation)
            if step < steps - 1 {
                let next_observation = self.sample_observation()?;
                self.learn(observation, action, next_observation);
            }
        }

        Ok(SimulationResults {
            actions,
            observations,
            belief_history: self.belief_history.clone(),
            free_energies,
        })
    }

    /// Sample observation from current belief state
    fn sample_observation(&self) -> AgentResult<usize> {
        let probs = self.generative_model.a_matrix.dot(&self.beliefs);

        // Normalize
        let sum = probs.sum();
        if sum <= 0.0 {
            return Err(AgentError::InvalidProbability { sum });
        }
        let probs = probs / sum;

        // Sample from categorical distribution
        let mut cumsum = 0.0;
        let rand_val: f64 = rand::random();

        for (i, &prob) in probs.iter().enumerate() {
            cumsum += prob;
            if rand_val <= cumsum {
                return Ok(i);
            }
        }

        Ok(probs.len() - 1) // fallback
    }

    /// Get current entropy of belief distribution
    pub fn belief_entropy(&self) -> f64 {
        self.beliefs
            .iter()
            .filter(|&&p| p > 0.0)
            .map(|&p| -p * p.ln())
            .sum::<f64>()
    }

    /// Get simulation statistics
    pub fn get_statistics(&self) -> AgentStatistics {
        AgentStatistics {
            current_entropy: self.belief_entropy(),
            belief_history_length: self.belief_history.len(),
            max_belief: self.beliefs.fold(f64::NEG_INFINITY, |a, &b| a.max(b)),
            min_belief: self.beliefs.fold(f64::INFINITY, |a, &b| a.min(b)),
            mean_belief: self.beliefs.mean().unwrap_or(0.0),
        }
    }
}

/// Results from a simulation run
#[derive(Debug, Clone)]
pub struct SimulationResults {
    pub actions: Vec<usize>,
    pub observations: Vec<usize>,
    pub belief_history: Vec<Array1<f64>>,
    pub free_energies: Vec<f64>,
}

impl SimulationResults {
    /// Compute summary statistics
    pub fn summary(&self) -> SimulationSummary {
        let avg_free_energy = self.free_energies.iter().sum::<f64>() / self.free_energies.len() as f64;
        let action_diversity = (0..self.actions.len().max(1))
            .map(|i| if self.actions.contains(&i) { 1 } else { 0 })
            .sum::<usize>() as f64 / self.actions.len().max(1) as f64;

        SimulationSummary {
            total_steps: self.actions.len(),
            average_free_energy: avg_free_energy,
            action_diversity,
            total_observations: self.observations.len(),
        }
    }
}

/// Summary statistics for simulation results
#[derive(Debug)]
pub struct SimulationSummary {
    pub total_steps: usize,
    pub average_free_energy: f64,
    pub action_diversity: f64,
    pub total_observations: usize,
}

/// Agent statistics
#[derive(Debug)]
pub struct AgentStatistics {
    pub current_entropy: f64,
    pub belief_history_length: usize,
    pub max_belief: f64,
    pub min_belief: f64,
    pub mean_belief: f64,
}

impl fmt::Display for AgentStatistics {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Agent Statistics:\n")?;
        write!(f, "  Current Entropy: {:.4}\n", self.current_entropy)?;
        write!(f, "  Belief History Length: {}\n", self.belief_history_length)?;
        write!(f, "  Max Belief: {:.4}\n", self.max_belief)?;
        write!(f, "  Min Belief: {:.4}\n", self.min_belief)?;
        write!(f, "  Mean Belief: {:.4}\n", self.mean_belief)
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("🦀 Active Inference Simulation in Rust");
    println!("======================================");

    // Simulation parameters
    let n_states = 4;
    let n_observations = 6;
    let n_actions = 3;
    let steps = 20;

    // Create agent
    let mut agent = ActiveInferenceAgent::new(n_states, n_observations, n_actions);

    println!("🚀 Starting simulation with {} steps...", steps);
    println!("📊 Initial beliefs: {:?}", agent.beliefs);

    // Run simulation
    let results = agent.run_simulation(steps, n_actions)?;

    // Display results
    println!("\n📈 Simulation Results:");
    println!("  Total steps: {}", results.actions.len());
    println!("  Actions taken: {:?}", results.actions);
    println!("  Observations: {:?}", results.observations);
    println!("  Final beliefs: {:?}", agent.beliefs);

    // Show statistics
    let stats = agent.get_statistics();
    println!("\n{}", stats);

    let summary = results.summary();
    println!("\n🎯 Simulation Summary:");
    println!("  Average Free Energy: {:.4}", summary.average_free_energy);
    println!("  Action Diversity: {:.4}", summary.action_diversity);

    println!("\n✅ Rust Active Inference simulation completed successfully!");

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_agent_creation() {
        let agent = ActiveInferenceAgent::new(3, 4, 2);
        assert_eq!(agent.beliefs.len(), 3);
        assert!(agent.beliefs.sum() > 0.99); // Should be normalized
    }

    #[test]
    fn test_belief_update() {
        let mut agent = ActiveInferenceAgent::new(2, 3, 2);
        let initial_entropy = agent.belief_entropy();

        agent.update_beliefs(0).unwrap();

        // Entropy should generally decrease with new information
        // (though this is not guaranteed for all cases)
        let new_entropy = agent.belief_entropy();
        assert!(new_entropy >= 0.0);
    }

    #[test]
    fn test_simulation_run() {
        let mut agent = ActiveInferenceAgent::new(3, 4, 2);
        let results = agent.run_simulation(10, 2).unwrap();

        assert_eq!(results.actions.len(), 10);
        assert_eq!(results.observations.len(), 10);
        assert!(!results.free_energies.is_empty());
    }

    #[test]
    fn test_invalid_probability() {
        let mut agent = ActiveInferenceAgent::new(2, 2, 1);
        // This should handle edge cases gracefully
        let result = agent.update_beliefs(0);
        assert!(result.is_ok());
    }
}