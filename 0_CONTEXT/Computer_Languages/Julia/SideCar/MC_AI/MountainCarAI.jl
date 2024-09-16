module MountainCarAI

using RxInfer
using LinearAlgebra

include("physics.jl")
include("agent.jl")
include("environment.jl")

export Environment, create_environment, step_environment!, create_agent, create_world, create_physics

end
