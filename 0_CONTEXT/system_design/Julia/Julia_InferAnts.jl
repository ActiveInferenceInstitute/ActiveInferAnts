using Distributions, LinearAlgebra, Random, Printf, ArgParse, StaticArrays, Logging, Plots

# Define custom types for improved type stability and readability
const Position = MVector{2,Float64}
const Matrix2D = Matrix{Float64}
const Vector2D = Vector{Float64}
const SVector2D = SVector{2,Float64}

"""
Abstract type for all active inference agents in the simulation.
"""
abstract type ActiveInferenceAgent end

"""
Represents an active nestmate in the ant colony simulation.

Fields:
- position: Current 2D position of the agent
- influence_factor: Factor determining the agent's influence on others
- A_matrix: Likelihood mapping (observation model)
- B_matrix: State transition beliefs
- C_matrix: Prior preferences over observations
- D_matrix: Prior beliefs about initial states
- preferences: Agent's preferences over states
- uncertainty: Epistemic value weighting factor
"""
struct ActiveNestmate <: ActiveInferenceAgent
    position::Position
    influence_factor::Float64
    A_matrix::Matrix2D
    B_matrix::Matrix2D
    C_matrix::Vector2D
    D_matrix::Vector2D
    preferences::SVector2D
    uncertainty::Float64
end

"""
Constructor for ActiveNestmate with type checking and validation.
"""
function ActiveNestmate(
    position::Vector2D,
    influence_factor::Float64,
    A_matrix::Matrix2D,
    B_matrix::Matrix2D,
    C_matrix::Vector2D,
    D_matrix::Vector2D,
    preferences::Vector2D,
    uncertainty::Float64
)
    @assert length(position) == 2 "Position must be a 2D vector"
    @assert 0 <= influence_factor <= 1 "Influence factor must be between 0 and 1"
    @assert size(A_matrix, 1) == size(A_matrix, 2) "A_matrix must be square"
    @assert size(B_matrix, 1) == size(B_matrix, 2) "B_matrix must be square"
    @assert length(C_matrix) == size(A_matrix, 1) "C_matrix length must match A_matrix dimensions"
    @assert length(D_matrix) == size(B_matrix, 1) "D_matrix length must match B_matrix dimensions"
    @assert length(preferences) == 2 "Preferences must be a 2D vector"
    @assert uncertainty >= 0 "Uncertainty must be non-negative"

    return ActiveNestmate(
        Position(position),
        influence_factor,
        A_matrix,
        B_matrix,
        C_matrix,
        D_matrix,
        SVector2D(preferences),
        uncertainty
    )
end

"""
Initialize matrices for the agent based on the given dimensions.
"""
function initialize_matrices!(
    agent::ActiveNestmate,
    sensory_modalities::Int,
    observation_dim::Int,
    action_modalities::Int,
    state_dim::Int
)
    agent.A_matrix .= normalize(randn(observation_dim, sensory_modalities), dims=2)
    agent.B_matrix .= normalize(randn(state_dim, action_modalities), dims=2)
    agent.C_matrix .= normalize(randn(observation_dim))
    agent.D_matrix .= normalize(randn(state_dim))
end

"""
Update the agent's internal states based on the latest action and observation.
"""
function update_internal_states!(
    agent::ActiveNestmate,
    action::Vector2D,
    observation::Vector2D
)
    η = 0.1  # Learning rate
    agent.B_matrix .+= η * (action * observation' - agent.B_matrix)
    agent.A_matrix .+= η * (observation * observation' - agent.A_matrix)
end

"""
Move the agent based on the given direction.
"""
function move!(agent::ActiveNestmate, direction::Vector2D)
    agent.position .+= direction
end

"""
Calculate the variational free energy for the agent.
"""
function calculate_vfe(agent::ActiveNestmate, observation::Vector2D)::Float64
    qs = softmax(agent.position)
    expected_log_likelihood = dot(qs, log.(agent.A_matrix * observation))
    kl_divergence = kldivergence(Categorical(qs), Categorical(softmax(agent.D_matrix)))
    return -(expected_log_likelihood - kl_divergence)
end

"""
Calculate the expected free energy for the agent.
"""
function calculate_efe(
    agent::ActiveNestmate,
    action::Vector2D,
    future_states::Vector2D
)::Float64
    pragmatic_value = dot(future_states, log.(future_states) .- log.(agent.preferences))
    epistemic_value = -entropy(Categorical(future_states))
    return pragmatic_value + agent.uncertainty * epistemic_value
end

"""
Compute the softmax function for a given vector.
"""
function softmax(x::AbstractVector)::Vector{Float64}
    e_x = exp.(x .- maximum(x))
    return e_x ./ sum(e_x)
end

"""
Decide the next action for the agent based on active inference principles.
"""
function decide_next_action(agent::ActiveNestmate)::Vector2D
    num_actions = 8
    possible_actions = [normalize(randn(SVector2D)) for _ in 1:num_actions]
    
    efe_scores = [
        calculate_efe(
            agent,
            action,
            softmax(agent.B_matrix * (agent.position + action))
        )
        for action in possible_actions
    ]
    
    probabilities = softmax(-efe_scores)
    chosen_index = rand(Categorical(probabilities))
    return Vector(possible_actions[chosen_index])
end

"""
Parse command-line arguments for the simulation.
"""
function parse_commandline()
    s = ArgParseSettings()
    @add_arg_table! s begin
        "--steps", "-s"
            help = "Number of simulation steps"
            arg_type = Int
            default = 100
        "--uncertainty", "-u"
            help = "Uncertainty factor for the agent"
            arg_type = Float64
            default = 0.1
        "--num_agents", "-n"
            help = "Number of agents in the simulation"
            arg_type = Int
            default = 5
        "--plot", "-p"
            help = "Generate plots of the simulation"
            action = :store_true
    end
    return parse_args(s)
end

"""
Run the ant colony simulation with multiple agents.
"""
function run_simulation(steps::Int, uncertainty::Float64, num_agents::Int, generate_plots::Bool)
    agents = [
        ActiveNestmate(
            rand(2) * 10,  # Random initial position in a 10x10 grid
            rand(),
            randn(2, 2),
            randn(2, 2),
            randn(2),
            randn(2),
            normalize(rand(2)),
            uncertainty
        ) for _ in 1:num_agents
    ]

    for agent in agents
        initialize_matrices!(agent, 2, 2, 2, 2)
    end

    if generate_plots
        plot_data = [Vector{Tuple{Float64, Float64}}() for _ in 1:num_agents]
    end

    for step in 1:steps
        for (i, agent) in enumerate(agents)
            action = decide_next_action(agent)
            observation = normalize(randn(2))  # Simulated observation
            update_internal_states!(agent, action, observation)
            move!(agent, action)
            
            if generate_plots
                push!(plot_data[i], (agent.position[1], agent.position[2]))
            end

            @info "Step $step, Agent $i: Position = [$(agent.position[1]), $(agent.position[2])]"
        end
    end

    if generate_plots
        p = plot(title="Ant Colony Simulation", xlabel="X", ylabel="Y", aspect_ratio=:equal)
        for (i, data) in enumerate(plot_data)
            x, y = zip(data...)
            plot!(p, x, y, label="Agent $i", marker=:circle)
        end
        savefig(p, "ant_colony_simulation.png")
        @info "Plot saved as ant_colony_simulation.png"
    end
end

"""
Main function to run the simulation.
"""
function main()
    args = parse_commandline()
    run_simulation(args["steps"], args["uncertainty"], args["num_agents"], args["plot"])
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
