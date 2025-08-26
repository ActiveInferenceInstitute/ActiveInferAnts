# Active Inference in C#

A modern, type-safe implementation of the Active Inference framework using C# 12.0 with .NET 8.0, featuring async/await, records, pattern matching, and comprehensive error handling.

## Overview

This C# implementation provides:

- 🛡️ **Type Safety**: Strong typing with records and modern C# features
- ⚡ **Asynchronous Processing**: Async/await for concurrent operations
- 📊 **Comprehensive Monitoring**: Detailed logging and performance metrics
- 🧪 **Error Handling**: Custom exception types with rich context
- 🎯 **Modern C#**: Records, pattern matching, LINQ, and more

## Features

### Core Components

- **`ActiveInferenceAgent`**: Main agent with async belief updating and policy selection
- **`AntColonyEnvironment`**: Multi-agent environment with pheromone communication
- **Custom Exception Types**: `ActiveInferenceException`, `BeliefUpdateError`, `PolicySelectionError`
- **LINQ Integration**: Functional programming with C# query syntax
- **Dependency Injection**: Clean architecture with Microsoft.Extensions.DI

### Mathematical Foundations

The implementation uses a complete generative model:

- **A Matrix**: Likelihood mapping `p(o|s)` - probability of observations given states
- **B Matrix**: Transition model `p(s'|s,a)` - state transitions given actions
- **C Vector**: Preferences `p(o)` - preferred observations
- **D Vector**: Prior beliefs `p(s)` - initial state beliefs

## Installation

### Prerequisites

- **.NET 8.0 SDK**: Download from [Microsoft](https://dotnet.microsoft.com/download)
- **C# 12.0**: Included with .NET 8.0

### Building

```bash
# Navigate to the C# directory
cd ActiveInferAnts/0_CONTEXT/Computer_Languages/CSharp

# Restore packages
dotnet restore

# Build the project
dotnet build

# Run the demo
dotnet run
```

### Dependencies

- **MathNet.Numerics**: Linear algebra and mathematical functions
- **Newtonsoft.Json**: JSON serialization for data persistence
- **Microsoft.Extensions.Logging**: Comprehensive logging framework
- **Microsoft.Extensions.DependencyInjection**: Dependency injection container

## Core Concepts

### Type-Safe Agent Configuration

```csharp
var config = new AgentConfig
{
    NStates = 3,
    NObservations = 3,
    NActions = 3,
    LearningRate = 0.1,
    UncertaintyWeight = 0.1,
    Precision = 1.0,
    EnableLogging = false,
    OutputDirectory = "output"
};
```

### Asynchronous Perception-Action Cycle

```csharp
var agent = new ActiveInferenceAgent(config, logger);

// Async perception-action loop
var observation = 1;
var action = await agent.StepAsync(observation);

Console.WriteLine($"Selected action: {action}");
Console.WriteLine($"Free energy: {agent.CalculateVariationalFreeEnergy()}");
```

### Error Handling with Custom Exceptions

```csharp
try
{
    var action = await agent.StepAsync(observation);
    Console.WriteLine($"Action selected: {action}");
}
catch (BeliefUpdateError e)
{
    Console.WriteLine($"Belief update failed: {e.Message}");
}
catch (PolicySelectionError e)
{
    Console.WriteLine($"Policy selection failed: {e.Message}");
}
```

## Mathematical Foundations

### Free Energy Minimization

Active inference minimizes variational free energy:

```
F = E_q[ln q(s) - ln p(o,s)]
```

Where:
- `q(s)`: Current beliefs about hidden states
- `p(o,s)`: Generative model likelihood

### Expected Free Energy

Actions are selected by minimizing expected free energy:

```
G(π) = E_{q(s'|π)}[ln q(s'|π) - ln p(o'|s')] + γ H[q(s'|π)]
```

## Examples

### Single Agent Demo

```bash
dotnet run --single-agent
```

Shows a single active inference agent learning through interaction.

### Multi-Agent Simulation

```csharp
var config = new AntColonyEnvironment.EnvironmentConfig
{
    GridSize = 10,
    NAnts = 8,
    FoodSources = 3,
    PheromoneDecay = 0.95,
    MaxSteps = 100,
    OutputDirectory = "output"
};

var environment = new AntColonyEnvironment(config, logger);
await environment.SaveResultsAsync("output");
```

## Architecture

### Project Structure

```
CSharp/
├── ActiveInference.csproj          # Project configuration
├── Program.cs                      # Main agent implementation
├── Demo.cs                         # Demo and environment
└── output/                         # Generated results (created automatically)
    ├── ant_colony/
    │   ├── simulation_results.json
    │   ├── pheromone_grid.csv
    │   └── food_grid.csv
    └── single_agent/
        ├── statistics.json
        ├── belief_history.csv
        └── action_history.csv
```

### Key Classes

#### `ActiveInferenceAgent`

Main agent class implementing active inference:

- **Async Methods**: Non-blocking belief updates and policy selection
- **Type Safety**: Full type checking with modern C# features
- **Error Handling**: Comprehensive exception safety
- **Performance Monitoring**: Detailed statistics tracking
- **LINQ Integration**: Functional programming capabilities

#### Custom Exception Hierarchy

```csharp
public class ActiveInferenceException : Exception
{
    public ActiveInferenceException(string message) : base(message) { }
}

public class BeliefUpdateError : ActiveInferenceException
{
    // Specialized for belief updating failures
}

public class PolicySelectionError : ActiveInferenceException
{
    // Specialized for policy selection failures
}
```

## Performance

### Benchmarks

- **Async Operations**: Efficient concurrent processing
- **Matrix Operations**: MathNet.Numerics optimized linear algebra
- **Memory Usage**: Efficient data structures with proper disposal
- **Serialization**: Fast JSON output for result persistence

### Optimization Features

- **Parallel Processing**: Multi-agent simulations with Parallel.ForEach
- **Lazy Evaluation**: On-demand computation of complex metrics
- **Efficient Data Structures**: MathNet matrices for numerical operations
- **Memory Pooling**: Reused data structures to minimize GC pressure

## Advanced Features

### Records and Pattern Matching

```csharp
// Modern C# record types
public record FreeEnergy
{
    public double Variational { get; init; }
    public double Expected { get; init; }
    public double Pragmatic { get; init; }
    public double Epistemic { get; init; }
}

// Pattern matching for configuration validation
public void Validate() => (NStates, NObservations, NActions) switch
{
    (<= 0, _, _) => throw new ArgumentException("States must be positive"),
    (_, <= 0, _) => throw new ArgumentException("Observations must be positive"),
    (_, _, <= 0) => throw new ArgumentException("Actions must be positive"),
    _ => { } // Valid configuration
};
```

### Asynchronous Processing

```csharp
public async Task<Vector<double>> UpdateBeliefsAsync(int observation)
{
    return await Task.Run(() =>
    {
        // Complex belief updating logic
        var likelihood = GetObservationLikelihood(observation);
        var posterior = _currentBeliefs.PointwiseMultiply(likelihood);
        return posterior / posterior.Sum();
    });
}
```

### Comprehensive Statistics

```csharp
var statistics = agent.GetStatistics();
Console.WriteLine($"Total steps: {statistics.TotalSteps}");
Console.WriteLine($"Average free energy: {statistics.AverageFreeEnergy:F4}");
Console.WriteLine($"Action distribution: {string.Join(", ", statistics.ActionDistribution.Select(d => d:F3))}");
```

## Output Files

### Single Agent Results

- **`statistics.json`**: Complete agent statistics and configuration
- **`belief_history.csv`**: Time series of belief states
- **`action_history.csv`**: Sequence of selected actions

### Multi-Agent Results

- **`simulation_results.json`**: Complete simulation data with all steps
- **`pheromone_grid.csv`**: Spatial distribution of pheromones
- **`food_grid.csv`**: Food source locations and amounts

## Future Extensions

- [ ] GUI dashboard for real-time visualization
- [ ] Machine learning integration with ML.NET
- [ ] Distributed processing with Orleans
- [ ] Unity integration for 3D simulations
- [ ] Performance profiling and optimization
- [ ] Advanced learning mechanisms (meta-learning)

## Contributing

### Development Guidelines

1. **Modern C#**: Use C# 12.0 features and patterns
2. **Type Safety**: All code must pass strict type checking
3. **Async/Await**: Use asynchronous programming where appropriate
4. **Error Handling**: Comprehensive exception handling
5. **Documentation**: XML documentation comments for all public APIs
6. **Testing**: Unit tests with xUnit and coverage analysis

### Code Style

- Follow .NET coding conventions
- Use records for immutable data
- Implement proper async/await patterns
- Include comprehensive error handling
- Maintain type safety throughout

## References

### Key Papers

1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### C# Resources

1. **C# Language Reference**: Official Microsoft documentation
2. **.NET Architecture Guides**: Best practices and patterns
3. **Math.NET Numerics**: Mathematical computing library

## License

MIT License - see LICENSE file for details.
