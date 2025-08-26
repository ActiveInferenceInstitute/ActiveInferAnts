# Active Inference Implementation in Crystal

class ActiveInferenceAgent
  @num_states : Int32 = 4
  @num_observations : Int32 = 3
  @num_actions : Int32 = 2

  property beliefs : Array(Float64)
  property a_matrix : Array(Array(Float64))
  property b_matrix : Array(Array(Float64))
  property c_vector : Array(Float64)
  property d_vector : Array(Float64)

  def initialize
    @beliefs = Array.new(@num_states) { 1.0 / @num_states }
    @a_matrix = [
      [0.8, 0.1, 0.1],
      [0.1, 0.8, 0.1],
      [0.1, 0.1, 0.8]
    ]
    @b_matrix = [
      [0.9, 0.1],
      [0.1, 0.9]
    ]
    @c_vector = [0.0, 0.5, 0.0]
    @d_vector = [0.5, 0.5]
  end

  def update_beliefs(observation : Int32)
    likelihood = @a_matrix[observation - 1]
    posterior = Array.new(@num_states) do |i|
      likelihood[i] * @beliefs[i]
    end

    # Normalize
    total = posterior.sum
    @beliefs = posterior.map { |p| total > 0 ? p / total : p }
  end

  def calculate_expected_free_energy(action : Int32) : Float64
    # Simplified EFE calculation
    @beliefs.each_with_index.sum do |belief, state|
      belief > 0 ? -belief * Math.log(belief) : 0.0
    end
  end

  def select_action : Int32
    (1..@num_actions).min_by do |action|
      calculate_expected_free_energy(action)
    end
  end

  def step(observation : Int32)
    update_beliefs(observation)
    select_action
  end

  def print_beliefs
    puts "Beliefs: #{@beliefs.map { |b| "%.3f" % b }.join(", ")}"
  end
end

# Demo
agent = ActiveInferenceAgent.new
puts "Crystal Active Inference Demo"
puts "Initial beliefs:"
agent.print_beliefs

5.times do |cycle|
  observation = (cycle % 3) + 1
  action = agent.step(observation)
  puts "Cycle #{cycle + 1}, Observation: #{observation}, Action: #{action}"
  agent.print_beliefs
end
