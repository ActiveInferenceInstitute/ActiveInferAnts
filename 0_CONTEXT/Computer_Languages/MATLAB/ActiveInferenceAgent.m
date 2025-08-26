classdef ActiveInferenceAgent < handle
    % Active Inference Agent Implementation in MATLAB/Octave
    %
    % This class implements the core active inference algorithm using
    % MATLAB's matrix operations and statistical capabilities.

    properties
        % Agent dimensions
        n_states        % Number of hidden states
        n_observations  % Number of observations
        n_actions       % Number of actions

        % Generative model matrices
        A_matrix        % Likelihood P(o|s) - observation model
        B_matrix        % Transition P(s'|s,a) - state transitions
        C_vector        % Preferences P(o) - observation preferences
        D_vector        % Prior P(s) - initial state beliefs

        % Current beliefs and parameters
        beliefs         % Current belief state P(s|o)
        precision       % Precision parameter for inference
        learning_rate   % Learning rate for model updates

        % History for analysis
        belief_history  % History of belief states
        action_history  % History of actions taken
        observation_history % History of observations
        free_energy_history % History of free energy values
    end

    methods
        function obj = ActiveInferenceAgent(n_states, n_observations, n_actions, varargin)
            % Constructor
            % Optional parameters: precision, learning_rate

            % Set dimensions
            obj.n_states = n_states;
            obj.n_observations = n_observations;
            obj.n_actions = n_actions;

            % Set default parameters
            obj.precision = 1.0;
            obj.learning_rate = 0.1;

            % Override defaults with varargin
            if ~isempty(varargin)
                for i = 1:2:length(varargin)
                    if strcmp(varargin{i}, 'precision')
                        obj.precision = varargin{i+1};
                    elseif strcmp(varargin{i}, 'learning_rate')
                        obj.learning_rate = varargin{i+1};
                    end
                end
            end

            % Initialize generative model
            obj = obj.initializeGenerativeModel();

            % Initialize beliefs to prior
            obj.beliefs = obj.D_vector;

            % Initialize history
            obj.belief_history = {};
            obj.action_history = [];
            obj.observation_history = [];
            obj.free_energy_history = [];

            % Store initial state
            obj.belief_history{1} = obj.beliefs;
        end

        function obj = initializeGenerativeModel(obj)
            % Initialize the generative model matrices

            % A_matrix: Likelihood P(o|s)
            % Simple diagonal structure with some noise
            obj.A_matrix = zeros(obj.n_observations, obj.n_states);
            for s = 1:obj.n_states
                for o = 1:obj.n_observations
                    if o == mod(s-1, obj.n_observations) + 1
                        obj.A_matrix(o, s) = 0.8;  % High probability for matching observation
                    else
                        obj.A_matrix(o, s) = 0.2 / (obj.n_observations - 1);  % Low probability for others
                    end
                end
            end

            % B_matrix: State transitions P(s'|s,a)
            obj.B_matrix = zeros(obj.n_states, obj.n_states, obj.n_actions);

            for a = 1:obj.n_actions
                for s = 1:obj.n_states
                    for s_next = 1:obj.n_states
                        % Action-specific transition patterns
                        if s_next == mod(s + a - 1, obj.n_states) + 1
                            obj.B_matrix(s_next, s, a) = 0.7;  % Likely to move forward by action amount
                        elseif s_next == s
                            obj.B_matrix(s_next, s, a) = 0.2;  % Some probability of staying
                        else
                            obj.B_matrix(s_next, s, a) = 0.1 / (obj.n_states - 2);  % Low probability for others
                        end
                    end
                end
            end

            % C_vector: Observation preferences
            obj.C_vector = zeros(obj.n_observations, 1);
            for o = 1:obj.n_observations
                if o == 1
                    obj.C_vector(o) = 0.0;  % Lower energy for preferred observation
                else
                    obj.C_vector(o) = 0.5;  % Higher energy for others
                end
            end

            % D_vector: Prior beliefs
            obj.D_vector = ones(obj.n_states, 1) / obj.n_states;  % Uniform prior
        end

        function obj = updateBeliefs(obj, observation)
            % Update beliefs using Bayesian inference
            % P(s|o) ∝ P(o|s) * P(s)

            % Get likelihood for this observation
            likelihood = obj.A_matrix(observation, :)';

            % Compute posterior: P(s|o) ∝ P(o|s) * P(s)
            posterior = likelihood .* obj.beliefs;

            % Normalize
            total = sum(posterior);
            if total > 0
                obj.beliefs = posterior / total;
            end

            % Store in history
            obj.belief_history{end+1} = obj.beliefs;
            obj.observation_history(end+1) = observation;
        end

        function action = selectAction(obj)
            % Select action by minimizing expected free energy

            min_efe = inf;
            best_action = 1;

            for a = 1:obj.n_actions
                % Predict beliefs after action
                predicted_beliefs = obj.predictBeliefs(a);

                % Calculate expected free energy
                efe = obj.calculateExpectedFreeEnergy(predicted_beliefs);

                if efe < min_efe
                    min_efe = efe;
                    best_action = a;
                end
            end

            action = best_action;

            % Store action in history
            obj.action_history(end+1) = action;
        end

        function predicted_beliefs = predictBeliefs(obj, action)
            % Predict beliefs after taking an action

            predicted_beliefs = zeros(obj.n_states, 1);

            % Get transition matrix for this action
            transition_matrix = squeeze(obj.B_matrix(:, :, action));

            % Compute predicted beliefs: P(s') = sum_s P(s'|s,a) * P(s)
            for s_next = 1:obj.n_states
                predicted_beliefs(s_next) = sum(transition_matrix(s_next, :) .* obj.beliefs');
            end
        end

        function efe = calculateExpectedFreeEnergy(obj, predicted_beliefs)
            % Calculate expected free energy for predicted beliefs

            efe = 0;

            for s = 1:obj.n_states
                if predicted_beliefs(s) > 0
                    % KL divergence between predicted beliefs and prior
                    efe = efe + predicted_beliefs(s) * log(predicted_beliefs(s) / obj.D_vector(s));
                end
            end

            % Weight by precision
            efe = efe * obj.precision;
        end

        function fe = calculateFreeEnergy(obj)
            % Calculate current variational free energy

            fe = 0;

            for s = 1:obj.n_states
                if obj.beliefs(s) > 0
                    fe = fe + obj.beliefs(s) * log(obj.beliefs(s) / obj.D_vector(s));
                end
            end

            % Store in history
            obj.free_energy_history(end+1) = fe;
        end

        function [obj, action] = step(obj, observation)
            % Execute one perception-action cycle

            % Update beliefs based on observation
            obj = obj.updateBeliefs(observation);

            % Select action
            action = obj.selectAction();

            % Calculate free energy
            obj.calculateFreeEnergy();
        end

        function obj = learn(obj, observation, action, next_observation)
            % Learn from experience (simplified learning rule)

            % Update A_matrix (observation likelihood)
            learning_rate = obj.learning_rate;
            obs_row = obj.A_matrix(observation, :);

            % Simple learning: reinforce the observed state
            [~, max_state] = max(obj.beliefs);
            obj.A_matrix(observation, max_state) = obj.A_matrix(observation, max_state) + learning_rate;

            % Renormalize row
            obj.A_matrix(observation, :) = obj.A_matrix(observation, :) / sum(obj.A_matrix(observation, :));
        end

        function entropy = calculateBeliefEntropy(obj)
            % Calculate entropy of current belief distribution

            entropy = 0;
            for s = 1:obj.n_states
                if obj.beliefs(s) > 0
                    entropy = entropy - obj.beliefs(s) * log(obj.beliefs(s));
                end
            end
        end

        function plotBeliefs(obj, title_text)
            % Plot belief evolution over time

            if nargin < 2
                title_text = 'Active Inference Belief Evolution';
            end

            figure;
            hold on;

            n_steps = length(obj.belief_history);
            belief_matrix = zeros(obj.n_states, n_steps);

            for t = 1:n_steps
                belief_matrix(:, t) = obj.belief_history{t};
            end

            plot(1:n_steps, belief_matrix');
            xlabel('Time Step');
            ylabel('Belief Probability');
            title(title_text);
            legend(arrayfun(@(x) sprintf('State %d', x), 1:obj.n_states, 'UniformOutput', false));
            grid on;
            hold off;
        end

        function printStatistics(obj)
            % Print agent statistics

            fprintf('Active Inference Agent Statistics:\n');
            fprintf('=====================================\n');
            fprintf('States: %d, Observations: %d, Actions: %d\n', ...
                obj.n_states, obj.n_observations, obj.n_actions);
            fprintf('Precision: %.2f, Learning Rate: %.2f\n', ...
                obj.precision, obj.learning_rate);

            if ~isempty(obj.action_history)
                fprintf('Total steps: %d\n', length(obj.action_history));
                fprintf('Final beliefs: [');
                for s = 1:obj.n_states
                    fprintf('%.3f', obj.beliefs(s));
                    if s < obj.n_states
                        fprintf(', ');
                    end
                end
                fprintf(']\n');

                if ~isempty(obj.free_energy_history)
                    fprintf('Final free energy: %.4f\n', obj.free_energy_history(end));
                end

                entropy = obj.calculateBeliefEntropy();
                fprintf('Belief entropy: %.4f\n', entropy);
            else
                fprintf('No steps taken yet.\n');
            end
        end
    end
end
