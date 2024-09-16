    # Active Inference Active Data Sampling (ADS)
    
    ## Overview
    
    Active Data Sampling (ADS) is a comprehensive framework designed to optimize data selection processes by leveraging principles from active inference and information theory. This implementation utilizes a Partially Observable Markov Decision Process (POMDP)-based active inference agent tailored for linear regression estimation.
    
    ## Features
    
    - **Generative Modeling**: Employs a generative model to predict data points and quantify associated uncertainties.
    - **Information Gain Calculation**: Computes the expected information gain for potential data samples to prioritize high-value acquisitions.
    - **Cost-Sensitive Sampling**: Balances information gain against sampling costs to make efficient data selection decisions.
    - **Dynamic Belief Updates**: Continuously updates model beliefs in response to new observations, enhancing estimation accuracy over time.
    - **Iterative Estimation Cycle**: Repeats the cycle of sampling, updating, and estimation to progressively refine the underlying linear function estimation.
    
    ## Key Components
    
    - **`POMDPActiveInferenceAgent`**: The core agent class implementing the ADS algorithm, responsible for data prediction, sampling decisions, and belief updates.
    - **`Run_ActiveDataSampling.py`**: Script to execute simulations under various settings, managing the simulation workflow, and output generation.
    - **`Methods_ActiveDataSampling.py`**: Contains the foundational implementation of the ADS algorithm, including data generation, model updates, and decision-making mechanisms.
    - **`Visualization_ActiveDataSampling.py`**: Provides tools for visualizing simulation results, such as posterior estimates, inferred slopes, and information gain metrics.
    - **`Analysis_ActiveDataSampling.py`**: Performs in-depth analysis of simulation results, summarizing statistics, generating plots, and compiling comprehensive reports.
    
    ## Installation
    
    ### Prerequisites
    
    - Python 3.7 or higher
    - Required Python packages:
      - `numpy`
      - `matplotlib`
      - `logging`
      - `json`
    
    ### Installation Steps
    
    1. **Clone the Repository**
    
        ```bash
        git clone https://github.com/yourusername/active-data-sampling.git
        cd active-data-sampling
        ```
    
    2. **Install Dependencies**
    
        ```bash
        pip install -r requirements.txt
        ```
    
        *Ensure that `requirements.txt` includes all necessary packages.*
    
    ## Usage
    
    The ADS pipeline consists of three main stages: Simulation, Visualization, and Analysis. Follow the steps below to execute the complete workflow.
    
    ### 1. Run the Simulation
    
    Execute the simulation script to perform active data sampling under predefined settings.
    
    ```bash
    python Run_ActiveDataSampling.py
    ```
    
    **What It Does:**
    
    - Initializes the ADS agent with different configurations (e.g., `free_`, `cost_sensitive_`).
    - Runs simulations for a specified number of timesteps.
    - Saves simulation results and logs in the `Outputs` directory.
    
    ### 2. Generate Visualizations
    
    After completing the simulations, generate visualizations to interpret the results.
    
    ```bash
    python Visualization_ActiveDataSampling.py
    ```
    
    **What It Does:**
    
    - Loads simulation results from the `Outputs` directory.
    - Creates visual plots for posterior estimates, inferred slopes, information gain, and more.
    - Saves visualization figures in respective output subdirectories.
    
    ### 3. Perform Analysis
    
    Analyze the simulation results to extract meaningful insights and statistical summaries.
    
    ```bash
    python Analysis_ActiveDataSampling.py
    ```
    
    **What It Does:**
    
    - Summarizes statistics from simulation results, including means, medians, and standard deviations.
    - Generates plots for summarized statistics and relationships between costs and precisions.
    - Compiles a textual report of the analysis findings.
    
    ## Example
    
    Upon successful execution of the simulation, visualization, and analysis scripts, the `Outputs` directory will contain subdirectories for each setting (e.g., `free_`, `cost_sensitive_`). Each subdirectory includes:
    
    - `full_simulation_results.txt`: Raw simulation data.
    - Visualization figures (e.g., `visualization_facet.png`).
    - Analysis outputs, including summary statistics, plots, and reports.
    
    ## Contributing
    
    Contributions are welcome! Please fork the repository and submit a pull request with your enhancements. Ensure that your contributions adhere to the project's coding standards and include appropriate documentation.
    
    ## License
    
    This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
    
    ## Contact
    
    For any questions or suggestions, please open an issue on the [GitHub repository](https://github.com/yourusername/active-data-sampling) or contact [your.email@example.com](mailto:your.email@example.com).