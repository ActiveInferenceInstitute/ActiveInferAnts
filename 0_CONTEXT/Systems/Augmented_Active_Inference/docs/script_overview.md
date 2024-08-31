# Script Overview

## social_science_sim.py

Purpose: Implements a social science simulation using active inference principles and pymdp. It creates multiple agents that interact in a simulated environment, making observations, inferring states, planning actions, and updating their generative models.

Inputs:
- num_agents: Number of agents in the simulation (default: 3)
- num_steps: Number of simulation steps (default: 10)
- output_dir: Directory for output files (default: 'output')

Outputs:
- Simulation results: JSON file containing agent actions and metrics
- Visualization: PNG file showing agent actions over time
- Logs: Detailed logs of the simulation process, including agent observations, actions, and belief states

Key Functions:
- main(): Orchestrates the entire simulation process
- run_and_analyze_simulation(): Executes the simulation and performs initial analysis
- analyze_agent_behavior(): Provides insights into individual agent behaviors
- save_simulation_data(): Stores simulation results for further analysis

Usage:
python social_science_sim.py [--num_agents NUM_AGENTS] [--num_steps NUM_STEPS] [--output_dir OUTPUT_DIR]

Example:
python social_science_sim.py --num_agents 5 --num_steps 20 --output_dir results

This script utilizes the SocialAgent class and various utility functions from utils.py to create a comprehensive simulation of social interactions based on active inference principles.