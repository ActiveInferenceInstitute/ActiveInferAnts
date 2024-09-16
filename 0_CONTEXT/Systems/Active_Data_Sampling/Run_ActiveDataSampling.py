import numpy as np
from Methods_ActiveDataSampling import POMDPActiveInferenceAgent
import os
import logging 
import Visualization_ActiveDataSampling as viz
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg') 

num_timesteps = 50 

# Create Outputs directory if it doesn't exist
os.makedirs("Outputs", exist_ok=True)

# Professionalized logging configuration with logger name
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(os.path.join("Outputs", "log.txt"))
formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def main() -> None:
    """Run the active data sampling simulation for different settings."""
    # Create Outputs directory if it doesn't exist
    os.makedirs("Outputs", exist_ok=True)
    
    logger.info("Starting active data sampling simulation.")
    print("Starting active data sampling simulation.")

    # Define different settings
    settings = {
        "free_": {
            "llm_costs": [1] * num_timesteps,
            "llm_precisions": [1] * num_timesteps,
            "output_subdir": "free_"
        },
        "cost_sensitive_": {
            "llm_costs": [1, 2, 3, 4, 5] * (num_timesteps // 5),
            "llm_precisions": [1, 2, 3, 4, 5] * (num_timesteps // 5), 
            "output_subdir": "cost_sensitive_"
        }
    }
    
    for setting, params in settings.items():
        # Create subdirectory for the setting
        setting_dir = os.path.join("Outputs", params["output_subdir"])  # Use output_subdir from params
        os.makedirs(setting_dir, exist_ok=True)
    
        logger.info(f"Running simulation for setting: {setting}")
        print(f"Running simulation for setting: {setting}")
    
        # Initialize agent with current setting
        agent = POMDPActiveInferenceAgent(
            llm_costs=params["llm_costs"],
            llm_precisions=params["llm_precisions"],
            output_dir=setting_dir  # Pass the specific output subdirectory
        )
    
        # Execute the simulation using the predefined num_timesteps
        simulation_output = agent.simulate(num_timesteps=num_timesteps)
        
        # Define beliefs_history from simulation_output
        beliefs_history = simulation_output.get('beliefs_history')  # Removed np.array wrapping
        
        # Added check for beliefs_history
        if beliefs_history is None:
            logger.error(f"'beliefs_history' is missing in simulation_output for setting {setting}.")
            print(f"'beliefs_history' is missing in simulation_output for setting {setting}. Skipping visualization.")
            continue  # Skip visualization
        
        # **Correct Extraction of posterior_estimates from beliefs_history**
        posterior_estimates = np.array([belief['mean'] for belief in beliefs_history])  # Added correct extraction
        
        # **Extract 'y' values from simulation data to match timesteps**
        # data = np.array(simulation_output.get('data'))  # Removed incorrect extraction
        data_history = [d[1] for d in simulation_output.get('data')]  # Extract only 'y' values
        
        posterior_covs = np.array(simulation_output.get('posterior_covs'))  # Define posterior_covs
        simulation_results = simulation_output.get('simulation_results')  # Define simulation_results

        # Convert lists to NumPy arrays
        actions = np.array(simulation_output.get('actions'))
        # data = np.array(simulation_output.get('data'))  # Removed incorrect extraction
        cost_history = np.array(simulation_output.get('cost_history'))
        info_gain_list = np.array(simulation_output.get('info_gain_list'))
        expected_info_gain_history = np.array(simulation_output.get('expected_info_gain_history'))
        inferred_slopes = np.array(simulation_output.get('inferred_slopes'))
        sampled_points = np.array(agent.sampled_x_values)
        
        logger.info(f"Simulation for {setting} completed successfully.")
        print(f"Simulation for {setting} completed successfully.")
    
        # Save full simulation results to a text file
        results_path = os.path.join(setting_dir, "full_simulation_results.txt")
        try:
            with open(results_path, 'w') as f:
                for result in simulation_results:
                    f.write(f"{result}\n")  # Updated to use simulation_results
            logger.info(f"Full simulation results saved to {results_path}.")
            print(f"Full simulation results saved to {results_path}.")
        except Exception as e:
            logger.error(f"Saving full simulation results failed for {setting}: {e}")
            print(f"Failed to save full simulation results for {setting}: {e}")
        
        # **New Addition: Call Visualization with Enhanced Logging and Single Faceted Figure**
        try:
            logger.info(f"Attempting to generate visualizations for setting: {setting}")
            print(f"Attempting to generate visualizations for setting: {setting}")
            
            fig = viz.visualize_sampling(
                posterior_estimates=posterior_estimates,
                sampled_points=sampled_points,
                posterior_covs=posterior_covs,
                actions=actions,
                data=data_history,  # Pass the extracted y-values
                cost_history=cost_history,
                info_gain_list=info_gain_list,
                expected_info_gain_history=expected_info_gain_history,
                mode=setting,
                inferred_slopes=inferred_slopes,
                beliefs_history=beliefs_history
            )
            
            if fig is not None:
                fig_path = os.path.join(setting_dir, f"visualization_facet.png")
                fig.savefig(fig_path)
                logger.info(f"Faceted visualization saved to {fig_path}.")
                print(f"Faceted visualization saved to {fig_path}.")
                plt.close(fig)
            else:
                logger.warning(f"No figures were generated for setting '{setting}'.")
                print(f"No figures were generated for setting '{setting}'.")
        except Exception as e:
            logger.error(f"Visualization failed for setting '{setting}': {e}")
            print(f"Visualization failed for setting '{setting}': {e}")
    
    logger.info("All simulations completed.")
    print("All simulations completed.")

if __name__ == "__main__":
    main()