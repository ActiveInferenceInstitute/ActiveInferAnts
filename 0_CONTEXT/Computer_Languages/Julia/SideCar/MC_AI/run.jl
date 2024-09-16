using MountainCarAI

# Set up the physics and world
engine_force_limit1 = 0.04
engine_force_limit2 = 0.02
Fa1, Ff1, Fg1, height1 = create_physics(engine_force_limit = engine_force_limit1)
Fa2, Ff2, Fg2, height2 = create_physics(engine_force_limit = engine_force_limit2)

initial_position = -0.5
initial_velocity = 0.0

execute_ai1, observe_ai1, initial_state1 = create_world(
    (Fa1, Ff1, Fg1, height1),
    initial_position = initial_position, 
    initial_velocity = initial_velocity
)

execute_ai2, observe_ai2, initial_state2 = create_world(
    (Fa2, Ff2, Fg2, height2),
    initial_position = initial_position, 
    initial_velocity = initial_velocity
)

# Set up simulation parameters
T_ai = 50
N_ai = 100
x_target = [0.5, 0.0]

# Create agent 1
(compute_ai1, act_ai1, slide_ai1, future_ai1) = create_agent(
    T = T_ai,
    Fa = Fa1,
    Fg = Fg1,
    Ff = Ff1,
    engine_force_limit = engine_force_limit1,
    x_target = x_target,
    initial_position = initial_position,
    initial_velocity = initial_velocity
)

# Create agent 2
(compute_ai2, act_ai2, slide_ai2, future_ai2) = create_agent(
    T = T_ai,
    Fa = Fa2,
    Fg = Fg2,
    Ff = Ff2,
    engine_force_limit = engine_force_limit2,
    x_target = x_target,
    initial_position = initial_position,
    initial_velocity = initial_velocity
)

agents = [
    Dict(
        :act_ai => act_ai1, :future_ai => future_ai1, :compute_ai => compute_ai1, :slide_ai => slide_ai1,
        :agent_a => Float64[], :agent_f => Vector{Float64}[], :agent_x => Vector{Float64}[]
    ),
    Dict(
        :act_ai => act_ai2, :future_ai => future_ai2, :compute_ai => compute_ai2, :slide_ai => slide_ai2,
        :agent_a => Float64[], :agent_f => Vector{Float64}[], :agent_x => Vector{Float64}[]
    )
]

# Initialize the environment
env = Environment(
    T_ai = T_ai,
    agents = agents,
    execute_ai = [execute_ai1, execute_ai2],
    observe_ai = [observe_ai1, observe_ai2],
    initial_states = [initial_state1, initial_state2]
)

# Step through actions for each agent within the environment
for _ in 1:N_ai
    step_environment!(env)
end

# Print final positions of both agents
println("Final position of Agent 1: ", env.agents[1][:agent_x][end][1])
println("Final position of Agent 2: ", env.agents[2][:agent_x][end][1])