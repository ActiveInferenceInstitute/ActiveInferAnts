using Distributions, LinearAlgebra, Random, Printf, ArgParse

abstract type ActiveInferenceAgent end

mutable struct ActiveNestmate <: ActiveInferenceAgent
    position::Vector{Float64}
    influence_factor::Float64
    A_matrix::Matrix{Float64}
    B_matrix::Matrix{Float64}
    C_matrix::Vector{Float64}
    D_matrix::Vector{Float64}
    preferences::Vector{Float64}
    uncertainty::Float64
end

function initialize_matrices!(agent::ActiveNestmate, sensory_modalities::Int, observation_dim::Int, action_modalities::Int, state_dim::Int)
    agent.A_matrix = randn(observation_dim, sensory_modalities)
    agent.B_matrix = randn(state_dim, action_modalities)
    agent.C_matrix = randn(observation_dim)
    agent.D_matrix = randn(state_dim)
end

function update_internal_states!(agent::ActiveNestmate, action::Vector{Float64}, observation::Vector{Float64})
    agent.B_matrix .+= action * transpose(observation)
    agent.A_matrix .+= observation * transpose(observation)
end

function move!(agent::ActiveNestmate, direction::Vector{Float64})
    agent.position .+= direction
end

function calculate_vfe(agent::ActiveNestmate, observation::Vector{Float64})::Float64
    qs = softmax(agent.position) # Improved approximation
    expected_log_likelihood = dot(qs, log.(agent.A_matrix[:, observation]))
    kl_divergence = dot(qs, (log.(qs) .- log.(agent.position)))
    vfe = -(expected_log_likelihood - kl_divergence)
    return vfe
end

function calculate_efe(agent::ActiveNestmate, action::Vector{Float64}, future_states::Vector{Float64}, preferences::Vector{Float64}, uncertainty::Float64)::Float64
    pragmatic_value = dot(future_states, (log.(future_states) .- log.(preferences)))
    epistemic_value = -entropy(future_states)
    efe = pragmatic_value + uncertainty * epistemic_value
    return efe
end

function softmax(x::Vector{Float64})
    e_x = exp.(x .- maximum(x))
    return e_x ./ sum(e_x)
end

function decide_next_action(agent::ActiveNestmate)::Vector{Float64}
    possible_actions = [normalize(randn(2), 1) for _ in 1:5] # Normalized actions
    efe_scores = [calculate_efe(agent, action, agent.position + action, agent.preferences, agent.uncertainty) for action in possible_actions]
    probabilities = softmax(-efe_scores)
    chosen_index = rand(Categorical(probabilities))
    return possible_actions[chosen_index]
end

function parse_args()
    s = ArgParseSettings()
    @add_arg_table! s begin
        "--steps", "-s", arg_type=Int, default=10, help="Number of simulation steps"
        "--uncertainty", "-u", arg_type=Float64, default=0.1, help="Uncertainty factor for the agent"
    end
    return parse_args(s)
end

function main()
    args = parse_args()
    steps, uncertainty = args["steps"], args["uncertainty"]

    agent = ActiveNestmate(rand(2), 0.5, randn(2, 2), randn(2, 2), randn(2), randn(2), [0.5, 0.5], uncertainty)
    initialize_matrices!(agent, 2, 2, 2, 2)

    for step in 1:steps
        action = decide_next_action(agent)
        observation = rand(2) # Simulated observation
        update_internal_states!(agent, action, observation)
        move!(agent, action)
        @printf("Step %d: Position = [%f, %f]\n", step, agent.position...)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
