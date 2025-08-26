# Active Inference Implementation in V

This directory contains a V language implementation of active inference, showcasing modern compiled language features with Go-like syntax and C-like performance.

## Overview

The V implementation provides:
- Fast compilation and execution
- Memory safety without garbage collection
- Simple, readable syntax
- Cross-platform compatibility

## Core Components

- **active_inference.v**: Main active inference implementation
- **agent.v**: Agent structure and behavior
- **simulation.v**: Simulation runner

## Architecture

### V-Specific Features
The implementation leverages V's unique features:

- **Simple Syntax**: Go-like readability with C-like performance
- **Memory Safety**: Compile-time memory management
- **Fast Compilation**: Rapid iterative development
- **Cross-Platform**: Single codebase for multiple platforms

### Agent Structure
```v
struct ActiveInferenceAgent {
    beliefs []f64
    a_matrix [][]f64  // Likelihood P(o|s)
    b_matrix [][][]f64  // Transition P(s'|s,a)
    c_vector []f64    // Preferences P(o)
    d_vector []f64    // Prior beliefs P(s)
    precision f64
    learning_rate f64
}
```

## Dependencies

- V compiler (vlang)
- No external dependencies required

## Installation

```bash
# Install V from source
git clone https://github.com/vlang/v
cd v
make
sudo ./v symlink

# Or use package manager
# Ubuntu/Debian
sudo apt install vlang

# Arch Linux
yay -S vlang
```

## Building and Running

```bash
# Run directly (V compiles and runs)
v run active_inference.v

# Build optimized binary
v -prod active_inference.v

# Build and run
v active_inference.v
./active_inference
```

## Core Algorithms

### Belief Update Algorithm
```v
fn (mut agent ActiveInferenceAgent) update_beliefs(observation int) {
    // Bayesian belief updating
    likelihood := agent.a_matrix[observation]

    // Posterior = prior * likelihood
    for i in 0..agent.beliefs.len {
        agent.beliefs[i] *= likelihood[i]
    }

    // Normalize
    mut total := 0.0
    for belief in agent.beliefs {
        total += belief
    }
    if total > 0.0 {
        for i in 0..agent.beliefs.len {
            agent.beliefs[i] /= total
        }
    }
}
```

### Expected Free Energy Calculation
```v
fn (agent ActiveInferenceAgent) calculate_expected_free_energy(action int) f64 {
    // Simplified EFE calculation
    mut efe := 0.0
    for i, belief in agent.beliefs {
        if belief > 0.0 {
            efe -= belief * math.log(belief)
        }
    }
    return efe
}
```

### Action Selection
```v
fn (agent ActiveInferenceAgent) select_action() int {
    mut min_efe := math.inf(1)
    mut best_action := 0

    for action in 0..agent.b_matrix.len {
        efe := agent.calculate_expected_free_energy(action)
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
- **Fast**: Compiles to machine code quickly
- **Incremental**: Fast recompilation for development
- **Optimized**: Production builds are highly optimized

### Runtime Performance
- **Native Code**: Direct machine code execution
- **Memory Efficient**: Minimal runtime overhead
- **Predictable**: Consistent performance characteristics

### Memory Safety
- **Compile-time Checks**: Prevents common memory errors
- **No GC**: Predictable memory usage
- **Safe by Default**: Memory safety without runtime cost

## Output and Analysis

The implementation generates:
- Real-time belief state tracking
- Action selection statistics
- Performance metrics
- Simulation results

## Extensions

### Advanced Features
- **Concurrency**: Built-in goroutine-like concurrency
- **Cross-compilation**: Single codebase for multiple platforms
- **C Interop**: Seamless integration with C libraries
- **WebAssembly**: Compile to WebAssembly for web deployment

### Integration Options
- **C Libraries**: Direct C library integration
- **System Programming**: Low-level system access
- **Web Development**: V web framework integration
- **Game Development**: Real-time performance for games

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### V Language Resources
1. **V Language Documentation**: Official language guide
2. **V by Example**: Practical code examples
3. **V Language GitHub**: Source code and community
