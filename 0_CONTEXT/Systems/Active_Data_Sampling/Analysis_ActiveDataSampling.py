# Analysis methods for Active Data Sampling

import json
import statistics
from typing import Dict, Any, List
import matplotlib.pyplot as plt
import os
import logging
import ast  # Added import

# Configure logging
def setup_logging(log_file: str):
    """
    Set up logging configuration.

    Args:
        log_file (str): Path to the log file.
    """
    logger = logging.getLogger()
    logger.handlers = []  # Clear existing handlers to ensure fresh logging configuration
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream handler (console)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

def summarize_statistics(simulation_results_path: str) -> Dict[str, Any]:
    """
    Summarize statistics from full_simulation_results.txt.

    Args:
        simulation_results_path (str): Path to the simulation results file.

    Returns:
        Dict[str, Any]: Summary statistics.
    """
    summaries = {}
    try:
        with open(simulation_results_path, 'r') as file:
            data = []
            for line_number, line in enumerate(file, 1):
                if line.strip():
                    try:
                        record = ast.literal_eval(line)
                        if isinstance(record, dict):
                            data.append(record)
                        else:
                            logging.error(f"Line {line_number}: Parsed data is not a dictionary.")
                    except Exception as e:
                        logging.error(f"Line {line_number}: Failed to parse line: {line.strip()} - {e}")
        logging.info(f"Loaded {len(data)} records from {simulation_results_path}")
    except Exception as e:
        logging.error(f"Failed to read or parse {simulation_results_path}: {e}")
        return summaries

    if not data:
        logging.warning(f"No data found in {simulation_results_path}")
        return summaries

    # Extract relevant fields
    inferred_slopes = [item['inferred_slope'] for item in data if 'inferred_slope' in item]
    costs = [item['expected_free_energy'] for item in data if 'expected_free_energy' in item]
    precisions = [item['information_gain'] for item in data if 'information_gain' in item]

    # Calculate statistics with checks
    def calculate_stats(values: List[float], key: str) -> Dict[str, float]:
        stats = {}
        if values:
            stats[f"{key}_mean"] = statistics.mean(values)
            stats[f"{key}_median"] = statistics.median(values)
            stats[f"{key}_stdev"] = statistics.stdev(values) if len(values) > 1 else 0.0
            logging.info(f"Calculated statistics for {key}")
        else:
            stats[f"{key}_mean"] = stats[f"{key}_median"] = stats[f"{key}_stdev"] = float('nan')
            logging.warning(f"No values to calculate statistics for {key}")
        return stats

    summaries.update(calculate_stats(inferred_slopes, 'inferred_slopes'))
    summaries.update(calculate_stats(costs, 'costs'))
    summaries.update(calculate_stats(precisions, 'precisions'))

    return summaries

def plot_statistics(summaries: Dict[str, Any], output_dir: str):
    """
    Plot summarized statistics.

    Args:
        summaries (Dict[str, Any]): Summary statistics.
        output_dir (str): Directory to save the plots.
    """
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"Creating plots in {output_dir}")

    # Plot Inferred Slopes
    try:
        plt.figure(figsize=(8, 6))
        plt.bar(['Mean', 'Median', 'Std Dev'], 
                [summaries.get('inferred_slopes_mean', 0), 
                 summaries.get('inferred_slopes_median', 0),
                 summaries.get('inferred_slopes_stdev', 0)],
                color=['skyblue', 'salmon', 'lightgreen'])
        plt.title('Inferred Slopes Statistics')
        plt.ylabel('Value')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'inferred_slopes_statistics.png'))
        plt.close()
        logging.info("Inferred Slopes statistics plot saved.")
    except Exception as e:
        logging.error(f"Failed to plot inferred slopes statistics: {e}")

    # Plot Costs
    try:
        plt.figure(figsize=(8, 6))
        plt.bar(['Mean', 'Median', 'Std Dev'], 
                [summaries.get('costs_mean', 0), 
                 summaries.get('costs_median', 0),
                 summaries.get('costs_stdev', 0)],
                color=['skyblue', 'salmon', 'lightgreen'])
        plt.title('Costs Statistics')
        plt.ylabel('Value')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'costs_statistics.png'))
        plt.close()
        logging.info("Costs statistics plot saved.")
    except Exception as e:
        logging.error(f"Failed to plot costs statistics: {e}")

    # Plot Precisions
    try:
        plt.figure(figsize=(8, 6))
        plt.bar(['Mean', 'Median', 'Std Dev'], 
                [summaries.get('precisions_mean', 0), 
                 summaries.get('precisions_median', 0),
                 summaries.get('precisions_stdev', 0)],
                color=['skyblue', 'salmon', 'lightgreen'])
        plt.title('Precisions Statistics')
        plt.ylabel('Value')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'precisions_statistics.png'))
        plt.close()
        logging.info("Precisions statistics plot saved.")
    except Exception as e:
        logging.error(f"Failed to plot precisions statistics: {e}")

def plot_costs_precision(simulation_results_path: str, output_dir: str):
    """
    Plot the relationship between costs and precisions.

    Args:
        simulation_results_path (str): Path to the simulation results file.
        output_dir (str): Directory to save the plot.
    """
    try:
        data = []
        with open(simulation_results_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if line.strip():
                    try:
                        record = ast.literal_eval(line)
                        if isinstance(record, dict):
                            data.append(record)
                        else:
                            logging.error(f"Line {line_number}: Parsed data is not a dictionary.")
                    except Exception as e:
                        logging.error(f"Line {line_number}: Failed to parse line: {line.strip()} - {e}")
        logging.info(f"Loaded {len(data)} records for costs vs. precisions plot.")
    except Exception as e:
        logging.error(f"Failed to read or parse {simulation_results_path}: {e}")
        return

    if not data:
        logging.warning(f"No data available to plot costs vs. precisions for {simulation_results_path}")
        return

    costs = [item['expected_free_energy'] for item in data if 'expected_free_energy' in item]
    precisions = [item['information_gain'] for item in data if 'information_gain' in item]

    if not costs or not precisions:
        logging.warning("Insufficient data to plot costs vs. precisions.")
        return

    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(costs, precisions, alpha=0.7, edgecolors='b')
        plt.title('Costs vs. Precisions')
        plt.xlabel('Costs (Expected Free Energy)')
        plt.ylabel('Precisions (Information Gain)')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'costs_vs_precisions.png'))
        plt.close()
        logging.info("Costs vs. Precisions scatter plot saved.")
    except Exception as e:
        logging.error(f"Failed to plot costs vs. precisions: {e}")

def generate_report(summaries: Dict[str, Any], output_dir: str):
    """
    Generate a textual report of the summarized statistics.

    Args:
        summaries (Dict[str, Any]): Summary statistics.
        output_dir (str): Directory to save the report.
    """
    try:
        report_path = os.path.join(output_dir, 'report.txt')
        with open(report_path, 'w') as report_file:
            report_file.write("Active Data Sampling Analysis Report\n")
            report_file.write("="*40 + "\n\n")
            for key, value in summaries.items():
                report_file.write(f"{key.replace('_', ' ').capitalize()}: {value:.4f}\n")
        logging.info(f"Report generated at {report_path}")
    except Exception as e:
        logging.error(f"Failed to generate report: {e}")

def analyze_simulation_results(simulation_results_path: str, output_dir: str, log_file: str = "Outputs/analysis_log.txt"):
    """
    Analyze simulation results by summarizing statistics, generating plots, and creating a report.

    Args:
        simulation_results_path (str): Path to the simulation results file.
        output_dir (str): Directory to save the summary, plots, and report.
        log_file (str): Path to the log file.
    """
    # Ensure output_dir is within Outputs/
    if not output_dir.startswith("Outputs/"):
        output_dir = os.path.join("Outputs", output_dir)
    
    os.makedirs(output_dir, exist_ok=True)  # Moved to before setup_logging

    setup_logging(log_file)  # Initialize logging after ensuring directories exist
    logging.info(f"Starting analysis for {simulation_results_path}")

    summaries = summarize_statistics(simulation_results_path)
    if summaries:
        plot_statistics(summaries, output_dir)
        plot_costs_precision(simulation_results_path, output_dir)
        generate_report(summaries, output_dir)

        # Save summary statistics to a JSON file
        try:
            summary_path = os.path.join(output_dir, 'summary_statistics.json')
            with open(summary_path, 'w') as f:
                json.dump(summaries, f, indent=4)
            logging.info(f"Summary statistics saved to {summary_path}")
        except Exception as e:
            logging.error(f"Failed to save summary statistics: {e}")
    else:
        logging.warning("No summaries to plot or report.")

    logging.info(f"Analysis complete. Outputs saved to {output_dir}")

def main():
    """
    Main function to analyze both 'free_' and 'cost_sensitive_' simulation results.
    Outputs are saved directly to the Outputs/ directory.
    """
    # Define simulation result files and corresponding output directories
    simulations = {
        "free_": {
            "simulation_results": "Outputs/free_/full_simulation_results.txt",
            "output_dir": "Outputs/free_/analysis",
            "log_file": "Outputs/free_/analysis_log.txt"
        },
        "cost_sensitive_": {
            "simulation_results": "Outputs/cost_sensitive_/full_simulation_results.txt",
            "output_dir": "Outputs/cost_sensitive_/analysis",
            "log_file": "Outputs/cost_sensitive_/analysis_log.txt"
        }
    }

    for name, paths in simulations.items():
        logging.info(f"Processing simulation: {name}")
        analyze_simulation_results(
            simulation_results_path=paths["simulation_results"],
            output_dir=paths["output_dir"],
            log_file=paths["log_file"]
        )

if __name__ == "__main__":
    main()
