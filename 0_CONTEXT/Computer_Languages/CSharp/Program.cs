using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using MathNet.Numerics.LinearAlgebra;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.DependencyInjection;
using Newtonsoft.Json;

namespace ActiveInference;

/// <summary>
/// Configuration for Active Inference Agent
/// </summary>
public record AgentConfig
{
    public int NStates { get; init; } = 3;
    public int NObservations { get; init; } = 3;
    public int NActions { get; init; } = 3;
    public double LearningRate { get; init; } = 0.1;
    public double UncertaintyWeight { get; init; } = 0.1;
    public double Precision { get; init; } = 1.0;
    public bool EnableLogging { get; init; } = false;
    public string OutputDirectory { get; init; } = "output";

    public void Validate()
    {
        if (NStates <= 0) throw new ArgumentException("Number of states must be positive");
        if (NObservations <= 0) throw new ArgumentException("Number of observations must be positive");
        if (NActions <= 0) throw new ArgumentException("Number of actions must be positive");
        if (LearningRate <= 0 || LearningRate > 1) throw new ArgumentException("Learning rate must be in (0, 1]");
        if (UncertaintyWeight < 0) throw new ArgumentException("Uncertainty weight must be non-negative");
        if (Precision <= 0) throw new ArgumentException("Precision must be positive");
    }
}

/// <summary>
/// Free energy components
/// </summary>
public record FreeEnergy
{
    public double Variational { get; init; }
    public double Expected { get; init; }
    public double Pragmatic { get; init; }
    public double Epistemic { get; init; }

    public static FreeEnergy Zero => new FreeEnergy
    {
        Variational = 0.0,
        Expected = 0.0,
        Pragmatic = 0.0,
        Epistemic = 0.0
    };
}

/// <summary>
/// Agent statistics for analysis
/// </summary>
public record AgentStatistics
{
    public int TotalSteps { get; init; }
    public double AverageFreeEnergy { get; init; }
    public double[] ActionDistribution { get; init; } = Array.Empty<double>();
    public double[] FinalBeliefs { get; init; } = Array.Empty<double>();
    public DateTime Timestamp { get; init; } = DateTime.UtcNow;
}

/// <summary>
/// Custom exception for Active Inference operations
/// </summary>
public class ActiveInferenceException : Exception
{
    public ActiveInferenceException(string message) : base(message) { }
    public ActiveInferenceException(string message, Exception inner) : base(message, inner) { }
}

/// <summary>
/// Active Inference Agent implementation
/// </summary>
public class ActiveInferenceAgent
{
    private readonly ILogger<ActiveInferenceAgent> _logger;
    private readonly AgentConfig _config;
    private readonly Matrix<double> _A; // Likelihood matrix p(o|s)
    private readonly Matrix<double>[] _B; // Transition matrices p(s'|s,a)
    private readonly Vector<double> _C; // Preferences p(o)
    private readonly Vector<double> _D; // Prior beliefs p(s)

    private Vector<double> _currentBeliefs;
    private readonly List<Vector<double>> _beliefHistory = new();
    private readonly List<int> _actionHistory = new();
    private readonly List<int> _observationHistory = new();
    private readonly List<double> _freeEnergyHistory = new();
    private readonly List<DateTime> _timestampHistory = new();

    public ActiveInferenceAgent(AgentConfig config, ILogger<ActiveInferenceAgent> logger)
    {
        _config = config;
        _config.Validate();
        _logger = logger;

        _A = InitializeLikelihoodMatrix();
        _B = InitializeTransitionMatrices();
        _C = InitializePreferenceVector();
        _D = InitializePriorVector();

        _currentBeliefs = _D.Clone();

        _logger.LogInformation("Active Inference Agent initialized with {NStates} states, {NObservations} observations, {NActions} actions",
            _config.NStates, _config.NObservations, _config.NActions);
    }

    /// <summary>
    /// Initialize likelihood matrix A (p(o|s))
    /// </summary>
    private Matrix<double> InitializeLikelihoodMatrix()
    {
        var matrix = Matrix<double>.Build.Dense(_config.NObservations, _config.NStates);
        var random = new Random(42); // For reproducible results

        for (int obs = 0; obs < _config.NObservations; obs++)
        {
            var row = Vector<double>.Build.Dense(_config.NStates);

            for (int state = 0; state < _config.NStates; state++)
            {
                // Diagonal structure with noise
                var isDiagonal = obs == state % _config.NObservations;
                var baseProb = isDiagonal ? 0.7 : 0.1;
                var noise = (random.NextDouble() - 0.5) * 0.2;
                row[state] = Math.Max(0.0, Math.Min(1.0, baseProb + noise));
            }

            // Normalize row
            row = row / row.Sum();
            matrix.SetRow(obs, row);
        }

        return matrix;
    }

    /// <summary>
    /// Initialize transition matrices B (p(s'|s,a))
    /// </summary>
    private Matrix<double>[] InitializeTransitionMatrices()
    {
        var matrices = new Matrix<double>[_config.NActions];
        var random = new Random(42);

        for (int action = 0; action < _config.NActions; action++)
        {
            var matrix = Matrix<double>.Build.Dense(_config.NStates, _config.NStates);

            for (int fromState = 0; fromState < _config.NStates; fromState++)
            {
                var row = Vector<double>.Build.Dense(_config.NStates, 0.1);

                // Action-specific transition patterns
                switch (action)
                {
                    case 0: // Stay/move left
                        row[fromState] = 0.6; // Stay
                        if (fromState > 0)
                            row[fromState - 1] = 0.3; // Move left
                        break;
                    case 1: // Move right
                        if (fromState < _config.NStates - 1)
                            row[fromState + 1] = 0.6; // Move right
                        else
                            row[fromState] = 0.6; // Stay if at boundary
                        break;
                    default: // Random exploration
                        row = Vector<double>.Build.Dense(_config.NStates, 1.0 / _config.NStates);
                        break;
                }

                // Normalize row
                row = row / row.Sum();
                matrix.SetRow(fromState, row);
            }

            matrices[action] = matrix;
        }

        return matrices;
    }

    /// <summary>
    /// Initialize preference vector C (p(o))
    /// </summary>
    private Vector<double> InitializePreferenceVector()
    {
        var vector = Vector<double>.Build.Dense(_config.NObservations);

        for (int obs = 0; obs < _config.NObservations; obs++)
        {
            // Prefer certain observations (e.g., food, safety)
            vector[obs] = obs < _config.NObservations / 2 ? 1.0 : 0.1;
        }

        return vector;
    }

    /// <summary>
    /// Initialize prior belief vector D (p(s))
    /// </summary>
    private Vector<double> InitializePriorVector()
    {
        return Vector<double>.Build.Dense(_config.NStates, 1.0 / _config.NStates);
    }

    /// <summary>
    /// Update beliefs given an observation
    /// </summary>
    public async Task<Vector<double>> UpdateBeliefsAsync(int observation)
    {
        return await Task.Run(() =>
        {
            if (observation < 0 || observation >= _config.NObservations)
                throw new ActiveInferenceException($"Invalid observation index: {observation}");

            try
            {
                // Get likelihood for this observation
                var likelihood = _A.Row(observation);

                // Bayesian update: posterior = prior * likelihood
                var posterior = _currentBeliefs.PointwiseMultiply(likelihood);

                // Normalize
                var sum = posterior.Sum();
                if (sum == 0.0)
                    throw new ActiveInferenceException("Invalid likelihood - posterior sums to zero");

                _currentBeliefs = posterior / sum;

                // Record in history
                _beliefHistory.Add(_currentBeliefs.Clone());
                _timestampHistory.Add(DateTime.UtcNow);

                if (_config.EnableLogging)
                    _logger.LogInformation("Beliefs updated for observation {Observation}", observation);

                return _currentBeliefs.Clone();
            }
            catch (Exception ex)
            {
                throw new ActiveInferenceException($"Failed to update beliefs: {ex.Message}", ex);
            }
        });
    }

    /// <summary>
    /// Calculate variational free energy
    /// </summary>
    public double CalculateVariationalFreeEnergy()
    {
        var expectedLikelihood = CalculateExpectedLikelihood();
        var entropy = CalculateEntropy(_currentBeliefs);

        return -expectedLikelihood - entropy;
    }

    /// <summary>
    /// Calculate expected free energy for an action
    /// </summary>
    public FreeEnergy CalculateExpectedFreeEnergy(int action)
    {
        if (action < 0 || action >= _config.NActions)
            throw new ActiveInferenceException($"Invalid action index: {action}");

        try
        {
            // Predict next beliefs
            var predictedBeliefs = PredictBeliefs(action);

            // Calculate pragmatic value (surprise about preferred observations)
            var pragmaticValue = CalculatePragmaticValue(predictedBeliefs);

            // Calculate epistemic value (information gain)
            var epistemicValue = CalculateEpistemicValue(predictedBeliefs);

            // Total EFE
            var expectedFE = pragmaticValue - _config.UncertaintyWeight * epistemicValue;

            return new FreeEnergy
            {
                Variational = CalculateVariationalFreeEnergy(),
                Expected = expectedFE,
                Pragmatic = pragmaticValue,
                Epistemic = epistemicValue
            };
        }
        catch (Exception ex)
        {
            throw new ActiveInferenceException($"Failed to calculate expected free energy: {ex.Message}", ex);
        }
    }

    /// <summary>
    /// Select the best action by minimizing expected free energy
    /// </summary>
    public async Task<int> SelectActionAsync()
    {
        return await Task.Run(() =>
        {
            try
            {
                var efes = new FreeEnergy[_config.NActions];

                // Calculate EFE for each action
                for (int action = 0; action < _config.NActions; action++)
                {
                    efes[action] = CalculateExpectedFreeEnergy(action);
                }

                // Select action with minimum expected free energy
                var bestAction = 0;
                var minEFE = efes[0].Expected;

                for (int action = 1; action < _config.NActions; action++)
                {
                    if (efes[action].Expected < minEFE)
                    {
                        minEFE = efes[action].Expected;
                        bestAction = action;
                    }
                }

                if (_config.EnableLogging)
                    _logger.LogInformation("Action {Action} selected with EFE {EFE}", bestAction, minEFE);

                return bestAction;
            }
            catch (Exception ex)
            {
                throw new ActiveInferenceException($"Failed to select action: {ex.Message}", ex);
            }
        });
    }

    /// <summary>
    /// Execute one step of the perception-action loop
    /// </summary>
    public async Task<int> StepAsync(int observation)
    {
        // Update beliefs based on observation
        await UpdateBeliefsAsync(observation);

        // Calculate free energy
        var fe = CalculateVariationalFreeEnergy();
        _freeEnergyHistory.Add(fe);

        // Select and return action
        var action = await SelectActionAsync();
        RecordHistory(action, observation);

        return action;
    }

    /// <summary>
    /// Get agent statistics
    /// </summary>
    public AgentStatistics GetStatistics()
    {
        var actionCounts = new double[_config.NActions];
        if (_actionHistory.Count > 0)
        {
            foreach (var action in _actionHistory)
            {
                if (action >= 0 && action < _config.NActions)
                    actionCounts[action]++;
            }

            // Convert to frequencies
            for (int i = 0; i < _config.NActions; i++)
                actionCounts[i] /= _actionHistory.Count;
        }

        return new AgentStatistics
        {
            TotalSteps = _actionHistory.Count,
            AverageFreeEnergy = _freeEnergyHistory.Count > 0
                ? _freeEnergyHistory.Average()
                : 0.0,
            ActionDistribution = actionCounts,
            FinalBeliefs = _currentBeliefs.ToArray(),
            Timestamp = DateTime.UtcNow
        };
    }

    /// <summary>
    /// Save results to output directory
    /// </summary>
    public async Task SaveResultsAsync()
    {
        await Task.Run(() =>
        {
            try
            {
                Directory.CreateDirectory(_config.OutputDirectory);

                // Save statistics
                var statistics = GetStatistics();
                var jsonPath = Path.Combine(_config.OutputDirectory, "statistics.json");
                File.WriteAllText(jsonPath, JsonConvert.SerializeObject(statistics, Formatting.Indented));

                // Save belief history
                var beliefHistoryPath = Path.Combine(_config.OutputDirectory, "belief_history.csv");
                using (var writer = new StreamWriter(beliefHistoryPath))
                {
                    writer.WriteLine("Step,State0,State1,State2"); // Assuming 3 states
                    for (int i = 0; i < _beliefHistory.Count; i++)
                    {
                        var beliefs = _beliefHistory[i];
                        writer.Write($"{i}");
                        for (int j = 0; j < beliefs.Count; j++)
                        {
                            writer.Write($",{beliefs[j]:F4}");
                        }
                        writer.WriteLine();
                    }
                }

                // Save action history
                var actionHistoryPath = Path.Combine(_config.OutputDirectory, "action_history.csv");
                File.WriteAllLines(actionHistoryPath,
                    _actionHistory.Select((action, i) => $"{i},{action}"));

                // Save configuration
                var configPath = Path.Combine(_config.OutputDirectory, "config.json");
                File.WriteAllText(configPath, JsonConvert.SerializeObject(_config, Formatting.Indented));

                if (_config.EnableLogging)
                    _logger.LogInformation("Results saved to {OutputDirectory}", _config.OutputDirectory);
            }
            catch (Exception ex)
            {
                throw new ActiveInferenceException($"Failed to save results: {ex.Message}", ex);
            }
        });
    }

    // Helper methods
    private Vector<double> PredictBeliefs(int action) => _currentBeliefs * _B[action];

    private double CalculatePragmaticValue(Vector<double> predictedBeliefs)
    {
        var pragmaticValue = 0.0;

        for (int state = 0; state < _config.NStates; state++)
        {
            var stateProb = predictedBeliefs[state];
            if (stateProb > 0.0)
            {
                for (int obs = 0; obs < _config.NObservations; obs++)
                {
                    var obsProb = _A[obs, state];
                    var preference = _C[obs];
                    pragmaticValue += stateProb * obsProb * preference;
                }
            }
        }

        return pragmaticValue;
    }

    private double CalculateEpistemicValue(Vector<double> predictedBeliefs)
        => CalculateEntropy(predictedBeliefs);

    private double CalculateEntropy(Vector<double> beliefs)
    {
        var entropy = 0.0;
        for (int i = 0; i < beliefs.Count; i++)
        {
            var prob = beliefs[i];
            if (prob > 0.0)
                entropy -= prob * Math.Log(prob, 2.0);
        }
        return entropy;
    }

    private double CalculateExpectedLikelihood()
    {
        var expectedLikelihood = 0.0;

        for (int obs = 0; obs < _config.NObservations; obs++)
        {
            var likelihood = _A.Row(obs);
            var expectedObsProb = _currentBeliefs.DotProduct(likelihood);
            if (expectedObsProb > 0.0)
                expectedLikelihood += expectedObsProb * Math.Log(expectedObsProb);
        }

        return expectedLikelihood;
    }

    private void RecordHistory(int action, int observation)
    {
        _actionHistory.Add(action);
        _observationHistory.Add(observation);
    }

    // Public properties for access
    public Vector<double> CurrentBeliefs => _currentBeliefs.Clone();
    public Matrix<double> A => _A.Clone();
    public Matrix<double>[] B => _B.Select(m => m.Clone()).ToArray();
    public Vector<double> C => _C.Clone();
    public Vector<double> D => _D.Clone();
}

/// <summary>
/// Main program entry point
/// </summary>
class Program
{
    static async Task Main(string[] args)
    {
        await Demo.MainAsync();
    }
}
