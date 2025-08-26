# Active Inference Implementation in Java

This directory contains a Java implementation of active inference with ant colony simulation, demonstrating swarm intelligence and multi-agent coordination.

## Overview

The Java implementation provides:
- Object-oriented design with comprehensive APIs
- Multi-agent ant colony simulation
- Thread-safe concurrent processing
- Rich visualization capabilities

## Core Components

- **AntColony.java**: Complete ant colony simulation with active inference agents

## Architecture

### Ant Colony Framework
The implementation features a sophisticated multi-agent system:

#### Ant Agent Structure
```java
class Ant {
    private double freeEnergy;
    private Map<String, Double> beliefs;
    private Map<String, Double> observations;
    private Map<String, Double> priors;
    private final double precision;
}
```

#### Colony Environment
```java
class AntColony {
    private final List<Ant> ants;
    private final Map<String, Double> environment;
    private final Random random;
}
```

## Dependencies

- Java 11+
- Standard Java library only

## Building and Running

```bash
# Compile the implementation
javac *.java

# Run the simulation
java AntColony

# With custom parameters
java AntColony 100 50  # 100 steps, 50 ants
```

## Configuration

Simulation parameters can be modified in the source code:

```java
// Environment parameters
private static final int GRID_SIZE = 20;
private static final int NUM_ANTS = 10;
private static final int NUM_FOOD_SOURCES = 5;
private static final double EVAPORATION_RATE = 0.9;

// Agent parameters
private static final double LEARNING_RATE = 0.1;
private static final double PRECISION = 1.0;
private static final double UNCERTAINTY_WEIGHT = 0.1;
```

## Core Algorithms

### Belief Update Mechanism
```java
public void updateBeliefs(Map<String, Double> newObservations) {
    // Bayesian belief updating
    // Likelihood calculation
    // Posterior normalization
}
```

### Free Energy Minimization
```java
public void minimizeFreeEnergy() {
    // Variational free energy calculation
    // Policy selection via EFE minimization
    // Action execution
}
```

### Action Selection
```java
public String selectAction() {
    // Calculate expected free energy for each action
    // Select action with minimum EFE
    // Return optimal action
}
```

## Multi-Agent Dynamics

### Swarm Intelligence
- **Pheromone Communication**: Indirect coordination through environment
- **Foraging Behavior**: Active inference guided food collection
- **Nest Maintenance**: Home pheromone trail following
- **Task Allocation**: Emergent division of labor

### Environmental Interaction
- **Dynamic Environment**: Changing resource availability
- **Pheromone Dynamics**: Evaporation and diffusion
- **Obstacle Avoidance**: Navigation around barriers
- **Resource Competition**: Multiple agents competing for resources

## Performance Characteristics

### Time Complexity
- **Belief Updates**: O(n) where n is number of states
- **Free Energy Calculation**: O(n²) for matrix operations
- **Action Selection**: O(a) where a is number of actions
- **Multi-Agent Simulation**: O(m * t) where m is agents, t is time steps

### Memory Usage
- **Per Agent**: O(n²) for generative model matrices
- **Environment**: O(g²) where g is grid size
- **Pheromone Grid**: O(g²) for spatial pheromone representation

## Output and Analysis

The implementation generates:
- Real-time simulation progress
- Final statistics summary
- Agent performance metrics
- Environmental state information
- Convergence analysis

## Extensions

### Advanced Features
- **Graphical Interface**: Swing-based visualization
- **Distributed Simulation**: Multi-machine coordination
- **Real-time Interaction**: Human-in-the-loop control
- **Parameter Optimization**: Genetic algorithm tuning

### Integration Options
- **Database Persistence**: Store simulation results
- **REST API**: Web-based control interface
- **Machine Learning**: Integration with ML frameworks
- **Robotics**: Real robot control interfaces

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Java Resources
1. **Effective Java**: Best practices and design patterns
2. **Java Concurrency in Practice**: Multi-threaded programming
3. **Java Performance**: Optimization techniques and profiling
