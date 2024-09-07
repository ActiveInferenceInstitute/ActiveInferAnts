import subprocess
import logging
import sys
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_script(script_name, *args):
    logger.info(f"Running {script_name}")
    command = [sys.executable, script_name] + list(args)
    process = subprocess.Popen(command, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT,
                               text=True,
                               bufsize=1,
                               universal_newlines=True)
    
    for line in process.stdout:
        print(line, end='')  # Print each line of output in real-time
    
    process.wait()
    
    if process.returncode != 0:
        logger.error(f"Error running {script_name}. Exit code: {process.returncode}")
        sys.exit(1)

def main():
    logger.info("Starting Cognitive Sovereignty simulation process")

    # Run 1_generate_entity_library.py
    run_script("1_generate_entity_library.py")

    # Run 2_cognitive_sovereignty_simulation.py with config file
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    run_script("2_cognitive_sovereignty_simulation.py", config_path)

    # Run 3_simulation_analysis.py with config file
    run_script("3_simulation_analysis.py", config_path)

    logger.info("Cognitive Sovereignty simulation process completed")

if __name__ == "__main__":
    main()
