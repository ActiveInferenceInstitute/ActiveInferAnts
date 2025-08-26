#!/usr/bin/env ruby

# Active Inference Implementation in Ruby
# =====================================
#
# This implementation demonstrates the Active Inference framework using Ruby's
# elegant object-oriented design and array operations.

require 'matrix'

class ActiveInferenceAgent
  attr_reader :n_states, :n_observations, :n_actions, :precision, :learning_rate
  attr_reader :beliefs, :belief_history, :action_history, :observation_history, :free_energy_history

  def initialize(n_states: 4, n_observations: 3, n_actions: 2, precision: 1.0, learning_rate: 0.1)
    @n_states = n_states
    @n_observations = n_observations
    @n_actions = n_actions
    @precision = precision
    @learning_rate = learning_rate

    # Initialize generative model
    initialize_generative_model

    # Initialize beliefs to prior
    @beliefs = @d_vector.clone
    @belief_history = [@beliefs.clone]
    @action_history = []
    @observation_history = []
    @free_energy_history = []
  end

  def initialize_generative_model
    # Initialize A matrix (observation likelihood) - P(o|s)
    @a_matrix = Array.new(@n_observations) do |o|
      Array.new(@n_states) do |s|
        # Diagonal structure with some noise
        if (s % @n_observations) == o
          0.8  # High probability for matching observation
        else
          0.2 / (@n_observations - 1)  # Low probability for others
        end
      end
    end

    # Initialize B matrix (state transitions) - P(s'|s,a)
    @b_matrix = Array.new(@n_actions) do |a|
      Array.new(@n_states) do |s|
        Array.new(@n_states) do |s_next|
          # Action-specific transition patterns
          if s_next == ((s + a + 1) % @n_states)
            0.7  # Likely to move forward by action amount
          elsif s_next == s
            0.2  # Some probability of staying
          else
            0.1 / (@n_states - 2)  # Low probability for others
          end
        end
      end
    end

    # Initialize C vector (observation preferences) - P(o)
    @c_vector = Array.new(@n_observations) do |o|
      o == 0 ? 0.0 : 0.5  # Lower energy for preferred observation
    end

    # Initialize D vector (prior beliefs) - P(s)
    @d_vector = Array.new(@n_states) { 1.0 / @n_states }  # Uniform prior
  end

  # Update beliefs using Bayesian inference
  def update_beliefs(observation)
    # Get likelihood for this observation
    likelihood = @a_matrix[observation]

    # Compute posterior: P(s|o) ∝ P(o|s) * P(s)
    posterior = likelihood.zip(@beliefs).map { |l, b| l * b }

    # Normalize
    total = posterior.sum
    @beliefs = total > 0 ? posterior.map { |p| p / total } : posterior

    # Store in history
    @belief_history << @beliefs.clone
    @observation_history << observation
  end

  # Select action by minimizing expected free energy
  def select_action
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

    @action_history << best_action
    best_action
  end

  # Predict beliefs after taking an action
  def predict_beliefs(action)
    predicted_beliefs = Array.new(@n_states, 0.0)

    @n_states.times do |s_next|
      @n_states.times do |s|
        predicted_beliefs[s_next] += @b_matrix[action][s][s_next] * @beliefs[s]
      end
    end

    predicted_beliefs
  end

  # Calculate expected free energy for predicted beliefs
  def calculate_expected_free_energy(predicted_beliefs)
    efe = 0.0

    @n_states.times do |s|
      if predicted_beliefs[s] > 0
        # KL divergence between predicted beliefs and prior
        efe += predicted_beliefs[s] * Math.log(predicted_beliefs[s] / @d_vector[s])
      end
    end

    efe * @precision
  end

  # Calculate current variational free energy
  def calculate_free_energy
    fe = 0.0

    @n_states.times do |s|
      if @beliefs[s] > 0
        fe += @beliefs[s] * Math.log(@beliefs[s] / @d_vector[s])
      end
    end

    @free_energy_history << fe
    fe
  end

  # Execute one perception-action cycle
  def step(observation)
    update_beliefs(observation)
    action = select_action
    calculate_free_energy
    action
  end

  # Learn from experience
  def learn(observation, action, next_observation)
    # Simple learning: reinforce the most likely state
    max_state = @beliefs.each_with_index.max[1]

    # Update A matrix
    @a_matrix[observation][max_state] += @learning_rate

    # Renormalize row
    row_sum = @a_matrix[observation].sum
    @a_matrix[observation].map! { |prob| prob / row_sum }
  end

  # Calculate belief entropy
  def calculate_belief_entropy
    entropy = 0.0
    @n_states.times do |s|
      if @beliefs[s] > 0
        entropy -= @beliefs[s] * Math.log(@beliefs[s])
      end
    end
    entropy
  end

  # Print agent statistics
  def print_statistics
    puts "Active Inference Agent Statistics:"
    puts "====================================="
    puts "States: #{@n_states}, Observations: #{@n_observations}, Actions: #{@n_actions}"
    puts "Precision: #{format('%.2f', @precision)}, Learning Rate: #{format('%.2f', @learning_rate)}"

    if !@action_history.empty?
      puts "Total steps: #{@action_history.length}"
      print "Final beliefs: ["
      @n_states.times do |s|
        print format('%.3f', @beliefs[s])
        print ', ' if s < @n_states - 1
      end
      puts ']'

      if !@free_energy_history.empty?
        puts "Final free energy: #{format('%.4f', @free_energy_history.last)}"
      end

      entropy = calculate_belief_entropy
      puts "Belief entropy: #{format('%.4f', entropy)}"
    else
      puts "No steps taken yet."
    end
  end

  # Get comprehensive statistics
  def get_statistics
    stats = {
      n_states: @n_states,
      n_observations: @n_observations,
      n_actions: @n_actions,
      precision: @precision,
      learning_rate: @learning_rate,
      current_beliefs: @beliefs.clone,
      total_steps: @action_history.length,
      belief_history_length: @belief_history.length
    }

    if !@free_energy_history.empty?
      stats[:final_free_energy] = @free_energy_history.last
      stats[:free_energy_history] = @free_energy_history.clone
    end

    if !@action_history.empty?
      stats[:action_history] = @action_history.clone
      stats[:observation_history] = @observation_history.clone
    end

    stats[:belief_entropy] = calculate_belief_entropy
    stats
  end

  # Get current beliefs
  def get_beliefs
    @beliefs.clone
  end
end

# Demonstration class
class ActiveInferenceDemo
  def self.run
    puts "🧠 Active Inference Ruby Implementation"
    puts "======================================"
    puts

    # Create agent
    n_states = 3
    n_observations = 3
    n_actions = 2

    puts "Creating agent with #{n_states} states, #{n_observations} observations, #{n_actions} actions..."
    puts

    agent = ActiveInferenceAgent.new(
      n_states: n_states,
      n_observations: n_observations,
      n_actions: n_actions,
      precision: 1.0,
      learning_rate: 0.1
    )

    # Print initial beliefs
    puts "Initial beliefs: [#{agent.get_beliefs.map { |b| format('%.3f', b) }.join(', ')}]"
    puts

    # Run simulation
    n_steps = 10
    puts "Running simulation for #{n_steps} steps..."
    puts

    n_steps.times do |step|
      # Generate random observation
      observation = rand(n_observations)

      puts "Step #{step + 1}:"
      puts "  Observation: #{observation}"

      # Execute perception-action cycle
      action = agent.step(observation)

      puts "  Selected action: #{action}"

      # Print current beliefs
      current_beliefs = agent.get_beliefs
      puts "  Updated beliefs: [#{current_beliefs.map { |b| format('%.3f', b) }.join(', ')}]"

      # Print free energy
      stats = agent.get_statistics
      if stats.key?(:final_free_energy)
        puts "  Free energy: #{format('%.4f', stats[:final_free_energy])}"
      end

      puts
    end

    # Print final statistics
    puts
    agent.print_statistics

    puts
    puts "✅ Ruby Active Inference simulation completed!"
  end

  def self.run_multi_agent_demo
    puts
    puts "🐜 Multi-Agent Ruby Demo"
    puts "========================"
    puts

    n_agents = 3
    agents = []

    # Create multiple agents
    n_agents.times do |i|
      agents << ActiveInferenceAgent.new(
        n_states: 3,
        n_observations: 3,
        n_actions: 2,
        precision: 1.0,
        learning_rate: 0.1
      )
    end

    # Run multi-agent simulation
    5.times do |step|
      puts "Multi-agent Step #{step + 1}:"

      agents.each_with_index do |agent, i|
        observation = rand(3)
        action = agent.step(observation)

        beliefs = agent.get_beliefs
        max_belief = beliefs.max

        puts "  Agent #{i + 1}: Obs=#{observation}, Action=#{action}, " +
             "Best Belief=#{format('%.3f', max_belief)}"
      end
      puts
    end

    puts "✅ Multi-agent simulation completed!"
  end
end

# Learning demonstration
class LearningDemo
  def self.run
    puts
    puts "🎓 Active Inference Learning Demo"
    puts "================================"
    puts

    agent = ActiveInferenceAgent.new(
      n_states: 4,
      n_observations: 3,
      n_actions: 2,
      precision: 1.0,
      learning_rate: 0.2
    )

    puts "Initial A-matrix (observation model):"
    agent.instance_variable_get(:@a_matrix).each_with_index do |row, o|
      puts "  O#{o}: [#{row.map { |p| format('%.2f', p) }.join(', ')}]"
    end
    puts

    # Learning loop
    20.times do |trial|
      # Generate observation
      observation = rand(3)

      # Step through environment
      action = agent.step(observation)

      # Generate next observation based on action
      next_observation = (observation + action + rand(2)) % 3

      # Learn from experience
      agent.learn(observation, action, next_observation)
    end

    puts "After learning:"
    agent.instance_variable_get(:@a_matrix).each_with_index do |row, o|
      puts "  O#{o}: [#{row.map { |p| format('%.2f', p) }.join(', ')}]"
    end

    puts
    agent.print_statistics

    puts
    puts "✅ Learning demonstration completed!"
  end
end

# Run demos if this file is executed directly
if __FILE__ == $0
  ActiveInferenceDemo.run
  ActiveInferenceDemo.run_multi_agent_demo
  LearningDemo.run
end
