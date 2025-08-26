# Active Inference Implementation in Julia

This directory contains a high-performance Julia implementation of active inference with probabilistic programming and scientific computing capabilities.

## Overview

The Julia implementation provides:
- High-performance scientific computing
- Probabilistic programming with RxInfer
- Category theory integration
- Advanced visualization and analysis

## Core Components

- **RxInfer_Agent_Model.jl**: RxInfer-based probabilistic active inference
- **Julia_InferAnts.jl**: Main active inference implementation
- **Category_Theory_Julia/**: Category theory foundations
- **Visualization/**: Advanced plotting and analysis tools
- **SideCar/**: Mountain Car reinforcement learning integration

## Architecture

### Multi-Level Implementation
The Julia implementation spans multiple approaches:

#### RxInfer Integration
```julia
@model function active_inference_model(observations, actions)
    # Probabilistic graphical model
    # State transitions with uncertainty
    # Observation likelihood model
end
```

#### Category Theory Foundations
```julia
struct PolynomialFunctor{T}
    # Polynomial functor implementation
    # State space transformations
    # Natural transformations
end
```

## Dependencies

- Julia 1.6+
- RxInfer.jl (probabilistic programming)
- Plots.jl (visualization)
- LinearAlgebra (matrix operations)
- Statistics (statistical analysis)

## Installing Dependencies

```julia
using Pkg
Pkg.add("RxInfer")
Pkg.add("Plots")
Pkg.add("LinearAlgebra")
Pkg.add("Statistics")
Pkg.add("Distributions")
```

## Building and Running

```julia
# Run the main implementation
julia Julia_InferAnts.jl

# Run RxInfer version
julia RxInfer_Agent_Model.jl

# Run Mountain Car integration
cd SideCar/MC_AI
julia run.jl

# Run with visualization
julia --project -e 'include("Julia_InferAnts.jl"); main()'
```

## Core Algorithms

### Belief Propagation
```julia
function belief_propagation(prior::Vector, likelihood::Matrix, observations::Vector)
    # Forward-backward algorithm
    # Message passing on factor graph
    # Posterior belief calculation
end
```

### Variational Inference
```julia
function variational_inference(model::GenerativeModel, observations::Vector)
    # Mean-field approximation
    # Free energy minimization
    # Parameter optimization
end
```

### Category Theory Operations
```julia
function compose_functors(F::PolynomialFunctor, G::PolynomialFunctor)
    # Functor composition
    # Natural transformation
    # Category theory operations
end
```

## Performance Features

### Just-In-Time Compilation
- **Fast Execution**: JIT compilation for optimal performance
- **Type Stability**: Optimized for Julia's type system
- **Multiple Dispatch**: Efficient method dispatch

### Parallel Processing
- **Multi-threading**: Built-in parallel capabilities
- **Distributed Computing**: Multi-machine support
- **GPU Acceleration**: CUDA integration available

## Visualization and Analysis

### Advanced Plotting
- **Time Series**: Belief evolution over time
- **Phase Space**: Dynamic system analysis
- **Probability Distributions**: Uncertainty visualization
- **Information Theory**: Entropy and mutual information plots

### LaTeX Integration
- **Tikz Plots**: High-quality publication graphics
- **Mathematical Notation**: Proper mathematical rendering
- **Animation**: Dynamic visualization of processes

## Output Files

- **simulation_results.json**: Complete simulation data
- **belief_evolution.png**: Time series plots
- **phase_space.png**: Dynamic analysis plots
- **information_metrics.png**: Information theory analysis
- ***.tex**: LaTeX/TikZ graphics files

## Integration Capabilities

### RxInfer Probabilistic Programming
- **Message Passing**: Efficient inference algorithms
- **Model Composition**: Hierarchical model building
- **Automatic Differentiation**: Gradient-based optimization

### Reinforcement Learning
- **Mountain Car**: Continuous control tasks
- **Policy Gradient**: Direct policy optimization
- **Model-Based RL**: World model learning

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Julia Resources
1. **Julia Documentation**: Official language documentation
2. **RxInfer Documentation**: Probabilistic programming framework
3. **Julia for Scientific Computing**: Performance optimization guides
