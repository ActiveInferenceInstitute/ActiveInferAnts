use ndarray::{Array2, Array3};
use std::collections::HashMap;
use std::f32::consts::E;
use thiserror::Error;

struct MatrixInitializer;

impl MatrixInitializer {
    fn initialize<T: Into<Vec<usize>>>(config_key: &str, agent_params: &HashMap<String, Vec<f32>>, dims: T) -> Array2<f32> {
        agent_params.get(config_key)
            .map(|matrix| Array2::from_shape_vec(dims.into(), matrix.clone()).expect("Failed to create matrix from shape and vector"))
            .unwrap_or_else(|| Array2::zeros(dims.into()))
    }
}

struct ActiveInferenceAgent {
    position: Array2<f32>,
    influence_factor: f32,
    agent_params: HashMap<String, Vec<f32>>,
    matrices: HashMap<String, Array2<f32>>,
}

impl ActiveInferenceAgent {
    fn new(position: Array2<f32>, influence_factor: f32, agent_params: HashMap<String, Vec<f32>>) -> Self {
        let matrices = ["A_matrix_config", "B_matrix_config", "C_matrix_config", "D_matrix_config"]
            .iter()
            .map(|&config_key| {
                let dims = match config_key {
                    "B_matrix_config" => vec![agent_params["ACTION_MODALITIES"][0] as usize, agent_params["STATE_DIM"][0] as usize, agent_params["STATE_DIM"][0] as usize],
                    _ => vec![agent_params[&config_key.replace("_config", "").to_uppercase()][0] as usize],
                };
                (config_key.to_string(), MatrixInitializer::initialize(config_key, &agent_params, dims))
            })
            .collect::<HashMap<_, _>>();

        ActiveInferenceAgent {
            position,
            influence_factor,
            agent_params,
            matrices,
        }
    }

    fn perceive(&mut self, observations: Array2<f32>) {
        let prediction_error = &observations - &self.predict_sensory_outcomes().expect("Failed to predict sensory outcomes");
        self.update_beliefs(&prediction_error).expect("Failed to update beliefs");
    }

    fn predict_sensory_outcomes(&self) -> AgentResult<Array2<f32>> {
        let a_matrix = self.matrices.get("A_matrix_config")
            .ok_or(AgentError::InvalidConfiguration)?;
        
        if a_matrix.shape() != self.position.shape() {
            return Err(AgentError::DimensionMismatch);
        }
        
        Ok(a_matrix.dot(&self.position))
    }

    fn update_beliefs(&mut self, prediction_error: &Array2<f32>) -> AgentResult<()> {
        let adjusted_error = prediction_error
            .mapv(|e| e.clamp(-1.0, 1.0)) * self.influence_factor;
        
        self.position = (&self.position - &adjusted_error)
            .mapv(|x| x.max(0.0).min(1.0));
        
        Ok(())
    }

    /// Calculates variational free energy (VFE) using the formula:
    /// VFE = -E[log p(o|s)] + D_KL[q(s) || p(s)]
    /// Where:
    /// - p(o|s) is the likelihood (A matrix)
    /// - q(s) is the approximate posterior
    /// - p(s) is the prior beliefs
    fn calculate_vfe(&self, observation: &Array2<f32>) -> AgentResult<f32> {
        let qs = ProbabilityVector::new(self.approximate_posterior(observation)?)?;
        let a_matrix = self.matrices.get("A_matrix_config")
            .ok_or(AgentError::InvalidConfiguration)?;
        
        // Validate matrix dimensions
        if a_matrix.dim() != (qs.0.dim().0, observation.dim().0) {
            return Err(AgentError::DimensionMismatch);
        }
        
        let expected_log_likelihood = qs.0.dot(a_matrix.mapv(|a| a.ln()));
        let kl_divergence = &qs.0 * (&qs.0.mapv(|q| q.ln()) - &self.position.mapv(|p| p.ln()));
        Ok(-(expected_log_likelihood - kl_divergence.sum()))
    }

    fn calculate_efe(&self, action: Array2<f32>, future_states: Array2<f32>, preferences: Array2<f32>, uncertainty: f32) -> f32 {
        let pragmatic_value = &future_states * (&future_states.mapv(|f| f.ln()) - &preferences.mapv(|p| p.ln()));
        let epistemic_value = future_states.mapv(|f| f * f.ln()).sum() - future_states.sum().ln();
        pragmatic_value.sum() + uncertainty * epistemic_value
    }

    fn decide_next_action(&self) -> Array2<f32> {
        let possible_actions = self.generate_possible_actions();
        let efe_scores: Vec<f32> = possible_actions.iter().map(|action| {
            self.calculate_efe(action.clone(), self.predict_future_states(action), self.agent_params.get("preferences").unwrap().clone(), *self.agent_params.get("uncertainty").unwrap().get(0).unwrap())
        }).collect();

        possible_actions[efe_scores.iter().enumerate().min_by(|a, b| a.1.partial_cmp(b.1).unwrap_or(std::cmp::Ordering::Equal)).unwrap().0].clone()
    }

    fn update_internal_states(&mut self, action: Array2<f32>, observation: Array2<f32>) {
        self.matrices.entry("B_matrix_config").and_modify(|b_matrix| *b_matrix += &(action.dot(&observation)));
        self.matrices.entry("A_matrix_config").and_modify(|a_matrix| *a_matrix += &(observation.dot(&observation)));
    }

    fn move_agent(&mut self, direction: Array2<f32>) {
        self.position += &direction;
    }

    fn release_pheromone(&self, _type: &str, _rate: f32) {
        // Implementation goes here
    }

    fn produce_sound(&self, _type: &str, _intensity: f32) {
        // Implementation goes here
    }
}

struct ActiveColony(ActiveInferenceAgent);

impl ActiveColony {
    fn new(position: Array2<f32>, influence_factor: f32, agent_params: HashMap<String, Vec<f32>>) -> Self {
        ActiveColony(ActiveInferenceAgent::new(position, influence_factor, agent_params))
    }
}

struct ActiveNestmate(ActiveInferenceAgent);

impl ActiveNestmate {
    fn new(position: Array2<f32>, influence_factor: f32, agent_params: HashMap<String, Vec<f32>>) -> Self {
        ActiveNestmate(ActiveInferenceAgent::new(position, influence_factor, agent_params))
    }
}

// New type aliases for semantic validation
#[derive(Debug, Clone)]
struct ProbabilityVector(Array2<f32>);

impl ProbabilityVector {
    fn new(data: Array2<f32>) -> Result<Self, AgentError> {
        if data.iter().any(|&x| x < 0.0 || x > 1.0) || (data.sum() - 1.0).abs() > 1e-6 {
            Err(AgentError::InvalidProbability)
        } else {
            Ok(Self(data))
        }
    }
}

#[derive(Debug, Clone)]
struct TransitionMatrix(Array3<f32>);

impl TransitionMatrix {
    fn new(data: Array3<f32>) -> Result<Self, AgentError> {
        for mut matrix in data.axis_iter(Axis(0)) {
            let row_sums = matrix.sum_axis(Axis(1));
            if row_sums.iter().any(|&x| (x - 1.0).abs() > 1e-6) {
                return Err(AgentError::InvalidTransitionMatrix);
            }
        }
        Ok(Self(data))
    }
}

trait AgentMorphism {
    type Domain;
    type Codomain;
    
    fn compose(&self, other: &impl AgentMorphism) -> Result<Self, AgentError>;
    fn product(&self, other: &impl AgentMorphism) -> Result<Self, AgentError>;
}

impl AgentMorphism for ActiveInferenceAgent {
    type Domain = Array2<f32>;
    type Codomain = Array2<f32>;
    
    fn compose(&self, other: &impl AgentMorphism) -> Result<Self, AgentError> {
        let new_position = self.position.dot(&other.position());
        let new_params = self.agent_params.combine(&other.params())?;
        Ok(Self::new(new_position, self.influence_factor, new_params))
    }
    
    fn product(&self, other: &impl AgentMorphism) -> Result<Self, AgentError> {
        let combined_position = stack![Axis(0), self.position.view(), other.position().view()];
        let combined_params = self.agent_params.product(&other.params())?;
        Ok(Self::new(combined_position, self.influence_factor, combined_params))
    }
}

#[derive(Debug, thiserror::Error)]
pub enum AgentError {
    #[error("Invalid probability distribution")]
    InvalidProbability,
    #[error("Invalid transition matrix")]
    InvalidTransitionMatrix,
    #[error("Dimension mismatch in matrix operation")]
    DimensionMismatch,
    #[error("Invalid parameter configuration")]
    InvalidConfiguration,
    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),
}

type AgentResult<T> = Result<T, AgentError>;
