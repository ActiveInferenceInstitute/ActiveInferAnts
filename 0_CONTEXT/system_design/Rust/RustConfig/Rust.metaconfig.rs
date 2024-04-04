use std::collections::HashMap;
use std::sync::Mutex;

struct MetaConfig<'a> {
    config: Mutex<HashMap<&'a str, HashMap<&'a str, Vec<(i32, i32)>>>>,
}

impl<'a> MetaConfig<'a> {
    fn new() -> Self {
        Self {
            config: Mutex::new(Self::initialize_config()),
        }
    }

    fn initialize_config() -> HashMap<&'static str, HashMap<&'static str, Vec<(i32, i32)>>> {
        let mut config = HashMap::with_capacity(3);
        config.insert("SIMULATION", Self::simulation_config());
        config.insert("ACTIVE_INFERENCE", Self::active_inference_config());
        config.insert("ANT_AND_COLONY", Self::ant_and_colony_config());
        config
    }

    fn simulation_config() -> HashMap<&'static str, Vec<(i32, i32)>> {
        let mut config = HashMap::with_capacity(5);
        config.insert("MAX_STEPS_RANGE", vec![(100, 1000)]);
        config.insert("AGENT_COUNT_RANGE", vec![(50, 500)]);
        config.insert("NEST_COUNT_RANGE", vec![(1, 10)]);
        config.insert("WORKER_COUNT_RANGE", vec![(1, 8)]);
        config.insert("CLUSTER_NODE_COUNT_RANGE", vec![(2, 16)]);
        config
    }

    fn active_inference_config() -> HashMap<&'static str, Vec<(i32, i32)>> {
        let mut config = HashMap::with_capacity(5);
        config.insert("PLANNING_HORIZON", vec![(5, 30)]);
        // Convert floating-point range to integer to avoid precision issues and improve security
        config.insert("PRECISION_WEIGHTING_RANGE", vec![(1, 10)]); // Representing 0.1 to 1.0
        config.insert("GENERALIZATION_DEPTH_RANGE", vec![(1, 10)]);
        config.insert("ITERATION_LIMIT_RANGE", vec![(10, 50)]);
        // Convert floating-point range to integer to avoid precision issues and improve security
        config.insert("LEARNING_RATE_RANGE", vec![(1, 50)]); // Representing 0.01 to 0.5
        config
    }

    fn ant_and_colony_config() -> HashMap<&'static str, Vec<(i32, i32)>> {
        let mut config = HashMap::with_capacity(6);
        config.insert("PHEROMONE_TYPE_RANGE", vec![(1, 10)]);
        config.insert("MAX_PHEROMONE_RELEASE_RATE_RANGE", vec![(1, 10)]);
        config.insert("SOUND_INTENSITY_LEVEL_RANGE", vec![(1, 10)]);
        config.insert("PERCEPTUAL_FIELD_SIZE_RANGE", vec![(1, 7)]);
        config.insert("MEMORY_CAPACITY_RANGE", vec![(50, 200)]);
        config.insert("ATTENTION_SPAN_RANGE", vec![(3, 10)]);
        config
    }
}

fn main() {
    let meta_config = MetaConfig::new();
    match meta_config.config.lock() {
        Ok(config) => println!("{:?}", config),
        Err(e) => eprintln!("Failed to acquire lock: {}", e),
    }
}
