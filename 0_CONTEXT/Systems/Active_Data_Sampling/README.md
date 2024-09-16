    // Start of Selection
    # Active Inference Active Data Sampling (ADS)
    
    ## Overview
    
    Active Data Sampling (ADS) is an approach to optimizing data selection based on principles from active inference and information theory. This implementation focuses on a POMDP-based active inference agent for linear regression estimation.
    
    Key features:
    
    1. Uses a generative model to predict data and quantify uncertainty
    2. Calculates expected information gain for potential data samples
    3. Selects samples that maximize information gain while considering costs
    4. Updates model beliefs after each new observation
    5. Repeats this cycle to efficiently estimate the underlying linear function
    
    ## Key Components
    
    - `POMDPActiveInferenceAgent`: Main agent class implementing the ADS algorithm
    - `Run_ActiveDataSampling.py`: Script to run simulations with different settings
    - `Methods_ActiveDataSampling.py`: Contains the core ADS implementation
    - `Visualization_ActiveDataSampling.py`: Provides visualization tools for results
    - `Analysis_ActiveDataSampling.py`: Performs analysis on simulation results
    
    ## Usage
    
    To run the complete simulation, visualization, and analysis pipeline:
    
    1. Run the simulation:
    
    ```python
    python Run_ActiveDataSampling.py
    ```
    
    2. Run the visualization:
    
    ```python
    python Visualization_ActiveDataSampling.py
    ```
    
    3. Run the analysis:
    
    ```python
    python Analysis_ActiveDataSampling.py
    ```