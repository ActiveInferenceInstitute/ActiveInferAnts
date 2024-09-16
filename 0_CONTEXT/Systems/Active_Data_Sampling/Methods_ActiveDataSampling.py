import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Any, Optional
import logging
import os
import pandas as pd
from scipy import stats

class POMDPActiveInferenceAgent:
    """Agent implementing POMDP-based active inference for data sampling."""

    def __init__(
        self,
        llm_costs: List[float],
        llm_precisions: List[float],
        x_step: float = 0.01,
        output_dir: str = "Outputs/free_",
        num_timesteps: int = 100
    ) -> None:
        """
        Initialize the POMDPActiveInferenceAgent.

        Args:
            llm_costs (List[float]): Costs associated with each LLM.
            llm_precisions (List[float]): Precision values for each LLM.
            x_step (float, optional): Step size for x values. Defaults to 0.01.
            output_dir (str, optional): Directory to save outputs. Defaults to "Outputs/free_".
            num_timesteps (int, optional): Number of timesteps for simulation. Defaults to 100.
        """
        # Initialize agent attributes
        self.llms: List[str] = ['LLM_low', 'LLM_medium', 'LLM_high']
        self.costs: List[float] = llm_costs
        self.precisions: List[float] = llm_precisions
        self.x_values: np.ndarray = np.arange(0, 1.01, x_step)
        self.current_x: Optional[float] = None
        self.observations: List[Tuple[float, float]] = []
        self.inferred_slope: float = 0
        self.inferred_intercept: float = 0
        
        # For tracking performance
        self.selected_llms: List[int] = []
        self.sampled_x_values: List[float] = []

        # Initialize output directory
        self.output_dir: str = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        # Configure simulation logging
        self.simulation_logger: logging.Logger = logging.getLogger('simulation')
        self.simulation_logger.setLevel(logging.INFO)
        fh: logging.FileHandler = logging.FileHandler(os.path.join(self.output_dir, "simulation_log.txt"))
        fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s:%(message)s'))
        self.simulation_logger.addHandler(fh)

        # Initialize additional tracking attributes
        self.posterior_covs: List[float] = []  # To store posterior covariances
        self.actions: List[int] = []          # To store selected actions (LLMs)
        self.data: List[Tuple[float, float]] = []  # To store observation data
        self.cost_history: List[float] = []     # To store cost history
        self.info_gain_list: List[float] = []   # To store information gain per step
        self.expected_info_gain_history: List[float] = []  # To store expected information gain
        self.inferred_slopes: List[float] = []  # To store inferred slopes over time

        # Ensure all numpy arrays have correct dimensions and initialize num_timesteps if needed
        self.num_timesteps: int = num_timesteps

    def select_action(self) -> Tuple[int, float]:
        """Select the best action based on expected free energy."""
        best_action: Optional[Tuple[int, float]] = None
        min_free_energy: float = float('inf')

        for llm_index, llm in enumerate(self.llms):
            for x in self.x_values:
                efe: float = self.calculate_expected_free_energy(llm_index, x)
                if efe < min_free_energy:
                    min_free_energy = efe
                    best_action = (llm_index, x)

        return best_action

    def calculate_expected_free_energy(self, llm_index: int, x_value: float) -> float:
        """Calculate the expected free energy for a given action."""
        information_gain: float = self.calculate_information_gain(llm_index, x_value)
        cost: float = self.costs[llm_index]
        efe: float = -information_gain + cost
        return efe

    def sample_x(self, x_value: float) -> float:
        """Sample X value with some noise."""
        self.current_x = x_value + np.random.normal(0, 0.01)  # Add small Gaussian noise
        return self.current_x

    def query_llm(self, llm_index: int, x_value: float) -> float:
        """
        Queries the selected LLM with the given X value.

        Args:
            llm_index (int): Index of the selected LLM.
            x_value (float): The X value to query.

        Returns:
            float: The output from the LLM.
        """
        # Example implementation: replace with actual LLM query logic
        llm: str = self.llms[llm_index]
        # Simulate LLM response
        llm_output: float = llm_index * x_value + np.random.normal(0, 0.1)
        return llm_output

    def update_observations(self, x: float, y: float):
        """
        Adds a new observation to the agent's history.

        Args:
            x (float): The X value of the observation.
            y (float): The Y value of the observation.
        """
        self.observations.append((x, y))
        self.infer_regression_slope()

    def infer_regression_slope(self) -> float:
        """
        Updates and returns the inferred regression slope based on observations.

        Returns:
            float: The inferred slope.
        """
        if len(self.observations) > 1:
            x: np.ndarray = np.array([obs[0] for obs in self.observations])
            y: np.ndarray = np.array([obs[1] for obs in self.observations])
            A: np.ndarray = np.vstack([x, np.ones(len(x))]).T
            self.inferred_slope, self.inferred_intercept = np.linalg.lstsq(A, y, rcond=None)[0]
        return self.inferred_slope

    def simulate(self, num_timesteps: Optional[int] = None) -> Dict[str, Any]:
        """Run the agent simulation for a specified number of timesteps.

        Args:
            num_timesteps (Optional[int], optional): Number of timesteps to simulate. Defaults to None.

        Returns:
            Dict[str, Any]: Simulation results containing various metrics.
        """
        if num_timesteps is None:
            num_timesteps = self.num_timesteps  # Use default if not provided

        simulation_results: List[Dict[str, Any]] = []
        inferred_slopes: List[float] = []
        posterior_estimates: np.ndarray = self.compute_posterior_estimates()  # Example computation
        beliefs_history: List[Dict[str, Any]] = []  # Initialize beliefs_history
        for timestep in range(num_timesteps):
            try:
                self.simulation_logger.info(f"Starting timestep {timestep+1}.")
                print(f"Starting timestep {timestep+1}.")
                llm_index, x = self.select_action()
                sampled_x = self.sample_x(x)
                y = self.true_generative_process(sampled_x)
                llm_output = self.query_llm(llm_index, sampled_x)
                info_gain = self.calculate_information_gain(llm_index, sampled_x)
                efe = self.calculate_expected_free_energy(llm_index, sampled_x)
                self.update_observations(sampled_x, llm_output)
                inferred_slopes.append(self.inferred_slope)
                result: Dict[str, Any] = {
                    "llm_index": llm_index,
                    "x": sampled_x,
                    "y": y,
                    "llm_output": llm_output,
                    "inferred_slope": self.inferred_slope,
                    "true_slope": 2.0,  # Assuming true_slope is 2.0
                    "expected_free_energy": efe,
                    "information_gain": info_gain,
                    "inferred_slopes": inferred_slopes
                }
                simulation_results.append(result)
                self.simulation_logger.info(f"Timestep {timestep+1} completed successfully.")
                print(f"Timestep {timestep+1} completed successfully.")

                # Track additional data
                self.actions.append(llm_index)
                self.data.append((sampled_x, y))
                self.cost_history.append(self.costs[llm_index])
                self.info_gain_list.append(info_gain)
                self.expected_info_gain_history.append(efe)
                self.posterior_covs.append(self._calculate_posterior(sampled_x, y)[1])
                self.inferred_slopes.append(self.inferred_slope)

                current_belief: Dict[str, Any] = self.get_current_belief()  # Retrieve current belief
                beliefs_history.append(current_belief)     # Append to beliefs_history
            except Exception as e:
                self.simulation_logger.error(f"Timestep {timestep+1} failed: {e}")
                print(f"Timestep {timestep+1} failed: {e}")

        # Generate summary statistics after simulation
        summary_stats: Dict[str, Any] = self.generate_summary_statistics()
        
        simulation_output: Dict[str, Any] = {
            'posterior_estimates': posterior_estimates,
            'posterior_covs': self.posterior_covs,
            'simulation_results': simulation_results,
            'beliefs_history': beliefs_history,
            'actions': self.actions,
            'data': self.data,
            'cost_history': self.cost_history,
            'info_gain_list': self.info_gain_list,
            'expected_info_gain_history': self.expected_info_gain_history,
            'inferred_slopes': self.inferred_slopes,
            'summary_statistics': summary_stats
        }
        return simulation_output

    def calculate_information_gain(self, llm_index: int, x_value: float) -> float:
        """
        Calculates the expected information gain for a given LLM and X value.

        Args:
            llm_index (int): Index of the LLM.
            x_value (float): The X value.

        Returns:
            float: The information gain.
        """
        predictive_mean, predictive_var = self._calculate_predictive_distribution(x_value)
        posterior_mean, posterior_var = self._calculate_posterior(x_value, self.true_generative_process(x_value))
        kl_div = self._kl_divergence(predictive_mean, predictive_var, posterior_mean, posterior_var)
        return kl_div

    def true_generative_process(self, x: float) -> float:
        """
        Implements the true underlying linear process with added noise.

        Args:
            x (float): The X value.

        Returns:
            float: The generated Y value.
        """
        true_slope: float = 2.0
        true_intercept: float = 1.0
        noise: float = np.random.normal(0, 0.1)
        return true_slope * x + true_intercept + noise

    def visualize_results(self, simulation_results: List[Dict], output_dir: str):
        """
        Creates visualizations of the agent's performance.
        Logs the attempt and success/failure of saving visualizations.
        """
        self.simulation_logger.info("Attempting to create visualizations.")
        print("Attempting to create visualizations.")

        try:
            # Example visualization: plot inferred slope over time
            inferred_slopes: List[float] = [res["inferred_slope"] for res in simulation_results]
            plt.figure()
            plt.plot(inferred_slopes, label='Inferred Slope')
            plt.axhline(y=2.0, color='r', linestyle='--', label='True Slope')
            plt.xlabel('Timestep')
            plt.ylabel('Slope Value')
            plt.title('Inferred Regression Slope Over Time')
            plt.legend()
            plt.savefig(os.path.join(self.output_dir, 'inferred_slope.png'))
            plt.close()
            self.simulation_logger.info("Inferred slope visualization saved successfully.")
            print("Inferred slope visualization saved successfully.")
        except Exception as e:
            self.simulation_logger.error(f"Failed to save inferred slope visualization: {e}")
            print(f"Failed to save inferred slope visualization: {e}")
        
        # Add new visualizations for summary statistics
        try:
            # LLM usage pie chart
            plt.figure(figsize=(10, 6))
            llm_usage: List[int] = [res['llm_index'] for res in simulation_results]
            plt.pie([llm_usage.count(i) for i in range(len(self.llms))], labels=self.llms, autopct='%1.1f%%')
            plt.title('LLM Usage Distribution')
            plt.savefig(os.path.join(self.output_dir, 'llm_usage_distribution.png'))
            plt.close()

            # Cost and Information Gain over time
            plt.figure(figsize=(12, 6))
            timesteps: List[int] = list(range(1, len(simulation_results) + 1))
            costs: List[float] = [res['expected_free_energy'] for res in simulation_results]
            info_gains: List[float] = [res['information_gain'] for res in simulation_results]
            plt.plot(timesteps, costs, label='Cost')
            plt.plot(timesteps, info_gains, label='Information Gain')
            plt.xlabel('Timestep')
            plt.ylabel('Value')
            plt.title('Cost and Information Gain over Time')
            plt.legend()
            plt.savefig(os.path.join(self.output_dir, 'cost_info_gain_over_time.png'))
            plt.close()

            self.simulation_logger.info("Additional visualizations saved successfully.")
            print("Additional visualizations saved successfully.")
        except Exception as e:
            self.simulation_logger.error(f"Failed to save additional visualizations: {e}")
            print(f"Failed to save additional visualizations: {e}")

    # Additional utility methods
    def _calculate_posterior(self, x: float, y: float) -> Tuple[float, float]:
        """
        Calculates the posterior distribution given a new observation.

        Args:
            x (float): The X value.
            y (float): The Y value.

        Returns:
            Tuple[float, float]: Posterior mean and variance.
        """
        # Placeholder implementation
        posterior_mean: float = self.inferred_slope
        posterior_variance: float = 1.0 / self.precisions[self.llms.index('LLM_low')]
        return posterior_mean, posterior_variance

    def _calculate_predictive_distribution(self, x: float) -> Tuple[float, float]:
        """
        Calculates the predictive distribution for a given X value.

        Args:
            x (float): The X value.

        Returns:
            Tuple[float, float]: Predictive mean and variance.
        """
        predictive_mean: float = self.inferred_slope * x + self.inferred_intercept
        predictive_variance: float = 1.0 / self.precisions[self.llms.index('LLM_low')]
        return predictive_mean, predictive_variance

    def _kl_divergence(self, p_mean: float, p_var: float, q_mean: float, q_var: float) -> float:
        """
        Calculates the KL divergence between two Gaussian distributions.

        Args:
            p_mean (float): Mean of distribution P.
            p_var (float): Variance of distribution P.
            q_mean (float): Mean of distribution Q.
            q_var (float): Variance of distribution Q.

        Returns:
            float: KL divergence.
        """
        kl: float = np.log(np.sqrt(q_var) / np.sqrt(p_var)) + (p_var + (p_mean - q_mean)**2) / (2 * q_var) - 0.5
        return kl

    def compute_posterior_estimates(self) -> np.ndarray:
        """
        Example computation for posterior estimates.
        Ensures the output array has the correct shape based on num_timesteps.
        """
        return np.linspace(1.0, 3.0, self.num_timesteps)  # Generates posterior estimates matching the number of timesteps

    def generate_summary_statistics(self) -> Dict:
        """
        Generates comprehensive summary statistics for the simulation results.

        Returns:
            Dict: A dictionary containing various summary statistics.
        """
        # Convert relevant data to numpy arrays for efficient computation
        inferred_slopes: np.ndarray = np.array(self.inferred_slopes)
        actions: np.ndarray = np.array(self.actions)
        costs: np.ndarray = np.array(self.cost_history)
        info_gains: np.ndarray = np.array(self.info_gain_list)
        expected_info_gains: np.ndarray = np.array(self.expected_info_gain_history)
        
        # Basic statistics for inferred slopes
        slope_stats: Dict[str, float] = {
            'mean': np.mean(inferred_slopes),
            'median': np.median(inferred_slopes),
            'std': np.std(inferred_slopes),
            'min': np.min(inferred_slopes),
            'max': np.max(inferred_slopes),
            'q1': np.percentile(inferred_slopes, 25),
            'q3': np.percentile(inferred_slopes, 75),
            'iqr': stats.iqr(inferred_slopes),
            'skewness': stats.skew(inferred_slopes),
            'kurtosis': stats.kurtosis(inferred_slopes)
        }

        # LLM usage statistics
        llm_usage: Dict[str, int] = {llm: np.sum(actions == i) for i, llm in enumerate(self.llms)}
        llm_usage_percentage: Dict[str, float] = {llm: (count / len(actions)) * 100 for llm, count in llm_usage.items()}

        # Cost statistics
        cost_stats: Dict[str, float] = {
            'total_cost': np.sum(costs),
            'mean_cost': np.mean(costs),
            'median_cost': np.median(costs),
            'std_cost': np.std(costs),
            'min_cost': np.min(costs),
            'max_cost': np.max(costs)
        }

        # Information gain statistics
        info_gain_stats: Dict[str, float] = {
            'total_info_gain': np.sum(info_gains),
            'mean_info_gain': np.mean(info_gains),
            'median_info_gain': np.median(info_gains),
            'std_info_gain': np.std(info_gains),
            'min_info_gain': np.min(info_gains),
            'max_info_gain': np.max(info_gains)
        }

        # Expected information gain statistics
        expected_info_gain_stats: Dict[str, float] = {
            'mean_expected_info_gain': np.mean(expected_info_gains),
            'median_expected_info_gain': np.median(expected_info_gains),
            'std_expected_info_gain': np.std(expected_info_gains),
            'min_expected_info_gain': np.min(expected_info_gains),
            'max_expected_info_gain': np.max(expected_info_gains)
        }

        # Convergence metrics
        convergence_metrics: Dict[str, float] = {
            'final_slope_error': abs(inferred_slopes[-1] - 2.0),  # Assuming true slope is 2.0
            'slope_rmse': np.sqrt(np.mean((inferred_slopes - 2.0)**2)),
            'slope_mae': np.mean(np.abs(inferred_slopes - 2.0))
        }

        # Efficiency metrics
        efficiency_metrics: Dict[str, float] = {
            'info_gain_per_cost': np.sum(info_gains) / np.sum(costs),
            'avg_info_gain_per_timestep': np.mean(info_gains),
            'avg_cost_per_timestep': np.mean(costs)
        }

        return {
            'slope_statistics': slope_stats,
            'llm_usage': llm_usage,
            'llm_usage_percentage': llm_usage_percentage,
            'cost_statistics': cost_stats,
            'info_gain_statistics': info_gain_stats,
            'expected_info_gain_statistics': expected_info_gain_stats,
            'convergence_metrics': convergence_metrics,
            'efficiency_metrics': efficiency_metrics
        }

    def get_current_belief(self) -> Dict[str, Any]:
        """
        Retrieves the current belief state.

        Returns:
            Dict[str, Any]: A dictionary containing the current belief state.
        """
        # Placeholder implementation
        return {
            'mean': self.inferred_slope,
            'cov': self.posterior_covs[-1] if self.posterior_covs else None
        }

# Example usage
if __name__ == "__main__":
    import json

    # Initialize agent
    llm_costs: List[float] = [1, 2, 3]
    llm_precisions: List[float] = [1, 5, 10]
    output_dir: str = "Outputs/free_"
    agent: POMDPActiveInferenceAgent = POMDPActiveInferenceAgent(llm_costs, llm_precisions, output_dir=output_dir)

    # Run simulation
    num_timesteps: int = 100
    simulation_results: Dict[str, Any] = agent.simulate(num_timesteps)

    # Save summary statistics
    summary_path: str = os.path.join(agent.output_dir, "summary_statistics.txt")
    try:
        with open(summary_path, 'w') as f:
            json.dump(simulation_results['summary_statistics'], f, indent=2)
        print(f"Summary statistics saved to {summary_path}")
    except Exception as e:
        agent.simulation_logger.error(f"Failed to save summary statistics: {e}")
        print(f"Failed to save summary statistics: {e}")

    # Print summary statistics
    print("Summary Statistics:")
    print(json.dumps(simulation_results['summary_statistics'], indent=2))
        