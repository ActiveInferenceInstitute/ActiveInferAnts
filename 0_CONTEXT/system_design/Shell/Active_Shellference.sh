#!/bin/bash

# Active Inference Simulation in Shell

# Define the environment, agent's initial beliefs, preferences, and transition probabilities
declare -A simulation=(
    [environment]="state1 state2 state3 state4"
    [beliefs]="0.25 0.25 0.25 0.25"
    [preferences]="0.1 0.2 0.3 0.4"
    [transition_probs]="0.7 0.1 0.1 0.1 0.1 0.7 0.1 0.1 0.1 0.1 0.7 0.1 0.1 0.1 0.1 0.7"
)

# Define the number of time steps and the precision parameter
time_steps=10
precision=1.0

# Function to calculate Variational Free Energy
calculate_vfe() {
    local vfe=0
    read -ra beliefs <<< "${simulation[beliefs]}"
    read -ra preferences <<< "${simulation[preferences]}"
    for i in "${!beliefs[@]}"; do
        vfe=$(echo "$vfe - ${beliefs[$i]} * l(${preferences[$i]})" | bc -l)
    done
    echo "$vfe"
}

# Function to calculate Expected Free Energy
calculate_efe() {
    local efe=0
    read -ra beliefs <<< "${simulation[beliefs]}"
    read -ra preferences <<< "${simulation[preferences]}"
    read -ra transition_probs <<< "${simulation[transition_probs]}"
    local env_size=${#beliefs[@]}
    
    for i in "${!beliefs[@]}"; do
        local expected_vfe=0
        for j in "${!beliefs[@]}"; do
            local idx=$((i * env_size + j))
            expected_vfe=$(echo "$expected_vfe + ${transition_probs[$idx]} * (${preferences[$j]} - l(${beliefs[$i]}))" | bc -l)
        done
        efe=$(echo "$efe + ${beliefs[$i]} * $expected_vfe" | bc -l)
    done
    echo "$efe"
}

# Run the simulation
for ((t=1; t<=time_steps; t++)); do
    echo "Time step: $t"
    
    # Perform state estimation and update beliefs
    read -ra beliefs <<< "${simulation[beliefs]}"
    read -ra environment <<< "${simulation[environment]}"
    read -ra preferences <<< "${simulation[preferences]}"
    read -ra transition_probs <<< "${simulation[transition_probs]}"
    local env_size=${#environment[@]}
    local updated_beliefs=()
    
    for i in "${!environment[@]}"; do
        local posterior=0
        for j in "${!environment[@]}"; do
            local idx=$((i * env_size + j))
            posterior=$(echo "$posterior + ${beliefs[$i]} * ${transition_probs[$idx]}" | bc -l)
        done
        posterior=$(echo "$posterior * ${preferences[$i]}" | bc -l)
        updated_beliefs+=($posterior)
    done
    
    # Normalize the beliefs
    local total_belief=$(IFS=+; echo "${updated_beliefs[*]}" | bc -l)
    for i in "${!updated_beliefs[@]}"; do
        updated_beliefs[$i]=$(echo "${updated_beliefs[$i]} / $total_belief" | bc -l)
    done
    simulation[beliefs]="${updated_beliefs[*]}"
    
    # Calculate Variational Free Energy
    vfe=$(calculate_vfe)
    echo "Variational Free Energy: $vfe"
    
    # Calculate and select action based on Expected Free Energy
    local min_efe=1000000
    local selected_action=""
    for action in "${environment[@]}"; do
        efe=$(calculate_efe)
        if (( $(echo "$efe < $min_efe" | bc -l) )); then
            min_efe=$efe
            selected_action=$action
        fi
    done
    
    echo "Selected action: $selected_action"
    echo "---"
done
