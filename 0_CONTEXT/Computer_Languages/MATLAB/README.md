# Active Inference Implementation in MATLAB/Octave

This directory contains a comprehensive implementation of the Active Inference framework using MATLAB or GNU Octave.

## Overview

The MATLAB/Octave implementation provides:

- **Object-oriented design** using MATLAB classes
- **Matrix-based computations** leveraging MATLAB's linear algebra capabilities
- **Visualization tools** for belief evolution and analysis
- **Statistical analysis** of agent behavior
- **Flexible parameter configuration**

## Files

- `ActiveInferenceAgent.m` - Main agent class implementation
- `demo.m` - Demonstration script showing agent behavior
- `run.sh` - Cross-platform runner for MATLAB/Octave
- `README.md` - This documentation

## Features

### Core Active Inference Components

1. **Generative Model**:
   - A-matrix: Observation likelihood P(o|s)
   - B-matrix: State transitions P(s'|s,a)
   - C-vector: Observation preferences P(o)
   - D-vector: Prior beliefs P(s)

2. **Inference Engine**:
   - Bayesian belief updating
   - Expected free energy calculation
   - Action selection via EFE minimization
   - Learning from experience

3. **Analysis Tools**:
   - Belief evolution plotting
   - Statistical analysis
   - Entropy calculation
   - Performance metrics

## Usage

### Basic Example

```matlab
% Create agent with 3 states, 3 observations, 2 actions
agent = ActiveInferenceAgent(3, 3, 2);

% Run simulation
for step = 1:10
    observation = randi(3);  % Random observation
    [agent, action] = agent.step(observation);

    fprintf('Step %d: Obs=%d, Action=%d\n', step, observation, action);
end

% Display results
agent.printStatistics();
agent.plotBeliefs();
```

### Advanced Configuration

```matlab
% Create agent with custom parameters
agent = ActiveInferenceAgent(4, 3, 3, ...
    'precision', 2.0, ...
    'learning_rate', 0.2);

% Run learning simulation
for trial = 1:100
    % Learning loop with teacher signal
    observation = generate_observation();
    [agent, action] = agent.step(observation);

    % Learn from experience
    next_observation = generate_observation();
    agent = agent.learn(observation, action, next_observation);
end
```

## Requirements

### MATLAB
- MATLAB R2018b or later
- Statistics and Machine Learning Toolbox (recommended)

### GNU Octave
- Octave 5.0 or later
- Statistics package (optional)

## Installation

1. **MATLAB**:
   ```bash
   # No installation required - just ensure MATLAB is in PATH
   ```

2. **Octave**:
   ```bash
   # Ubuntu/Debian
   sudo apt-get install octave octave-statistics

   # macOS
   brew install octave
   ```

## Running the Demo

### Automatic (Cross-platform)
```bash
./run.sh
```

### Manual

**MATLAB:**
```bash
matlab -batch "demo"
```

**Octave:**
```bash
octave --no-gui demo.m
```

## Algorithm Details

### Belief Updating
```matlab
% Bayesian inference: P(s|o) ∝ P(o|s) * P(s)
likelihood = A_matrix(observation, :)';
posterior = likelihood .* beliefs;
beliefs = posterior / sum(posterior);
```

### Action Selection
```matlab
% Minimize expected free energy
for action = 1:n_actions
    predicted_beliefs = predictBeliefs(action);
    efe = calculateExpectedFreeEnergy(predicted_beliefs);
    if efe < min_efe
        best_action = action;
    end
end
```

### Learning
```matlab
% Simple reinforcement learning
[max_state, ~] = max(beliefs);
A_matrix(observation, max_state) = A_matrix(observation, max_state) + learning_rate;
A_matrix(observation, :) = A_matrix(observation, :) / sum(A_matrix(observation, :));
```

## Performance Characteristics

- **Initialization**: O(n_states × n_observations × n_actions)
- **Belief Update**: O(n_states)
- **Action Selection**: O(n_actions × n_states²)
- **Memory Usage**: O(n_states × n_observations × n_actions)

## Visualization

The implementation includes plotting capabilities for:

- **Belief Evolution**: Track how beliefs change over time
- **Free Energy**: Monitor the variational free energy
- **Action Distribution**: Analyze action selection patterns

```matlab
agent.plotBeliefs('Custom Title');
```

## Extension Points

### Custom Generative Models
```matlab
classdef CustomAgent < ActiveInferenceAgent
    methods
        function obj = initializeGenerativeModel(obj)
            % Custom generative model initialization
            obj.A_matrix = custom_likelihood_matrix();
            obj.B_matrix = custom_transition_matrix();
            % ... etc
        end
    end
end
```

### Multi-Agent Simulations
```matlab
% Create multiple agents
agents = cell(1, n_agents);
for i = 1:n_agents
    agents{i} = ActiveInferenceAgent(3, 3, 2);
end

% Run multi-agent simulation
for t = 1:100
    for i = 1:n_agents
        observation = get_observation_from_environment(i);
        [agents{i}, action] = agents{i}.step(observation);
        execute_action_in_environment(i, action);
    end
end
```

## References

- **Active Inference**: Friston, K. (2010). The free-energy principle
- **MATLAB Matrix Operations**: MATLAB Documentation
- **Bayesian Inference**: Bishop, C. M. (2006). Pattern Recognition and Machine Learning

## Troubleshooting

### Common Issues

1. **Plotting Errors**: Ensure graphics toolkit is available in Octave
   ```octave
   graphics_toolkit("gnuplot")
   ```

2. **Memory Issues**: For large state spaces, consider reducing dimensions
   ```matlab
   agent = ActiveInferenceAgent(5, 5, 3);  % Smaller dimensions
   ```

3. **Performance**: For real-time applications, pre-allocate arrays
   ```matlab
   belief_history = zeros(n_states, max_steps);
   ```

## License

This implementation is provided under the MIT License. See the main repository for full license details.
