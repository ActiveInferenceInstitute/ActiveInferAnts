use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct SimulationConfig {
    max_steps: u32,
    agent_count: u32,
    nest_count: u32,
    parallel_execution: ParallelExecution,
    computation_settings: ComputationSettings,
}

#[derive(Debug, Serialize, Deserialize)]
struct ParallelExecution {
    enabled: bool,
    worker_count: u32,
    strategy: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct ComputationSettings {
    gpu_acceleration: bool,
    gpu_preference: String,
    distributed_computing: DistributedComputing,
}

#[derive(Debug, Serialize, Deserialize)]
struct DistributedComputing {
    enabled: bool,
    cluster_node_count: u32,
    communication_protocol: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct ActiveInferenceConfig {
    enabled: bool,
    inference_models: Vec<String>,
    expectation_free_energy: bool,
    planning_horizon: PlanningHorizon,
    time_resolution: String,
    precision_weighting: PrecisionWeighting,
    generalization_depth: u32,
    iteration_limit: u32,
    adaptive_learning: AdaptiveLearning,
    context_awareness: ContextAwareness,
    cognitive_complexity: CognitiveComplexity,
    surprise_minimization: bool,
    goal_oriented_behavior: GoalOrientedBehavior,
    learning_rate: f64,
    efe_calculation_params: EFECalculationParams,
    meta_learning: MetaLearning,
    multi_objective_decision_making: MultiObjectiveDecisionMaking,
    uncertainty_management: UncertaintyManagement,
    communication: Communication,
    learning_mechanisms: LearningMechanisms,
}

#[derive(Debug, Serialize, Deserialize)]
struct PlanningHorizon {
    #[serde(rename = "TYPE")]
    type_: String,
    base_value: u32,
    adaptation_strategy: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct PrecisionWeighting {
    perception: AdaptiveBase,
    action: AdaptiveBase,
}

#[derive(Debug, Serialize, Deserialize)]
struct AdaptiveBase {
    base: f64,
    adaptive: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct AdaptiveLearning {
    enabled: bool,
    learning_rate: f64,
    feedback_sensitivity: String,
    model_updating: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct ContextAwareness {
    enabled: bool,
    context_types: Vec<String>,
    dynamic_adjustment: bool,
    prediction: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct CognitiveComplexity {
    enabled: bool,
    types: Vec<String>,
    strategy_adaptation: bool,
    complexity_management: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct GoalOrientedBehavior {
    enabled: bool,
    goals: Vec<String>,
    goal_prioritization: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct EFECalculationParams {
    default: f64,
}

#[derive(Debug, Serialize, Deserialize)]
struct MetaLearning {
    enabled: bool,
    strategies: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct MultiObjectiveDecisionMaking {
    enabled: bool,
    integration_strategy: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct UncertaintyManagement {
    enabled: bool,
    strategies: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct Communication {
    enabled: bool,
    modes: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct LearningMechanisms {
    enabled: bool,
    types: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct AntAndColonyConfig {
    nestmate: Nestmate,
    colony: Colony,
}

#[derive(Debug, Serialize, Deserialize)]
struct Nestmate {
    active_inference: ActiveInference,
}

#[derive(Debug, Serialize, Deserialize)]
struct ActiveInference {
    blanket_states: BlanketStates,
    internal_states: InternalStates,
}

#[derive(Debug, Serialize, Deserialize)]
struct BlanketStates {
    action: Action,
    sense: Sense,
}

#[derive(Debug, Serialize, Deserialize)]
struct Action {
    movement: Vec<Vec<i32>>,
    pheromone_release: PheromoneRelease,
    sound_production: SoundProduction,
}

#[derive(Debug, Serialize, Deserialize)]
struct PheromoneRelease {
    types: HashMap<String, PheromoneType>,
    queen_pheromone: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct PheromoneType {
    id: u32,
    max_rate: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct SoundProduction {
    types: Vec<String>,
    intensity_levels: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Sense {
    observations: Observations,
}

#[derive(Debug, Serialize, Deserialize)]
struct Observations {
    vision: u32,
    width: u32,
    height: u32,
    total_size: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct InternalStates {
    cognitive: Cognitive,
    meta_cognitive: MetaCognitive,
    sensory_processing: SensoryProcessing,
}

#[derive(Debug, Serialize, Deserialize)]
struct Cognitive {
    memory_capacity: u32,
    attention_span: u32,
    theory_of_mind: bool,
    problem_solving: bool,
    emotional_intelligence: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct MetaCognitive {
    decision_strategy: String,
    learning_rate: f64,
    adaptability: bool,
    risk_taking: String,
    creativity: String,
    social_learning: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct SensoryProcessing {
    visual: bool,
    auditory: bool,
    tactile: bool,
    olfactory: bool,
    gustatory: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct Colony {
    initial_positions: InitialPositions,
    influence_factor: f64,
    life_stage: String,
    demographics: Demographics,
    structure: String,
    storage: Storage,
    defenses: Vec<String>,
    foraging_strategies: Vec<String>,
    communication_methods: Vec<String>,
    mortality_rates: MortalityRates,
    resource_needs: ResourceNeeds,
    expansion_strategy: String,
    threat_responses: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct InitialPositions {
    xyz: XYZ,
    ivm: IVM,
}

#[derive(Debug, Serialize, Deserialize)]
struct XYZ {
    x: u32,
    y: u32,
    z: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct IVM {
    w: u32,
    x: u32,
    y: u32,
    z: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Demographics {
    workers: u32,
    queens: u32,
    males: u32,
    larvae: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Storage {
    food_capacity: u32,
    water_system: bool,
}

#[derive(Debug, Serialize, Deserialize)]
struct MortalityRates {
    workers: f64,
    larvae: f64,
}

#[derive(Debug, Serialize, Deserialize)]
struct ResourceNeeds {
    food_consumption: u32,
    water_consumption: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct EnvironmentConfig {
    grid: Grid,
    resource_zones: Vec<ResourceZone>,
    obstacles: Vec<Obstacle>,
    environmental_grounds: Vec<String>,
    pheromone_config: PheromoneConfig,
}

#[derive(Debug, Serialize, Deserialize)]
struct Grid {
    width: u32,
    height: u32,
    dimensions: Vec<u32>,
    total_size: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct ResourceZone {
    #[serde(rename = "TYPE")]
    type_: String,
    position: Position,
    size: Size,
    dimensions: Vec<u32>,
    total_size: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Position {
    x: u32,
    y: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Size {
    width: u32,
    height: u32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Obstacle {
    #[serde(rename = "TYPE")]
    type_: String,
    position: Position,
    size: Size,
    dimensions: Vec<u32>,
}

#[derive(Debug, Serialize, Deserialize)]
struct PheromoneConfig {
    stigmergy_types: Vec<String>,
    molecular_stigmergy_types: Vec<String>,
    level_count: u32,
    decay_rate: f64,
}
