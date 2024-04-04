use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use ring::digest::{Context, Digest, SHA256};

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Config {
    pub simulation: Simulation,
    pub ants: Ants,
    pub world: World,
    pub food: Food,
    pub pheromones: Pheromones,
    pub security: SecurityConfig,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Simulation {
    pub num_ants: usize,
    pub num_food: usize,
    pub evaporation_rate: f32,
    pub diffusion_rate: f32,
    pub max_steps: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Ants {
    pub speed: f32,
    pub sensor_angle: f32,
    pub sensor_offset_distance: f32,
    pub turning_speed: f32,
    pub initial_pheromone_strength: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct World {
    pub width: f32,
    pub height: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Food {
    pub radius: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Pheromones {
    pub radius: f32,
    pub max_strength: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct SecurityConfig {
    pub encryption_keys: HashMap<String, String>,
    pub integrity_check: IntegrityCheck,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct IntegrityCheck {
    pub enabled: bool,
    pub hash: String,
}

impl SecurityConfig {
    pub fn new(encryption_keys: HashMap<String, String>) -> Self {
        Self {
            encryption_keys,
            integrity_check: IntegrityCheck::default(),
        }
    }

    pub fn calculate_hash(&mut self, data: &[u8]) -> Digest {
        let mut context = Context::new(&SHA256);
        context.update(data);
        let hash = context.finish();
        self.integrity_check.hash = format!("{:?}", hash);
        hash
    }
}


use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use ring::digest::{Context, Digest, SHA256};

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Config {
    pub simulation: Simulation,
    pub ants: Ants,
    pub world: World,
    pub food: Food,
    pub pheromones: Pheromones,
    pub security: SecurityConfig,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Simulation {
    pub num_ants: usize,
    pub num_food: usize,
    pub evaporation_rate: f32,
    pub diffusion_rate: f32,
    pub max_steps: usize,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Ants {
    pub speed: f32,
    pub sensor_angle: f32,
    pub sensor_offset_distance: f32,
    pub turning_speed: f32,
    pub initial_pheromone_strength: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct World {
    pub width: f32,
    pub height: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Food {
    pub radius: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct Pheromones {
    pub radius: f32,
    pub max_strength: f32,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct SecurityConfig {
    pub encryption_keys: HashMap<String, String>,
    pub integrity_check: IntegrityCheck,
}

#[derive(Debug, Clone, Serialize, Deserialize, Default)]
pub struct IntegrityCheck {
    pub enabled: bool,
    pub hash: String,
}

impl SecurityConfig {
    pub fn new(encryption_keys: HashMap<String, String>) -> Self {
        Self {
            encryption_keys,
            integrity_check: IntegrityCheck::default(),
        }
    }

    pub fn calculate_hash(&mut self, data: &[u8]) -> Digest {
        let mut context = Context::new(&SHA256);
        context.update(data);
        let hash = context.finish();
        self.integrity_check.hash = format!("{:?}", hash);
        hash
    }
}