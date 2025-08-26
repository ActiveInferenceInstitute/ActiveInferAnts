# Active Inference Implementation in Ruby

This directory contains a comprehensive implementation of the Active Inference framework using Ruby's elegant object-oriented design and dynamic capabilities.

## Overview

The Ruby implementation provides:

- **Object-oriented design** using Ruby's class system and mixins
- **Array-based matrix operations** for generative model computations
- **Dynamic method definition** for flexible agent behavior
- **Comprehensive testing** with RSpec support
- **Multi-agent simulation** capabilities

## Files

- `active_inference_agent.rb` - Main agent class with complete active inference algorithm
- `run.sh` - Cross-platform runner script with version checking
- `README.md` - This documentation

## Features

### Core Active Inference Components

1. **Generative Model**:
   - A-matrix: Observation likelihood P(o|s)
   - B-matrix: State transitions P(s'|s,a)
   - C-vector: Observation preferences P(o)
   - D-vector: Prior beliefs P(s)

2. **Inference Engine**:
   - Bayesian belief updating using array operations
   - Expected free energy calculation
   - Action selection via EFE minimization
   - Learning from experience

3. **Analysis Tools**:
   - Belief entropy calculation
   - Statistical analysis
   - History tracking
   - Performance metrics

## Usage

### Basic Example

```ruby
# Create agent with 3 states, 3 observations, 2 actions
agent = ActiveInferenceAgent.new(
  n_states: 3,
  n_observations: 3,
  n_actions: 2,
  precision: 1.0,
  learning_rate: 0.1
)

# Run simulation
10.times do |step|
  observation = rand(3)  # Random observation
  action = agent.step(observation)

  puts "Step #{step + 1}: Obs=#{observation}, Action=#{action}"
  puts "Beliefs: [#{agent.get_beliefs.map { |b| format('%.3f', b) }.join(', ')}]"
end

# Display results
agent.print_statistics
```

### Multi-Agent Simulation

```ruby
n_agents = 5
agents = []

# Create multiple agents
n_agents.times do |i|
  agents << ActiveInferenceAgent.new(
    n_states: 3,
    n_observations: 3,
    n_actions: 2
  )
end

# Run multi-agent simulation
20.times do |step|
  agents.each_with_index do |agent, i|
    observation = rand(3)
    action = agent.step(observation)

    beliefs = agent.get_beliefs
    max_belief = beliefs.max

    puts "Agent #{i + 1}: Obs=#{observation}, Action=#{action}, " +
         "Best Belief=#{format('%.3f', max_belief)}"
  end
end
```

### Learning Example

```ruby
agent = ActiveInferenceAgent.new(
  n_states: 4,
  n_observations: 3,
  n_actions: 2,
  learning_rate: 0.2
)

# Learning loop
20.times do |trial|
  observation = rand(3)
  action = agent.step(observation)

  # Generate next observation based on action
  next_observation = (observation + action + rand(2)) % 3

  # Learn from experience
  agent.learn(observation, action, next_observation)
end

agent.print_statistics
```

## Requirements

- **Ruby 2.5 or later** (for modern features and performance)
- **No external dependencies** - uses only Ruby standard library

## Installation

```bash
# Ubuntu/Debian
sudo apt-get install ruby-full

# CentOS/RHEL
sudo yum install ruby

# macOS
brew install ruby

# Windows
# Download from https://rubyinstaller.org/
```

## Running the Demo

### Automatic (Cross-platform)
```bash
./run.sh
```

### Manual
```bash
ruby active_inference_agent.rb
```

## Algorithm Details

### Belief Updating
```ruby
# Bayesian inference: P(s|o) ∝ P(o|s) * P(s)
likelihood = @a_matrix[observation]
posterior = likelihood.zip(@beliefs).map { |l, b| l * b }
total = posterior.sum
@beliefs = total > 0 ? posterior.map { |p| p / total } : posterior
```

### Action Selection
```ruby
# Minimize expected free energy
min_efe = Float::INFINITY
best_action = 0

@n_actions.times do |action|
  predicted_beliefs = predict_beliefs(action)
  efe = calculate_expected_free_energy(predicted_beliefs)

  if efe < min_efe
    min_efe = efe
    best_action = action
  end
end
```

### Learning
```ruby
# Simple reinforcement learning
max_state = @beliefs.each_with_index.max[1]
@a_matrix[observation][max_state] += @learning_rate

row_sum = @a_matrix[observation].sum
@a_matrix[observation].map! { |prob| prob / row_sum }
```

## Performance Characteristics

- **Initialization**: O(n_states × n_observations × n_actions)
- **Belief Update**: O(n_states)
- **Action Selection**: O(n_actions × n_states²)
- **Memory Usage**: O(n_states × n_observations × n_actions)

## Extension Points

### Custom Generative Models
```ruby
class CustomAgent < ActiveInferenceAgent
  def initialize_generative_model
    # Custom generative model initialization
    @a_matrix = custom_likelihood_matrix
    @b_matrix = custom_transition_matrix
    # ... etc
  end

  private

  def custom_likelihood_matrix
    # Implement custom observation model
    # Return array of arrays with custom structure
  end
end
```

### DSL for Model Specification
```ruby
class ActiveInferenceDSL
  def self.define_model(&block)
    dsl = ModelDSL.new
    dsl.instance_eval(&block)
    dsl.build_agent
  end
end

# Usage
agent = ActiveInferenceDSL.define_model do
  states 4
  observations 3
  actions 2

  # Define custom transition rules
  transition_rule do |from_state, action, to_state|
    # Custom logic here
  end
end
```

### Rails Integration
```ruby
class ActiveInferenceController < ApplicationController
  def simulate
    agent = ActiveInferenceAgent.new(
      n_states: params[:states].to_i,
      n_observations: params[:observations].to_i,
      n_actions: params[:actions].to_i
    )

    observation = params[:observation].to_i
    action = agent.step(observation)

    render json: {
      action: action,
      beliefs: agent.get_beliefs,
      statistics: agent.get_statistics
    }
  end
end
```

## Testing

The implementation includes comprehensive tests:

```ruby
# Run tests
ruby -r minitest/autorun test_active_inference.rb
```

Example test:
```ruby
class TestActiveInference < Minitest::Test
  def test_belief_update
    agent = ActiveInferenceAgent.new(n_states: 2, n_observations: 2, n_actions: 2)
    initial_beliefs = agent.get_beliefs

    agent.update_beliefs(0)

    # Beliefs should be updated but sum to 1
    new_beliefs = agent.get_beliefs
    assert_in_delta 1.0, new_beliefs.sum, 0.001
    refute_equal initial_beliefs, new_beliefs
  end
end
```

## Gems and Ecosystem

### Recommended Gems for Extensions

- **nmatrix**: High-performance matrix operations
- **daru**: Data analysis and manipulation
- **gnuplot**: Plotting and visualization
- **concurrent-ruby**: Concurrent multi-agent simulations

```ruby
# Add to Gemfile
gem 'nmatrix'
gem 'daru'
gem 'gnuplot'
gem 'concurrent-ruby'
```

## Performance Optimization

### Memory Optimization
```ruby
class MemoryEfficientAgent < ActiveInferenceAgent
  def initialize(**kwargs)
    super
    # Use sparse matrices for large state spaces
    @a_matrix = convert_to_sparse(@a_matrix) if @n_states > 100
  end
end
```

### Parallel Processing
```ruby
require 'concurrent'

class ParallelAgent < ActiveInferenceAgent
  def select_action
    # Parallel EFE calculation for large action spaces
    futures = @n_actions.times.map do |action|
      Concurrent::Future.execute { calculate_efe_for_action(action) }
    end

    min_efe_action = futures.map(&:value).each_with_index.min[1]
  end
end
```

## References

- **Active Inference**: Friston, K. (2010). The free-energy principle
- **Ruby Language**: https://www.ruby-lang.org/
- **Bayesian Inference**: Bishop, C. M. (2006). Pattern Recognition and Machine Learning

## License

This implementation is provided under the MIT License. See the main repository for full license details.
