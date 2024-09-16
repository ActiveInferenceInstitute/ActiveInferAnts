mutable struct Environment
    T_ai::Int
    t::Int
    agents::Vector{Dict}
    execute_ai::Vector
    observe_ai::Vector
    agent_states::Vector{Vector{Float64}}  # Store each agent's state
    
    Environment(; T_ai, agents, execute_ai, observe_ai, initial_states) = begin
        return new(T_ai, 1, agents, execute_ai, observe_ai, initial_states)
    end
end

function step_environment!(env::Environment)
    for (i, agent) in enumerate(env.agents)
        # Compute new action
        new_action = agent[:act_ai]()
        push!(agent[:agent_a], new_action)

        # Compute future prediction
        new_future = agent[:future_ai]()
        push!(agent[:agent_f], new_future)

        # Execute action and observe new state
        env.execute_ai[i](new_action, env.agent_states[i])
        new_observation = env.observe_ai[i](env.agent_states[i])
        push!(agent[:agent_x], new_observation)

        # Update AI
        agent[:compute_ai](new_action, new_observation)
        agent[:slide_ai]()
    end
    env.t += 1
end