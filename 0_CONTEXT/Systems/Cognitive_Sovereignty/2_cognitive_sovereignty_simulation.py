import sys
from utils_cognitive_sovereignty import (
    CognitiveSovereignty, load_entity_library, ensure_output_directory,
    save_results, visualize_simulation, visualize_entity_traces, visualize_transition_matrices, STATES
)
import logging
import argparse
from typing import List, Dict, Any
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_config(config_file: str) -> Dict[str, Any]:
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def run_simulation(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Run the Cognitive Sovereignty simulation with the given configuration."""
    input_dir = config['input_dir']
    output_dir = config['output_dir']
    before_crisis = config['before_crisis']
    after_crisis = config['after_crisis']

    ensure_output_directory(output_dir)
    
    # Load entity library
    entities = load_entity_library(f"{input_dir}/entity_library.json")
    
    # Visualize transition matrices
    visualize_transition_matrices(entities, f"{output_dir}/transition_matrices_visualization.png")
    
    # Initialize simulation
    simulation = CognitiveSovereignty()
    for entity in entities:
        simulation.add_entity(entity)
    
    # Run simulation
    results = simulation.run_simulation(before_crisis, after_crisis)
    
    # Save results
    save_results(results, f"{output_dir}/simulation_results.json")
    
    # Visualize results
    visualize_simulation(results, f"{output_dir}/simulation_visualization.png", before_crisis)
    visualize_entity_traces(results, f"{output_dir}/entity_traces_visualization.png", before_crisis)
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Run Cognitive Sovereignty simulation")
    parser.add_argument("config", help="Path to configuration file")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        logger.info("Starting Cognitive Sovereignty simulation")
        logger.info(f"Configuration: {config}")
        
        results = run_simulation(config)
        
        logger.info("Cognitive Sovereignty simulation completed")
    except Exception as e:
        logger.exception(f"An error occurred during the simulation: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()