use ndarray::{ArrayD, Array1};
use std::collections::HashMap;
use std::option::Option;
use std::vec::Vec;

/// A struct representing an AntAgent that employs active inference for decision-making.
struct AntAgent {
    observation_model: ArrayD<f64>,
    transition_model: ArrayD<f64>,
    preference_model: ArrayD<f64>,
    initial_state_distribution: ArrayD<f64>,
    policy_prior: Option<ArrayD<f64>>,
    policy_length: usize,
    inference_depth: usize,
    controllable_factors: Vec<usize>,
    possible_policies: Option<ArrayD<f64>>,
    generative_model: HashMap<String, ArrayD<f64>>,
    model_dimensions: HashMap<String, Vec<usize>>,
    posterior_states: ArrayD<f64>,
    updated_policies: ArrayD<f64>,
}

impl AntAgent {
    /// Constructs a new `AntAgent`.
    fn new(
        observation_model: ArrayD<f64>,
        transition_model: ArrayD<f64>,
        preference_model: ArrayD<f64>,
        initial_state_distribution: ArrayD<f64>,
        policy_prior: Option<ArrayD<f64>>,
        policy_length: usize,
        inference_depth: usize,
        controllable_factors: Option<Vec<usize>>,
        possible_policies: Option<ArrayD<f64>>,
    ) -> Self {
        let observation_model = utils::to_obj_array(observation_model);
        let transition_model = utils::to_obj_array(transition_model);
        let initial_state_distribution = Self::_initialize_alternate_initial_state_distribution();
        let policy_prior = Self::_introduce_policy_prior_modifications();

        let generative_model = [
            ("observation_model", observation_model.clone()),
            ("transition_model", transition_model.clone()),
            ("preference_model", preference_model.clone()),
            ("initial_state_distribution", initial_state_distribution.clone()),
            ("policy_prior", policy_prior.clone()),
        ].iter().cloned().collect();

        let model_dimensions = Self::_calculate_model_dimensions(&observation_model, &transition_model);

        let controllable_factors = controllable_factors.unwrap_or_else(|| (0..model_dimensions["num_factors"][0]).collect::<Vec<_>>());
        let possible_policies = possible_policies.unwrap_or_else(|| Self::_define_possible_policies(&model_dimensions, &controllable_factors, policy_length));

        AntAgent {
            observation_model,
            transition_model,
            preference_model,
            initial_state_distribution,
            policy_prior: Some(policy_prior),
            policy_length,
            inference_depth,
            controllable_factors,
            possible_policies: Some(possible_policies),
            generative_model,
            model_dimensions,
            posterior_states: initial_state_distribution.clone(),
            updated_policies: ArrayD::<f64>::zeros((0,).f()),
        }
    }

    /// Calculates the dimensions of the models for subsequent operations.
    fn _calculate_model_dimensions(observation_model: &ArrayD<f64>, transition_model: &ArrayD<f64>) -> HashMap<String, Vec<usize>> {
        let num_observations = observation_model.shape().iter().map(|&s| s as usize).collect::<Vec<_>>();
        let num_states = transition_model.shape().iter().map(|&s| s as usize).collect::<Vec<_>>();
        [
            ("num_observations", num_observations),
            ("num_states", num_states),
            ("num_modalities", vec![observation_model.ndim()]),
            ("num_factors", vec![transition_model.ndim()]),
        ].iter().cloned().collect()
    }

    /// Generates the set of feasible policies based on the agent's models.
    fn _define_possible_policies(model_dimensions: &HashMap<String, Vec<usize>>, controllable_factors: &Vec<usize>, policy_length: usize) -> ArrayD<f64> {
        control::construct_policies(model_dimensions, controllable_factors, policy_length)
    }

    /// Updates the agent's beliefs regarding hidden states upon receiving new observations.
    fn update_beliefs_about_states(&mut self, observation: ArrayD<f64>) {
        self.posterior_states = inference::update_posterior_states(&self.observation_model, &observation, &self.transition_model, &self.posterior_states, self.policy_length, self.inference_depth);
    }

    /// Refines the agent's beliefs over policies, integrating current states and model insights.
    fn update_beliefs_about_policies(&mut self) {
        let (updated_policies, _) = control::update_posterior_policies(&self.posterior_states, &self.observation_model, &self.transition_model, &self.preference_model, self.possible_policies.as_ref().unwrap(), self.policy_prior.as_ref().unwrap());
        self.updated_policies = updated_policies;
    }

    /// Determines an action based on the agent's current policy beliefs.
    fn choose_action(&self) -> Array1<f64> {
        control::sample_action(&self.updated_policies, self.possible_policies.as_ref().unwrap(), &self.model_dimensions["num_factors"], &self.controllable_factors)
    }

    /// Conducts a single action selection cycle based on a new observation.
    fn execute_step(&mut self, observation: ArrayD<f64>) -> Array1<f64> {
        self.update_beliefs_about_states(observation);
        self.update_beliefs_about_policies();
        self.choose_action()
    }
}
