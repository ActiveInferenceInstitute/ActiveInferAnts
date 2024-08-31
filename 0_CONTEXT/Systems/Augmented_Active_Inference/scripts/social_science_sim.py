import logging
from utils import run_simulation, visualize_results, calculate_metrics

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting social science simulation")
    results = run_simulation(num_agents=3, num_steps=10)
    logger.info("Simulation complete")

    visualize_results(results)
    metrics = calculate_metrics(results)
    logger.info(f"Simulation metrics: {metrics}")

if __name__ == "__main__":
    main()