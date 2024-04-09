#!/bin/bash

# Active Inference Simulation in Shell

# Define the environment
environment=("state1" "state2" "state3" "state4")

# Define the agent's initial beliefs
beliefs=("0.25" "0.25" "0.25" "0.25") 

# Define the agent's preferences 
preferences=("0.1" "0.2" "0.3" "0.4")

# Define the transition probabilities
transition_probs=("0.7" "0.1" "0.1" "0.1" \
                  "0.1" "0.7" "0.1" "0.1" \
                  "0.1" "0.1" "0.7" "0.1" \
                  "0.1" "0.1" "0.1" "0.7")

# Define the number of time steps
time_steps=10

# Define the precision parameter
precision=1.0

# Function to calculate Variational Free Energy
calculate_vfe() {
    local vfe=0
    for ((i=0; i<${#environment[@]}; i++)); do
        belief=${beliefs[$i]}
        preference=${preferences[$i]}
        vfe=$(echo "$vfe - $belief * l($preference)" | bc -l)
    done
    echo "$vfe"
}

# Function to calculate Expected Free Energy
calculate_efe() {
    local efe=0
    for ((i=0; i<${#environment[@]}; i++)); do
        belief=${beliefs[$i]}
        preference=${preferences[$i]}
        
        local expected_vfe=0
        for ((j=0; j<${#environment[@]}; j++)); do
            transition_prob=${transition_probs[$((i*${#environment[@]}+j))]}
            expected_vfe=$(echo "$expected_vfe + $transition_prob * ($preference - l($belief))" | bc -l)
        done
        
        efe=$(echo "$efe + $belief * $expected_vfe" | bc -l)
    done
    echo "$efe"
}

# Run the simulation
for ((t=1; t<=time_steps; t++)); do
    echo "Time step: $t"
    
    # Perform state estimation
    for ((i=0; i<${#environment[@]}; i++)); do
        state=${environment[$i]}
        belief=${beliefs[$i]}
        preference=${preferences[$i]}
        
        # Calculate the posterior probability
        posterior=0
        for ((j=0; j<${#environment[@]}; j++)); do
            transition_prob=${transition_probs[$((i*${#environment[@]}+j))]}
            posterior=$(echo "$posterior + $belief * $transition_prob" | bc -l)
        done
        posterior=$(echo "$posterior * $preference" | bc -l)
        
        # Update the beliefs
        beliefs[$i]=$posterior
    done
    
    # Normalize the beliefs
    total_belief=$(echo "${beliefs[@]}" | tr ' ' '+' | bc -l)
    for ((i=0; i<${#beliefs[@]}; i++)); do
        beliefs[$i]=$(echo "${beliefs[$i]} / $total_belief" | bc -l)
    done
    
    # Calculate Variational Free Energy
    vfe=$(calculate_vfe)
    echo "Variational Free Energy: $vfe"
    
    # Calculate Expected Free Energy for each action
    for ((i=0; i<${#environment[@]}; i++)); do
        action=${environment[$i]}
        efe=$(calculate_efe)
        echo "Expected Free Energy for action '$action': $efe"
    done
    
    # Perform action selection based on Expected Free Energy
    min_efe=1000000
    selected_action=""
    for ((i=0; i<${#environment[@]}; i++)); do
        action=${environment[$i]}
        efe=$(calculate_efe)
        if (( $(echo "$efe < $min_efe" | bc -l) )); then
            min_efe=$efe
            selected_action=$action
        fi
    done
    
    echo "Selected action: $selected_action"
    echo "---"
done
