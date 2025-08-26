# Active Inference Implementation in Odin

This directory contains an Odin language implementation of active inference, showcasing modern systems programming with clean syntax and powerful features.

## Overview

The Odin implementation provides:
- Clean, readable syntax inspired by Pascal and C
- Memory safety with explicit control
- Powerful compile-time features
- Cross-platform compatibility
- High performance characteristics

## Core Components

- **active_inference.odin**: Main active inference implementation
- **agent.odin**: Agent structure and behavior
- **simulation.odin**: Simulation runner and utilities

## Architecture

### Odin-Specific Features
The implementation leverages Odin's unique features:

- **Explicit Memory Management**: Clear ownership and lifetime semantics
- **Clean Syntax**: Pascal-inspired readability with C-like performance
- **Compile-time Evaluation**: Powerful metaprogramming capabilities
- **Type Safety**: Strong static typing with modern features

### Agent Structure
```odin
Active_Inference_Agent :: struct {
    beliefs: []f64,
    a_matrix: matrix.Matrix(f64),  // Likelihood P(o|s)
    b_matrix: []matrix.Matrix(f64), // Transition P(s'|s,a)
    c_vector: []f64,               // Preferences P(o)
    d_vector: []f64,               // Prior beliefs P(s)
    precision: f64,
    learning_rate: f64,
    n_states: int,
    n_observations: int,
    n_actions: int,
}
```

## Dependencies

- Odin compiler
- No external dependencies required

## Installation

```bash
# Install Odin from source
git clone https://github.com/odin-lang/Odin
cd Odin
./build.sh

# Or download pre-built binaries from releases
```

## Building and Running

```bash
# Run directly with Odin
odin run active_inference.odin

# Build optimized binary
odin build active_inference.odin -o:speed

# Build and run
odin build active_inference.odin
./active_inference
```

## Core Algorithms

### Belief Update Algorithm
```odin
update_beliefs :: proc(agent: ^Active_Inference_Agent, observation: int) {
    likelihood := matrix_get_row(agent.a_matrix, observation)

    // Bayesian update: posterior = prior * likelihood
    for i in 0..<len(agent.beliefs) {
        agent.beliefs[i] *= likelihood[i]
    }

    // Normalize beliefs
    normalize_vector(agent.beliefs)
}
```

### Expected Free Energy Calculation
```odin
calculate_expected_free_energy :: proc(agent: Active_Inference_Agent, action: int) -> f64 {
    // Simplified EFE using entropy
    efe: f64 = 0.0
    for belief in agent.beliefs {
        if belief > 0.0 {
            efe -= belief * math.ln(belief)
        }
    }
    return efe
}
```

### Action Selection
```odin
select_action :: proc(agent: Active_Inference_Agent) -> int {
    min_efe := math.F64_MAX
    best_action := 0

    for action in 0..<agent.n_actions {
        efe := calculate_expected_free_energy(agent, action)
        if efe < min_efe {
            min_efe = efe
            best_action = action
        }
    }

    return best_action
}
```

## Performance Characteristics

### Compilation Speed
- **Fast Compilation**: Quick iterative development cycles
- **Incremental Builds**: Fast recompilation for changes
- **Cross-platform**: Single codebase for multiple targets

### Runtime Performance
- **Native Code**: Direct machine code execution
- **Memory Efficient**: Minimal runtime overhead
- **Predictable**: Consistent performance characteristics

### Memory Safety
- **Explicit Control**: Clear memory ownership and lifetimes
- **Bounds Checking**: Array access safety
- **Type Safety**: Compile-time type checking

## Output and Analysis

The implementation generates:
- Real-time belief state tracking
- Action selection statistics
- Performance metrics
- Memory usage information
- Simulation results

## Extensions

### Advanced Features
- **Procedural Generation**: Compile-time code generation
- **Cross-platform**: Windows, Linux, macOS support
- **C Interop**: Seamless integration with C libraries
- **WebAssembly**: Compile to WebAssembly for web deployment

### Integration Options
- **Game Development**: Real-time performance for games
- **System Programming**: Low-level system access
- **Embedded Systems**: Suitable for resource-constrained environments
- **Graphics Programming**: Integration with graphics APIs

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Odin Language Resources
1. **Odin Language Documentation**: Official language guide
2. **Odin by Example**: Practical code examples
3. **Odin Language GitHub**: Source code and community
