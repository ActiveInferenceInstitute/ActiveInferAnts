import HypergeometricFunctions: _₂F₁

function create_physics(; engine_force_limit = 0.04, friction_coefficient = 0.1)
    Fa = (a::Real) -> engine_force_limit * tanh(a) 
    Ff = (y_dot::Real) -> -friction_coefficient * y_dot 
    Fg = (y::Real) -> begin
        if y < 0
            0.05*(-2*y - 1)
        else
            0.05*(-(1 + 5*y^2)^(-0.5) - (y^2)*(1 + 5*y^2)^(-3/2) - (y^4)/16)
        end
    end
    height = (x::Float64) -> begin
        if x < 0
            h = x^2 + x
        else
            h = x * _₂F₁(0.5,0.5,1.5, -5*x^2) + x^3 * _₂F₁(1.5, 1.5, 2.5, -5*x^2) / 3 + x^5 / 80
        end
        return 0.05*h
    end
    return (Fa, Ff, Fg, height)
end

function create_world(physics; initial_position = -0.5, initial_velocity = 0.0)
    Fa, Ff, Fg, height = physics
    initial_state = [initial_position, initial_velocity]
    
    execute = (a_t::Float64, state::Vector{Float64}) -> begin
        y_t, y_dot_t = state
        y_dot_t_new = y_dot_t + Fg(y_t) + Ff(y_dot_t) + Fa(a_t)
        y_t_new = y_t + y_dot_t_new
        state[1], state[2] = y_t_new, y_dot_t_new
    end
    
    observe = (state::Vector{Float64}) -> copy(state)
        
    return (execute, observe, initial_state)
end