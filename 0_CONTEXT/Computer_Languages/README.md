# Active Inference / Free Energy Principle Implementations

This directory contains implementations of the Active Inference / Free Energy Principle across multiple programming languages. Each implementation demonstrates core concepts of active inference including belief updating, policy selection, and free energy minimization.

## Overview

Active Inference is a framework for understanding perception, action, and learning in biological and artificial agents. It formalizes the idea that agents act to minimize surprise or prediction error by maintaining internal models of the world.

### Core Concepts Implemented

- **Generative Models**: Internal models of how observations are generated from hidden states
- **Belief Updating**: Bayesian inference to update beliefs about hidden states
- **Expected Free Energy**: Calculation of expected surprise under different policies
- **Policy Selection**: Choosing actions that minimize expected free energy
- **Perception-Action Loop**: Continuous cycle of sensing, inference, and action

## Language Implementations

| Language | Status | Description | Key Features | Dependencies |
|----------|--------|-------------|--------------|--------------|
| **Brainfuck** | ✅ Complete | Esoteric language implementation with sophisticated cognitive processes | Memory-efficient, minimalistic | None |
| **C** | ✅ Complete | Low-level systems implementation | High performance, teacher-student model | Standard library only |
| **C++** | ✅ Complete | Object-oriented implementation with templates | Generic programming, RAII, high performance | Standard library, Eigen (recommended) |
| **C#** | 🔄 In Progress | .NET implementation with LINQ | Modern syntax, async support | .NET Standard |
| **Golang** | ✅ Complete | Concurrent agent-based simulation | Goroutines, channels, ant colony simulation | Standard library only |
| **Haskell** | ✅ Complete | Functional programming approach | Pure functions, monads, type safety, lazy evaluation | Haskell Platform |
| **Java** | ✅ Complete | Object-oriented ant colony simulation | JVM ecosystem, Bayesian inference | Standard library only |
| **JavaScript** | ✅ Complete | Node.js implementation | Event-driven, npm ecosystem, ant colony simulation | Node.js, mathjs, plotly.js |
| **Jock** | ✅ Complete | Functional language for distributed systems | Category theory, Urbit integration | Urbit runtime |
| **Julia** | ✅ Complete | Scientific computing implementation | High-performance, RxInfer integration | Julia ecosystem |
| **Kotlin** | ✅ Complete | Modern JVM language implementation | Concise syntax, coroutines, type safety | Kotlin/JVM, Gradle |
| **MATLAB/Octave** | ⏳ Planned | Matrix-based implementation | Signal processing, control systems | MATLAB/Octave |
| **Perl** | ✅ Complete | Dynamic language implementation | Text processing, CPAN modules | Standard library |
| **PHP** | ⏳ Planned | Web-oriented implementation | Web integration, Composer | PHP 8.0+ |
| **Python** | ✅ Complete | Scientific implementation with numpy | Rich ecosystem, Student-Teacher POMDP | numpy, scipy, matplotlib |
| **R** | ✅ Complete | Statistical programming implementation | Statistical analysis, visualization, data export | R ecosystem |
| **Ruby** | ⏳ Planned | Dynamic object-oriented implementation | Elegant syntax, gems | Ruby 3.0+ |
| **Rust** | ✅ Complete | Systems programming implementation | Memory safety, performance | ndarray, thiserror |
| **Scala** | ⏳ Planned | Functional JVM language | Type system, functional programming | Scala ecosystem |
| **Shell** | ✅ Complete | Command-line implementation | System integration, pipes | POSIX shell |
| **SQL** | ✅ Complete | Database-driven implementation | Declarative programming, queries | SQLite/PostgreSQL |
| **Swift** | ⏳ Planned | Modern systems programming | Type safety, performance | Swift ecosystem |
| **TypeScript** | ✅ Complete | Typed JavaScript implementation | Static typing, comprehensive error handling | Node.js, TypeScript, mathjs |
| **Ada** | ⏳ Planned | Safety-critical systems implementation | Strong typing, concurrency, reliability | GNAT, Ada standard library |
| **Assembly** | ⏳ Planned | Low-level hardware implementation | Direct hardware control, optimization | NASM/GAS assembler |
| **Clojure** | ⏳ Planned | Functional Lisp implementation | Immutable data, JVM ecosystem | Leiningen, Clojure standard library |
| **Crystal** | ⏳ Planned | Ruby-like compiled implementation | Performance, type safety, macros | Crystal standard library |
| **Elixir** | ⏳ Planned | Distributed functional implementation | Erlang VM, fault-tolerance, OTP | Mix, Erlang ecosystem |
| **Erlang** | ⏳ Planned | Concurrent distributed implementation | Actor model, fault-tolerance | Erlang/OTP standard library |
| **F#** | ⏳ Planned | Functional .NET implementation | Type providers, async workflows | .NET Core, F# ecosystem |
| **Fortran** | ⏳ Planned | Scientific computing implementation | Numerical computing, performance | Fortran standard library |
| **Lua** | ⏳ Planned | Lightweight embeddable implementation | Fast, simple, extensible | Lua standard library |
| **Nim** | ⏳ Planned | Python-like systems implementation | Performance, expressiveness, macros | Nim standard library |
| **OCaml** | ⏳ Planned | Functional systems implementation | Type inference, performance | OCaml standard library |
| **Pascal** | ⏳ Planned | Educational structured implementation | Clear syntax, teaching focused | Free Pascal, Lazarus |
| **Prolog** | ⏳ Planned | Logic programming implementation | Declarative, constraint solving | SWI-Prolog, constraint libraries |
| **Racket** | ⏳ Planned | Lisp dialect educational implementation | Language-oriented programming | Racket standard library |
| **Zig** | ⏳ Planned | Modern systems implementation | Safety, performance, C replacement | Zig standard library |

## Implementation Patterns

### Core Components

Each implementation typically includes:

1. **Agent Structure**: Defines the agent's internal state and parameters
2. **Generative Model**: A, B, C, D matrices or equivalent structures
3. **Inference Engine**: Belief updating and policy selection algorithms
4. **Environment Interface**: Interaction with external world
5. **Visualization/Analysis**: Results display and analysis tools

### Common Approaches

- **Student-Teacher Models**: Learning through interaction (Python, C)
- **Ant Colony Optimization**: Swarm intelligence (Java, Golang)
- **POMDP Frameworks**: Partially observable decision processes
- **Bayesian Networks**: Probabilistic graphical models
- **Category Theory**: Mathematical structure preservation (Jock, Haskell)

## Getting Started

### Prerequisites

Most implementations require only standard libraries. For advanced features:

```bash
# Python
pip install numpy scipy matplotlib

# Julia
using Pkg; Pkg.add("RxInfer")

# Rust
cargo add ndarray thiserror

# JavaScript/TypeScript
npm install @types/node
```

### Running Examples

Each language directory contains:

- Main implementation file(s)
- Configuration files
- Example usage
- Documentation

See individual language directories for specific instructions.

## Architecture Patterns

### Modular Design

```
Language/
├── Core/           # Core active inference algorithms
├── Models/         # Specific model implementations
├── Environments/   # Environment interfaces
├── Utils/          # Helper functions and utilities
├── Examples/       # Usage examples
└── Tests/          # Test suites
```

### Common Interfaces

Most implementations follow similar interfaces:

```python
# Python example
class ActiveInferenceAgent:
    def __init__(self, config):
        # Initialize generative model
        pass

    def update_beliefs(self, observation):
        # Bayesian belief updating
        pass

    def select_action(self):
        # Policy selection via EFE minimization
        pass

    def step(self, observation):
        # Perception-action cycle
        pass
```

## Advanced Features

### Multi-Agent Systems

Several implementations support multiple agents:

- **Golang**: Concurrent goroutines with channels
- **Java**: Thread-safe agent colonies
- **Rust**: Async/await with tokio

### Distributed Computing

- **Jock**: Built for distributed Urbit networks
- **Rust**: Async agents with message passing
- **Golang**: Channel-based communication

### Visualization

- **Python**: matplotlib/seaborn plots
- **Julia**: Plots.jl ecosystem
- **Java**: JavaFX/Swing interfaces

## Performance Characteristics

| Language | Performance | Memory Usage | Concurrency | Ecosystem |
|----------|-------------|--------------|-------------|-----------|
| **C** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Rust** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Julia** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Golang** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Python** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Java** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Ada** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Assembly** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ |
| **Clojure** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Crystal** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Elixir** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Erlang** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **F#** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Fortran** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Lua** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Nim** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **OCaml** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Pascal** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Prolog** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Racket** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Zig** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## Contributing

### Adding New Languages

1. Create language directory: `LanguageName/`
2. Implement core active inference algorithms
3. Add configuration and example files
4. Update this README with status
5. Add tests and documentation

### Implementation Guidelines

- Follow language-specific conventions
- Include comprehensive documentation
- Provide working examples
- Implement core active inference concepts
- Handle errors gracefully

### Testing

Each implementation should include:

- Unit tests for core functions
- Integration tests for agent behavior
- Performance benchmarks
- Documentation examples

## Research Applications

### Neuroscience

- Perception and sensory processing
- Decision-making under uncertainty
- Motor control and action selection
- Learning and memory formation

### Artificial Intelligence

- Autonomous agents and robots
- Reinforcement learning
- Cognitive architectures
- Multi-agent systems

### Complex Systems

- Swarm intelligence
- Collective behavior
- Self-organization
- Adaptive systems

## References

### Key Papers

1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Friston, K. et al. (2017)**: Active inference and learning
3. **Da Costa, L. et al. (2020)**: Active inference on discrete state-spaces
4. **Parr, T. & Friston, K. (2019)**: Generalised free energy and active inference

### Books

- Friston, K. (2019): *A free energy principle for a particular physics*
- Buckley, C. et al. (2017): *The free energy principle*

## License

This collection of implementations is provided under the MIT License. Individual language implementations may have their own licensing terms.

## Acknowledgments

Implementations inspired by:

- Karl Friston's work on Active Inference
- The PyMDP library (Python)
- Various research papers and tutorials
- Open-source active inference community

---

*For questions or contributions, please see individual language directories or create an issue in the main repository.*
