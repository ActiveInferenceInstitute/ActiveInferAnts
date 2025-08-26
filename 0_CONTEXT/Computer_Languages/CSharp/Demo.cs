using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.DependencyInjection;
using Newtonsoft.Json;

namespace ActiveInference;

/// <summary>
/// Ant Colony Environment for multi-agent simulation
/// </summary>
public class AntColonyEnvironment
{
    public record Position(int X, int Y);
    public record PheromoneLevels(double Home, double Food);

    public record AntAgent
    {
        public int Id { get; init; }
        public Position Position { get; set; }
        public ActiveInferenceAgent Agent { get; init; }
        public bool CarryingFood { get; set; }
        public double Energy { get; set; }

        public AntAgent(int id, Position pos, ActiveInferenceAgent agent)
        {
            Id = id;
            Position = pos;
            Agent = agent;
            CarryingFood = false;
            Energy = 100.0;
        }
    }

    public record EnvironmentConfig
    {
        public int GridSize { get; init; } = 8;
        public int NAnts { get; init; } = 5;
        public int FoodSources { get; init; } = 3;
        public double PheromoneDecay { get; init; } = 0.95;
        public int MaxSteps { get; init; } = 100;
        public string OutputDirectory { get; init; } = "output";

        public void Validate()
        {
            if (GridSize <= 0 || NAnts <= 0 || FoodSources < 0)
                throw new ArgumentException("Invalid environment configuration");
        }
    }

    public record SimulationStep
    {
        public int Step { get; init; }
        public double TotalPheromones { get; init; }
        public int FoodCollected { get; init; }
        public Position[] AntPositions { get; init; } = Array.Empty<Position>();
        public double AverageFreeEnergy { get; init; }
        public DateTime Timestamp { get; init; } = DateTime.UtcNow;
    }

    private readonly EnvironmentConfig _config;
    private readonly ILogger<AntColonyEnvironment> _logger;
    private readonly PheromoneLevels[,] _pheromoneGrid;
    private readonly double[,] _foodGrid;
    private readonly AntAgent[] _ants;
    private readonly Position[] _foodLocations;
    private readonly Random _random = new(42);

    public AntColonyEnvironment(EnvironmentConfig config, ILogger<AntColonyEnvironment> logger)
    {
        _config = config;
        _config.Validate();
        _logger = logger;

        _pheromoneGrid = new PheromoneLevels[_config.GridSize, _config.GridSize];
        _foodGrid = new double[_config.GridSize, _config.GridSize];
        _ants = new AntAgent[_config.NAnts];
        _foodLocations = new Position[_config.FoodSources];

        InitializeEnvironment();
        InitializeAnts();

        _logger.LogInformation("Ant Colony Environment initialized with {NAnts} ants on {GridSize}x{GridSize} grid",
            _config.NAnts, _config.GridSize, _config.GridSize);
    }

    private void InitializeEnvironment()
    {
        // Initialize grids
        for (int y = 0; y < _config.GridSize; y++)
        {
            for (int x = 0; x < _config.GridSize; x++)
            {
                _pheromoneGrid[y, x] = new PheromoneLevels(0.0, 0.0);
            }
        }

        // Place food sources
        for (int i = 0; i < _config.FoodSources; i++)
        {
            var pos = GetRandomPosition();
            _foodGrid[pos.Y, pos.X] = 10.0;
            _foodLocations[i] = pos;
        }
    }

    private void InitializeAnts()
    {
        var agentConfig = new AgentConfig
        {
            NStates = 4,
            NObservations = 3,
            NActions = 4,
            UncertaintyWeight = 0.2,
            EnableLogging = false,
            OutputDirectory = Path.Combine(_config.OutputDirectory, "ants")
        };

        for (int i = 0; i < _config.NAnts; i++)
        {
            var pos = GetRandomPosition();
            var agent = new ActiveInferenceAgent(agentConfig, _logger);
            _ants[i] = new AntAgent(i, pos, agent);
        }
    }

    private Position GetRandomPosition()
    {
        return new Position(
            _random.Next(_config.GridSize),
            _random.Next(_config.GridSize)
        );
    }

    private int GenerateObservation(Position position)
    {
        var (x, y) = position;
        double foodNearby = 0.0;
        double pheromoneHome = 0.0;
        double pheromoneFood = 0.0;

        // Check neighboring cells
        for (int dy = -1; dy <= 1; dy++)
        {
            for (int dx = -1; dx <= 1; dx++)
            {
                var nx = x + dx;
                var ny = y + dy;

                if (nx >= 0 && nx < _config.GridSize && ny >= 0 && ny < _config.GridSize)
                {
                    foodNearby = Math.Max(foodNearby, _foodGrid[ny, nx]);
                    pheromoneHome = Math.Max(pheromoneHome, _pheromoneGrid[ny, nx].Home);
                    pheromoneFood = Math.Max(pheromoneFood, _pheromoneGrid[ny, nx].Food);
                }
            }
        }

        // Discretize observations
        if (foodNearby > 0.0) return 0;           // Food present
        if (pheromoneFood > 0.5) return 1;      // Strong food pheromone
        if (pheromoneHome > 0.5) return 2;      // Strong home pheromone
        return 0;                               // Default observation
    }

    private Position ExecuteAction(Position position, int action)
    {
        var (x, y) = position;
        return action switch
        {
            0 => new Position(x, Math.Max(0, y - 1)),           // North
            1 => new Position(Math.Min(_config.GridSize - 1, x + 1), y), // East
            2 => new Position(x, Math.Min(_config.GridSize - 1, y + 1)), // South
            3 => new Position(Math.Max(0, x - 1), y),           // West
            _ => position // Stay in place for invalid actions
        };
    }

    private void LayPheromone(AntAgent ant, Position position)
    {
        var (x, y) = position;

        if (ant.CarryingFood)
        {
            _pheromoneGrid[y, x] = _pheromoneGrid[y, x] with
            {
                Food = Math.Min(1.0, _pheromoneGrid[y, x].Food + 0.1)
            };
        }
        else
        {
            _pheromoneGrid[y, x] = _pheromoneGrid[y, x] with
            {
                Home = Math.Min(1.0, _pheromoneGrid[y, x].Home + 0.1)
            };
        }
    }

    private void UpdateEnvironment()
    {
        // Decay pheromones
        for (int y = 0; y < _config.GridSize; y++)
        {
            for (int x = 0; x < _config.GridSize; x++)
            {
                _pheromoneGrid[y, x] = _pheromoneGrid[y, x] with
                {
                    Home = _pheromoneGrid[y, x].Home * _config.PheromoneDecay,
                    Food = _pheromoneGrid[y, x].Food * _config.PheromoneDecay
                };
            }
        }

        // Update ants
        Parallel.ForEach(_ants, async ant =>
        {
            try
            {
                // Generate observation
                var observation = GenerateObservation(ant.Position);

                // Agent takes action
                var action = await ant.Agent.StepAsync(observation);

                // Execute action
                var newPosition = ExecuteAction(ant.Position, action);
                ant.Position = newPosition;

                // Lay pheromone
                LayPheromone(ant, newPosition);

                // Check for food
                if (_foodGrid[newPosition.Y, newPosition.X] > 0.0)
                {
                    ant.CarryingFood = true;
                    _foodGrid[newPosition.Y, newPosition.X]--;
                    ant.Energy = Math.Min(100.0, ant.Energy + 20.0);
                }

                // Decrease energy
                ant.Energy = Math.Max(0.0, ant.Energy - 1.0);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error updating ant {Id}", ant.Id);
            }
        });
    }

    public async Task<SimulationStep[]> RunSimulationAsync()
    {
        var steps = new List<SimulationStep>();

        for (int step = 0; step < _config.MaxSteps; step++)
        {
            UpdateEnvironment();

            // Collect statistics
            var totalPheromones = GetTotalPheromones();
            var foodCollected = _ants.Count(ant => ant.CarryingFood);
            var antPositions = _ants.Select(ant => ant.Position).ToArray();
            var averageFreeEnergy = GetAverageFreeEnergy();

            var simulationStep = new SimulationStep
            {
                Step = step,
                TotalPheromones = totalPheromones,
                FoodCollected = foodCollected,
                AntPositions = antPositions,
                AverageFreeEnergy = averageFreeEnergy,
                Timestamp = DateTime.UtcNow
            };

            steps.Add(simulationStep);

            // Log progress
            if ((step + 1) % 10 == 0)
            {
                _logger.LogInformation("Step {Step}: Pheromones={Pheromones:F2}, Food={Food}",
                    step + 1, totalPheromones, foodCollected);
            }
        }

        return steps.ToArray();
    }

    private double GetTotalPheromones()
    {
        double total = 0.0;
        for (int y = 0; y < _config.GridSize; y++)
        {
            for (int x = 0; x < _config.GridSize; x++)
            {
                total += _pheromoneGrid[y, x].Home + _pheromoneGrid[y, x].Food;
            }
        }
        return total;
    }

    private double GetAverageFreeEnergy()
    {
        return _ants.Average(ant => ant.Agent.CalculateVariationalFreeEnergy());
    }

    public async Task SaveResultsAsync(string baseOutputDirectory)
    {
        var outputDirectory = Path.Combine(baseOutputDirectory, "ant_colony");
        Directory.CreateDirectory(outputDirectory);

        // Run simulation
        var steps = await RunSimulationAsync();

        // Save simulation results
        var resultsPath = Path.Combine(outputDirectory, "simulation_results.json");
        var results = new
        {
            Configuration = _config,
            Steps = steps,
            FinalStatistics = GetStatistics(),
            Timestamp = DateTime.UtcNow
        };
        await File.WriteAllTextAsync(resultsPath, JsonConvert.SerializeObject(results, Formatting.Indented));

        // Save pheromone grid
        var pheromonePath = Path.Combine(outputDirectory, "pheromone_grid.csv");
        using (var writer = new StreamWriter(pheromonePath))
        {
            writer.WriteLine("Y,X,HomePheromone,FoodPheromone");
            for (int y = 0; y < _config.GridSize; y++)
            {
                for (int x = 0; x < _config.GridSize; x++)
                {
                    writer.WriteLine($"{y},{x},{_pheromoneGrid[y, x].Home:F4},{_pheromoneGrid[y, x].Food:F4}");
                }
            }
        }

        // Save food grid
        var foodPath = Path.Combine(outputDirectory, "food_grid.csv");
        using (var writer = new StreamWriter(foodPath))
        {
            writer.WriteLine("Y,X,FoodAmount");
            for (int y = 0; y < _config.GridSize; y++)
            {
                for (int x = 0; x < _config.GridSize; x++)
                {
                    if (_foodGrid[y, x] > 0)
                    {
                        writer.WriteLine($"{y},{x},{_foodGrid[y, x]:F2}");
                    }
                }
            }
        }

        // Save individual ant results
        foreach (var ant in _ants)
        {
            await ant.Agent.SaveResultsAsync();
        }

        _logger.LogInformation("Ant colony results saved to {OutputDirectory}", outputDirectory);
    }

    private object GetStatistics()
    {
        return new
        {
            TotalAnts = _ants.Length,
            FoodSources = _foodLocations.Length,
            TotalPheromones = GetTotalPheromones(),
            FoodCollected = _ants.Count(ant => ant.CarryingFood),
            AverageEnergy = _ants.Average(ant => ant.Energy),
            AntDetails = _ants.Select(ant => new
            {
                ant.Id,
                ant.Position,
                ant.CarryingFood,
                Energy = ant.Energy,
                Statistics = ant.Agent.GetStatistics()
            }).ToArray()
        };
    }
}

/// <summary>
/// Standalone demo program
/// </summary>
public static class Demo
{
    public static async Task RunSingleAgentDemoAsync()
    {
        Console.WriteLine("🧠 Single Agent C# Demo");
        Console.WriteLine("======================");

        // Setup dependency injection
        var serviceProvider = ConfigureServices();
        var logger = serviceProvider.GetRequiredService<ILogger<ActiveInferenceAgent>>();

        // Create agent
        var config = new AgentConfig
        {
            NStates = 3,
            NObservations = 3,
            NActions = 3,
            UncertaintyWeight = 0.1,
            EnableLogging = true,
            OutputDirectory = "output/single_agent"
        };

        var agent = new ActiveInferenceAgent(config, logger);

        Console.WriteLine("Initial beliefs: [{0}]",
            string.Join(", ", agent.CurrentBeliefs.Select(b => b.ToString("F3"))));

        // Run perception-action cycles
        var random = new Random(42);

        for (int t = 0; t < 10; t++)
        {
            var observation = random.Next(config.NObservations);

            Console.WriteLine($"\nStep {t + 1}:");
            Console.WriteLine($"  Observation: {observation}");

            var action = await agent.StepAsync(observation);
            Console.WriteLine($"  Action: {action}");

            var beliefs = agent.CurrentBeliefs;
            Console.WriteLine($"  Beliefs: [{string.Join(", ", beliefs.Select(b => b.ToString("F3")))}]");

            var freeEnergy = agent.CalculateVariationalFreeEnergy();
            Console.WriteLine($"  Free Energy: {freeEnergy:F3}");
        }

        // Save results
        await agent.SaveResultsAsync();

        // Show statistics
        var statistics = agent.GetStatistics();
        Console.WriteLine($"\nFinal Statistics:");
        Console.WriteLine($"  Total Steps: {statistics.TotalSteps}");
        Console.WriteLine($"  Average Free Energy: {statistics.AverageFreeEnergy:F4}");
        Console.WriteLine($"  Action Distribution: [{string.Join(", ", statistics.ActionDistribution.Select(d => d.ToString("F3")))}]");
    }

    public static async Task RunAntColonyDemoAsync()
    {
        Console.WriteLine("\n🐜 Ant Colony C# Demo");
        Console.WriteLine("=====================");

        var serviceProvider = ConfigureServices();
        var logger = serviceProvider.GetRequiredService<ILogger<AntColonyEnvironment>>();

        var config = new AntColonyEnvironment.EnvironmentConfig
        {
            GridSize = 8,
            NAnts = 5,
            FoodSources = 3,
            PheromoneDecay = 0.95,
            MaxSteps = 50,
            OutputDirectory = "output"
        };

        Console.WriteLine($"Creating environment: {config.GridSize}x{config.GridSize} grid, {config.NAnts} ants, {config.FoodSources} food sources");

        var environment = new AntColonyEnvironment(config, logger);
        await environment.SaveResultsAsync("output");

        Console.WriteLine("Ant colony simulation completed!");
    }

    private static IServiceProvider ConfigureServices()
    {
        return new ServiceCollection()
            .AddLogging(builder =>
            {
                builder.AddConsole();
                builder.SetMinimumLevel(LogLevel.Information);
            })
            .BuildServiceProvider();
    }

    public static async Task MainAsync()
    {
        Console.WriteLine("🧠 Active Inference C# Implementation");
        Console.WriteLine("====================================");

        try
        {
            await RunSingleAgentDemoAsync();
            await RunAntColonyDemoAsync();

            Console.WriteLine("\n✅ All demos completed successfully!");
            Console.WriteLine("\n💡 C# Benefits Demonstrated:");
            Console.WriteLine("   • Strong type safety with records and modern syntax");
            Console.WriteLine("   • Asynchronous programming with async/await");
            Console.WriteLine("   • Comprehensive error handling with custom exceptions");
            Console.WriteLine("   • LINQ for functional programming features");
            Console.WriteLine("   • Dependency injection for clean architecture");
            Console.WriteLine("   • JSON serialization for data persistence");

        }
        catch (Exception ex)
        {
            Console.WriteLine($"❌ Demo failed: {ex.Message}");
            if (ex.InnerException != null)
            {
                Console.WriteLine($"Inner exception: {ex.InnerException.Message}");
            }
        }
    }
}
