import matplotlib.pyplot as plt
import numpy as np
import logging
from typing import List, Dict, Any, Optional, Tuple
import os  # Added import

def visualize_sampling(
    posterior_estimates: np.ndarray,
    sampled_points: np.ndarray,
    posterior_covs: np.ndarray,
    actions: List[int],
    data: List[float],
    cost_history: List[float],
    info_gain_list: List[float],
    expected_info_gain_history: List[float],
    mode: str,
    inferred_slopes: List[float],
    beliefs_history: List[Dict[str, Any]]
) -> Optional[plt.Figure]:
    """Generate visualizations for active data sampling.

    Args:
        posterior_estimates (np.ndarray): Array of posterior estimates.
        sampled_points (np.ndarray): Array of sampled points.
        posterior_covs (np.ndarray): Array of posterior covariances.
        actions (List[int]): List of actions taken.
        data (List[float]): List of observed data points.
        cost_history (List[float]): List of costs incurred.
        info_gain_list (List[float]): List of information gains.
        expected_info_gain_history (List[float]): List of expected information gains.
        mode (str): Current mode of simulation.
        inferred_slopes (List[float]): List of inferred slopes over time.
        beliefs_history (List[Dict[str, Any]]): History of beliefs.

    Returns:
        Optional[plt.Figure]: The generated matplotlib figure or None if failed.
    """
    logging.info(f"Starting visualization for mode: {mode}")
    
    if not isinstance(beliefs_history, list):
        beliefs_history = [beliefs_history]
    
    # Log the number of beliefs_history entries before filtering
    logging.debug(f"Original beliefs_history length: {len(beliefs_history)}")
    logging.debug(f"Original beliefs_history content: {beliefs_history}")
    
    # Ensure beliefs_history is a list of valid dictionaries
    beliefs_history = [
        belief for belief in beliefs_history
        if belief is not None and 'mean' in belief and 'cov' in belief
    ]
    
    # Log the number of beliefs_history entries after filtering
    logging.debug(f"Filtered beliefs_history length: {len(beliefs_history)}")
    logging.debug(f"Filtered beliefs_history content: {beliefs_history}")
    
    if not beliefs_history:
        logging.error("No valid 'beliefs_history' data to process.")
        return None  # Return None instead of empty list
    
    logging.debug("Visualize_sampling called with:")
    logging.debug(f"posterior_estimates shape: {posterior_estimates.shape}")
    logging.debug(f"sampled_points shape: {sampled_points.shape}")
    logging.debug(f"posterior_covs shape: {posterior_covs.shape}")
    logging.debug(f"actions length: {len(actions)}")
    logging.debug(f"data length: {len(data)}")
    logging.debug(f"cost_history length: {len(cost_history)}")
    logging.debug(f"info_gain_list length: {len(info_gain_list)}")
    
    # Determine prefix based on mode
    prefix = 'free_' if mode == 'free_' else 'cost_sensitive_'
    
    # Convert beliefs_history to a hashable type with type checks
    beliefs_history_hashable = [
        (
            tuple(belief['mean']) if isinstance(belief['mean'], (list, tuple, np.ndarray)) else (belief['mean'],),
            tuple(tuple(row) for row in belief['cov']) if isinstance(belief['cov'], (list, tuple, np.ndarray)) else ((belief['cov'],),)
        )
        for belief in beliefs_history
    ]
    
    # Convert lists to numpy arrays for easier manipulation
    actions_history = np.array(actions)
    data_history = np.array(data)
    cost_history = np.array(cost_history)
    info_gain_list = np.array(info_gain_list)
    expected_info_gain_history = np.array(expected_info_gain_history)
    sampled_points = np.array(sampled_points)
    
    # Ensure posterior_estimates and posterior_covs have the same length
    if len(posterior_estimates) != len(posterior_covs):
        logging.error(
            f"Length mismatch: posterior_estimates({len(posterior_estimates)}) vs "
            f"posterior_covs({len(posterior_covs)})"
        )
        return None  # Return None instead of empty list
    
    # Extract scalar covariance (standard deviation) per timestep from beliefs_history
    posterior_covs = np.array([
        np.sqrt(np.trace(belief['cov'])) if isinstance(belief['cov'], np.ndarray) and belief['cov'].ndim == 2
        else np.sqrt(belief['cov']) if isinstance(belief['cov'], (int, float, np.number))
        else 0.0  # Default value for unexpected formats
        for belief in beliefs_history
    ])  # Updated to handle covariances with different dimensions
    
    # Extract mean and covariance from beliefs_history_hashable
    belief_means = np.array([belief[0] for belief in beliefs_history_hashable])
    belief_covs = np.array([belief[1] for belief in beliefs_history_hashable])
    
    # Create output directories if they don't exist
    os.makedirs(os.path.join("Outputs", mode), exist_ok=True)
    
    # Generate a single faceted figure with multiple subplots
    try:
        fig, axs = plt.subplots(3, 1, figsize=(15, 18), constrained_layout=True)
        
        # Subplot 1: Posterior Estimates with Real Underlying Value and Samples
        axs[0].plot(posterior_estimates, label='Posterior Estimates', color='blue')
        axs[0].fill_between(
            range(len(posterior_estimates)),
            posterior_estimates - posterior_covs,
            posterior_estimates + posterior_covs,
            color='blue',
            alpha=0.2,
            label='Confidence Interval'
        )
        axs[0].plot(data_history, label='Real Underlying Value', color='red', linestyle='--')
        if sampled_points.size > 0:
            axs[0].scatter(range(len(sampled_points)), sampled_points, color='green', label='Sampled Points')
        axs[0].set_title(f'Posterior Estimates vs Real Value - {mode}')
        axs[0].set_xlabel('Timestep')
        axs[0].set_ylabel('Value')
        axs[0].legend()
        
        # Subplot 2: Inferred Slopes
        axs[1].plot(inferred_slopes, label='Inferred Slopes', color='green')
        axs[1].set_title(f'Inferred Slopes Over Time - {mode}')
        axs[1].set_xlabel('Timestep')
        axs[1].set_ylabel('Slope')
        axs[1].legend()
        
        # Subplot 3: Information Gain
        axs[2].plot(info_gain_list, label='Information Gain', color='purple')
        axs[2].set_title(f'Information Gain Over Time - {mode}')
        axs[2].set_xlabel('Timestep')
        axs[2].set_ylabel('Information Gain')
        axs[2].legend()
        
        logging.info(f"Faceted figure generated successfully for mode '{mode}'.")
        return fig  # Return the single faceted figure
    
    except Exception as e:
        logging.error(f"Failed to generate faceted figure for mode '{mode}': {e}")
        return None  # Return None if figure generation fails
