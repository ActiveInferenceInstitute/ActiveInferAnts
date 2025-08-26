-- Active Inference Implementation in Lua

local ActiveInference = {}
ActiveInference.__index = ActiveInference

function ActiveInference:new()
    local agent = {
        num_states = 4,
        num_observations = 3,
        num_actions = 2,
        beliefs = {0.25, 0.25, 0.25, 0.25},
        a_matrix = {
            {0.8, 0.1, 0.1},
            {0.1, 0.8, 0.1},
            {0.1, 0.1, 0.8}
        },
        b_matrix = {
            {0.9, 0.1},
            {0.1, 0.9}
        },
        c_vector = {0.0, 0.5, 0.0},
        d_vector = {0.5, 0.5}
    }
    setmetatable(agent, self)
    return agent
end

function ActiveInference:update_beliefs(observation)
    local likelihood = self.a_matrix[observation]
    local posterior = {}
    local total = 0
    
    -- Calculate posterior P(s|o) ∝ P(o|s) * P(s)
    for i = 1, self.num_states do
        posterior[i] = likelihood[i] * self.beliefs[i]
        total = total + posterior[i]
    end
    
    -- Normalize
    if total > 0 then
        for i = 1, self.num_states do
            self.beliefs[i] = posterior[i] / total
        end
    end
end

function ActiveInference:calculate_expected_free_energy(action)
    local efe = 0
    for i, belief in ipairs(self.beliefs) do
        if belief > 0 then
            efe = efe - belief * math.log(belief)
        end
    end
    return efe
end

function ActiveInference:select_action()
    local min_efe = math.huge
    local best_action = 1
    
    for action = 1, self.num_actions do
        local efe = self:calculate_expected_free_energy(action)
        if efe < min_efe then
            min_efe = efe
            best_action = action
        end
    end
    
    return best_action
end

function ActiveInference:step(observation)
    self:update_beliefs(observation)
    return self:select_action()
end

function ActiveInference:print_beliefs()
    io.write("Beliefs: ")
    for i, belief in ipairs(self.beliefs) do
        io.write(string.format("%.3f", belief))
        if i < #self.beliefs then io.write(", ") end
    end
    io.write("\n")
end

-- Demo
local agent = ActiveInference:new()
print("Lua Active Inference Demo")
print("Initial beliefs:")
agent:print_beliefs()

for cycle = 1, 5 do
    local observation = (cycle - 1) % 3 + 1
    local action = agent:step(observation)
    io.write(string.format("Cycle %d: Observation=%d, Action=%d, ", cycle, observation, action))
    agent:print_beliefs()
end
