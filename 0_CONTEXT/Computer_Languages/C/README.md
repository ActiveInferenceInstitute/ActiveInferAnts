# Active Inference Implementation in C

This directory contains a high-performance C implementation of active inference with teacher-student learning dynamics.

## Overview

The C implementation provides:
- Maximum performance and memory efficiency
- Teacher-student POMDP framework
- Direct memory management
- Minimal runtime overhead

## Core Components

- **Active_Inference.c**: Core active inference algorithms
- **teacher_model.c**: Teacher model with knowledge growth dynamics

## Architecture

### Teacher-Student Framework

The implementation uses a sophisticated teacher-student model:

#### Teacher Model
- **Knowledge Growth**: Sigmoid learning curve with configurable growth rate
- **Resource Suggestion**: Intelligent resource allocation based on student gaps
- **Memory Management**: Efficient dynamic memory allocation

#### Student Model
- **Belief Updating**: Bayesian inference for state estimation
- **Policy Selection**: Free energy minimization for action selection
- **Learning Dynamics**: Adaptive learning from teacher demonstrations

## Dependencies

- GCC 8.0+ or Clang 7.0+
- Standard C library
- POSIX threads (optional for parallel processing)

## Building and Running

```bash
# Compile the implementation
gcc -o active_inference Active_Inference.c teacher_model.c -lm

# Run the simulation
./active_inference

# With debugging
gcc -g -o active_inference_debug Active_Inference.c teacher_model.c -lm
gdb ./active_inference_debug
```

## Configuration

The simulation parameters can be modified in the source code:

```c
// Simulation parameters
#define NUM_STATES 4
#define NUM_OBSERVATIONS 3
#define NUM_ACTIONS 2

// Teacher parameters
#define INITIAL_KNOWLEDGE 0.0
#define MAX_KNOWLEDGE 1.0
#define GROWTH_RATE 0.1

// Student parameters
#define LEARNING_RATE 0.1
#define UNCERTAINTY_WEIGHT 0.1
```

## Mathematical Foundations

### Teacher Knowledge Update
```
k_t = k_max * k_prev * exp(μ) / (k_max + k_prev * (exp(μ) - 1))
```

### Student Belief Update
```
q(s|o) ∝ p(o|s) * q(s)
```

### Free Energy Calculation
```
F = E_q[ln q(s) - ln p(o,s)] = -E_q[ln p(o|s)] + E_q[ln q(s)]
```

## Memory Management

The implementation includes sophisticated memory management:

- **Dynamic Arrays**: Runtime-sized state and observation arrays
- **Memory Pools**: Efficient allocation for frequent operations
- **Resource Tracking**: Memory usage monitoring and leak prevention

## Performance Characteristics

- **Time Complexity**: O(n²) for matrix operations, O(n) for belief updates
- **Space Complexity**: O(n²) for generative model matrices
- **Memory Usage**: Minimal overhead, efficient data structures
- **Cache Efficiency**: Optimized data layouts for CPU cache performance

## Output and Analysis

The implementation generates:
- Real-time console output of belief states
- Performance metrics and timing information
- Teacher-student interaction logs
- Final knowledge state analysis

## Extensions

### Parallel Processing
The framework can be extended with:
- OpenMP for multi-threaded belief updates
- MPI for distributed teacher-student networks
- GPU acceleration with CUDA/OpenCL

### Advanced Features
- Online learning algorithms
- Meta-learning capabilities
- Multi-agent coordination
- Real-time performance monitoring

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Sajid, N., et al. (2022)**: Active inference in robotics and control systems

### C Programming Resources
1. **Kernighan & Ritchie (1988)**: The C Programming Language
2. **C99/C11 Standards**: ISO/IEC 9899 standards
3. **POSIX Threads Programming**: Multi-threaded C applications
