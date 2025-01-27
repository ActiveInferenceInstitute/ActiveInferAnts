using RxInfer
using Distributions
using Random
using LinearAlgebra
using Rocket

@model NavigatingAgentGridworld() begin
    # Define the grid dimensions
    grid_width = 5
    grid_height = 5

    # Define possible actions
    actions = [:up, :down, :left, :right]

    # Define states as grid positions
    @variable state::Tuple{Int, Int}

    # Define observations (e.g., sensor readings)
    observations = [:obstacle, :goal, :empty]
    @variable observation::Symbol

    # Initial state distribution (starting at position (1,1))
    @prior state ~ Categorical([(1, 1)])

    # Transition model: deterministic movement with boundary conditions
    function transition_model(state, action)
        x, y = state
        new_state = deepcopy(state)
        if action == :up && y < grid_height
            new_state = (x, y + 1)
        elseif action == :down && y > 1
            new_state = (x, y - 1)
        elseif action == :left && x > 1
            new_state = (x - 1, y)
        elseif action == :right && x < grid_width
            new_state = (x + 1, y)
        end
        return new_state
    end

    # Define transition probabilities
    @dynamics state' ~ transition_model(state, action)

    # Observation model: probabilistic observations based on state
    function observation_model(state)
        if state == (grid_width, grid_height)
            return [:goal => 0.9, :empty => 0.1]
        elseif some_obstacle(state)
            return [:obstacle => 0.8, :empty => 0.2]
        else
            return [:empty => 1.0]
        end
    end

    # Helper function to determine if a state has an obstacle
    function some_obstacle(state)
        # Define obstacle positions
        obstacles = [(2,2), (3,3)]
        return state in obstacles
    end

    # Define observation probabilities
    @likelihood observation ~ observation_model(state)

    # Define policy (sequence of actions)
    @policy actions_policy::Vector{Symbol}
end

# Additional functions for agent behavior

function choose_action(state::Tuple{Int, Int}, goal::Tuple{Int, Int})
    # Simple heuristic: move towards the goal
    x, y = state
    goal_x, goal_y = goal
    
    if x < goal_x
        return :right
    elseif x > goal_x
        return :left
    elseif y < goal_y
        return :up
    elseif y > goal_y
        return :down
    else
        return :up  # Default action if at goal
    end
end

function update_belief(agent_model, observation)
    # Update the agent's belief based on the observation using RxInfer
    updated_belief = update(agent_model, (:observation, observation))
    return updated_belief
end

function run_episode(agent_model, max_steps=100)
    goal = (5, 5)  # Top-right corner of the grid
    
    # Initialize the belief
    initial_belief = initialize(agent_model)
    
    # Create a Subject for observations
    observations = Subject(Symbol)
    
    # Create a reactive stream for belief updates
    beliefs = observations |> scan(update_belief, initial_belief)
    
    for step in 1:max_steps
        # Get current state from the latest belief
        current_state = mode(beliefs |> latest())
        
        # Choose an action
        action = choose_action(current_state, goal)
        
        # Take action and get observation (this would interact with the environment)
        observation = take_action_and_observe(agent_model, action)
        
        # Push the observation to update the belief
        next!(observations, observation)
        
        # Check if goal is reached
        if current_state == goal
            println("Goal reached in $step steps!")
            break
        end
    end
    
    complete!(observations)
end

function take_action_and_observe(agent_model, action)
    # Simulate the environment's response to the action
    # This is a placeholder and should be implemented based on your specific environment
    # For now, we'll return a random observation
    return rand([:obstacle, :goal, :empty])
end

# Main execution
function main()
    agent_model = NavigatingAgentGridworld()
    run_episode(agent_model)
end

# Uncomment to run the main function
# main()
