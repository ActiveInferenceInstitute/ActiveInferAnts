% Active Inference Demo in MATLAB/Octave
% This script demonstrates the Active Inference agent in action

fprintf('🧠 Active Inference MATLAB/Octave Implementation\n');
fprintf('===============================================\n\n');

% Create agent
n_states = 3;
n_observations = 3;
n_actions = 2;

fprintf('Creating agent with %d states, %d observations, %d actions...\n', ...
    n_states, n_observations, n_actions);

agent = ActiveInferenceAgent(n_states, n_observations, n_actions, ...
    'precision', 1.0, 'learning_rate', 0.1);

% Print initial state
fprintf('\nInitial beliefs: [');
for s = 1:n_states
    fprintf('%.3f', agent.beliefs(s));
    if s < n_states
        fprintf(', ');
    end
end
fprintf(']\n\n');

% Run simulation
n_steps = 10;
fprintf('Running simulation for %d steps...\n\n', n_steps);

for step = 1:n_steps
    % Generate random observation
    observation = randi(n_observations);

    fprintf('Step %d:\n', step);
    fprintf('  Observation: %d\n', observation);

    % Execute perception-action cycle
    [agent, action] = agent.step(observation);

    fprintf('  Selected action: %d\n', action);
    fprintf('  Updated beliefs: [');
    for s = 1:n_states
        fprintf('%.3f', agent.beliefs(s));
        if s < n_states
            fprintf(', ');
        end
    end
    fprintf(']\n');

    if ~isempty(agent.free_energy_history)
        fprintf('  Free energy: %.4f\n', agent.free_energy_history(end));
    end
    fprintf('\n');
end

% Print final statistics
agent.printStatistics();

% Plot results if MATLAB/Octave supports plotting
try
    agent.plotBeliefs('Active Inference Belief Evolution');
    fprintf('Belief evolution plot created successfully!\n');
catch
    fprintf('Plotting not available in this environment.\n');
end

fprintf('\n✅ MATLAB/Octave Active Inference simulation completed!\n');
