# Active Inference Implementation in Shell

This directory contains a POSIX shell implementation of active inference demonstrating system integration and command-line processing capabilities.

## Overview

The Shell implementation provides:
- System-level active inference simulation
- Command-line interface for parameter control
- File-based data persistence
- Integration with system utilities

## Core Components

- **Active_Shellference.sh**: Main active inference implementation
- **config.sh**: Configuration file for simulation parameters

## Architecture

### Shell-Specific Design
The implementation leverages shell scripting features:

- **Pipes and Redirection**: Data flow between processing stages
- **Process Substitution**: Concurrent belief updates
- **Command Substitution**: Dynamic parameter evaluation
- **Arrays and Variables**: State and belief representation

### Simulation Structure
```bash
# Belief state as array
beliefs=(0.25 0.25 0.25 0.25)

# Generative model matrices
declare -A a_matrix  # Likelihood P(o|s)
declare -A b_matrix  # Transition P(s'|s,a)

# Configuration parameters
precision=1.0
learning_rate=0.1
time_steps=100
```

## Dependencies

- POSIX-compliant shell (bash, zsh, dash)
- Standard Unix utilities:
  - `bc`: Arbitrary precision calculator
  - `awk`: Text processing and calculations
  - `sed`: Stream editor for data manipulation
  - `grep`: Pattern matching
  - `sort`: Data sorting
  - `uniq`: Unique value extraction

## Configuration

The simulation is configured through `config.sh`:

```bash
# Simulation parameters
CONFIG_ENVIRONMENT=("food" "danger" "safe")
CONFIG_INITIAL_BELIEFS=("0.25" "0.25" "0.25" "0.25")
CONFIG_PREFERENCES=("1.0" "0.0" "0.5")
CONFIG_TRANSITION_PROBS=("0.9" "0.1" "0.1" "0.8" "0.1" "0.9")
CONFIG_TIME_STEPS=100
CONFIG_PRECISION=4

# Output configuration
CONFIG_OUTPUT_FILE="simulation_results.txt"
CONFIG_LOG_LEVEL="INFO"
```

## Core Algorithms

### Belief Update Algorithm
```bash
calculate_kl_divergence() {
    local kl_divergence=0
    local i=0

    for belief in "${beliefs[@]}"; do
        local preference=${preferences[$i]}
        kl_divergence=$(echo "scale=$precision; $kl_divergence + $belief * (l($belief) - l($preference))" | bc -l)
        ((i++))
    done

    echo "$kl_divergence"
}
```

### Variational Free Energy
```bash
calculate_vfe() {
    local vfe
    vfe=$(calculate_kl_divergence)
    echo "$vfe"
}
```

### Action Selection
```bash
select_action() {
    local min_efe=1000000
    local selected_action=""

    for action in "${environment[@]}"; do
        local efe
        efe=$(calculate_efe)
        if (( $(echo "$efe < $min_efe" | bc -l) )); then
            min_efe=$efe
            selected_action=$action
        fi
    done

    echo "$selected_action"
}
```

## Running the Implementation

```bash
# Basic simulation
./Active_Shellference.sh

# With custom configuration
CONFIG_TIME_STEPS=50 ./Active_Shellference.sh

# With output redirection
./Active_Shellference.sh > results.txt

# With debugging
bash -x ./Active_Shellference.sh
```

## Data Flow Architecture

### Pipeline Processing
```bash
# Generate observations
generate_observation() {
    # Random observation generation
    echo $((RANDOM % 3))
}

# Process through pipeline
observation=$(generate_observation)
beliefs_updated=$(update_beliefs "$observation")
action_selected=$(select_action "$beliefs_updated")
```

### File-Based Persistence
```bash
# Save simulation state
save_state() {
    cat > "$CONFIG_OUTPUT_FILE" << EOF
Time Step: $current_step
Beliefs: ${beliefs[*]}
Action: $selected_action
Free Energy: $current_vfe
EOF
}

# Load previous state
load_state() {
    if [[ -f "$CONFIG_OUTPUT_FILE" ]]; then
        source "$CONFIG_OUTPUT_FILE"
    fi
}
```

## Performance Characteristics

### Shell Script Optimization
- **Minimal Resource Usage**: Lightweight process execution
- **System Integration**: Direct access to system utilities
- **Text Processing**: Efficient log and data processing
- **Automation**: Cron job and script integration

### Limitations and Workarounds
- **Precision**: Using `bc` for floating-point arithmetic
- **Arrays**: Indexed arrays for state representation
- **Performance**: External utilities for complex calculations
- **Memory**: File-based persistence for large simulations

## Output and Analysis

The implementation generates:
- Real-time console output with belief states
- File-based logs of simulation progress
- Performance metrics and timing information
- Formatted reports for analysis

## Extensions

### Advanced Features
- **Distributed Processing**: Multiple shell processes coordination
- **Real-time Monitoring**: Integration with system monitoring tools
- **Web Interface**: CGI integration for web-based control
- **Database Integration**: SQL database for result storage

### Integration Options
- **System Administration**: Server monitoring and automation
- **DevOps**: CI/CD pipeline integration
- **Data Processing**: Log analysis and processing
- **Network Management**: Configuration management

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Shell Resources
1. **POSIX Shell Programming**: Standard shell scripting
2. **Advanced Bash Scripting Guide**: Comprehensive bash techniques
3. **Shell Command Language**: POSIX standard specification
