# Active Inference Implementation in Brainfuck

This directory contains a sophisticated active inference simulation implemented in Brainfuck, demonstrating advanced cognitive processes through minimalist programming.

## Overview

The Brainfuck implementation showcases:
- Esoteric language cognitive modeling
- Memory-efficient belief representation
- Sophisticated perception-action loops
- Advanced visualization and analysis tools

## Architecture

The implementation uses a Python-based Brainfuck interpreter with comprehensive analysis tools:

- **Brainfuck_ActiveInference.py**: Main simulation with memory cell management
- **analysis.py**: Advanced metrics and causal structure analysis
- **category_theory.py**: Category theory integration for mathematical foundations
- **config_schema.py**: Configuration validation and schema management
- **visualization.py**: Comprehensive plotting and visualization tools

## Core Components

### Memory Cell Layout
```
Cells 0-13: Cognitive processes
  0: Sensory input
  1: Prediction
  2: Action
  3: Free energy
  4: Attention
  5: Memory
  6: Anticipation
  7: Learning rate
  8: Precision
  9: Temporal integration
  10: Exploration factor
  11: Model complexity
  12: Goal-directed behavior
  13: Uncertainty
```

### Active Inference Loop
The main simulation loop implements:
1. **Perception**: Sensory input processing with attention modulation
2. **Prediction**: Forward model prediction with learning rate adaptation
3. **Action Selection**: Free energy minimization for optimal action choice
4. **Memory Update**: Experience integration with model complexity consideration
5. **Anticipation**: Future state prediction with goal-directed behavior

## Dependencies

- Python 3.7+
- NumPy
- SciPy
- NetworkX
- Matplotlib
- Seaborn
- Pandas
- FastDTW
- scikit-learn

## Running the Simulation

```bash
# Basic simulation
python Brainfuck_ActiveInference.py

# With visualization
python Brainfuck_ActiveInference.py --config config.json --visualize

# Advanced analysis
python analysis.py
```

## Configuration

The simulation uses a comprehensive configuration schema:

```python
@dataclass
class SimulationConfig:
    max_iterations: int = 1000
    visualization_enabled: bool = True
    output_directory: str = "./output"
    logging_level: str = "INFO"

    # Initial values for memory cells
    initial_values: Dict[str, int] = field(default_factory=lambda: {
        "sensory_input": 10,
        "prediction": 10,
        "learning_rate": 3,
        "precision": 5,
        "temporal_integration": 1,
        "exploration_factor": 2,
        "model_complexity": 3,
        "goal_directed_behavior": 4,
        "uncertainty": 2
    })
```

## Analysis Features

### Metrics
- Prediction accuracy using dynamic time warping
- Free energy reduction rates
- Uncertainty dynamics
- Temporal complexity analysis
- Causal structure identification

### Visualization
- Time series plots with uncertainty bands
- Phase space analysis
- Probability distribution analysis
- Information theory metrics
- Summary statistics dashboards

## Mathematical Foundations

The implementation demonstrates:

### Free Energy Minimization
```
F = E_q[ln q(s) - ln p(o,s)]
```

### Belief Updating
```
q(s|o) ∝ p(o|s) * q(s)
```

### Expected Free Energy
```
G(π) = Σ_s q(s) * [ln q(s) - ln p(o|s,π)]
```

## Advanced Features

### Category Theory Integration
- Polynomial functors for state transformations
- Functor composition for cognitive morphisms
- Categorical representation of generative models

### Performance Analysis
- Granger causality testing
- Mutual information calculation
- Sample entropy computation
- Rolling window statistics

## Output Files

- `simulation_results.json`: Complete simulation data
- `belief_history.csv`: Belief state evolution
- `action_history.csv`: Action selection history
- `simulation_results.png`: Visualization plots

## References

### Key Papers
1. Friston, K. (2010). The free-energy principle: a unified brain theory?
2. Da Costa, L., et al. (2020). Active inference on discrete state-spaces
3. Parr, T., & Friston, K. (2019). Generalised free energy and active inference

### Brainfuck Resources
1. Urban Müller (1993). Brainfuck programming language specification
2. Brainfuck interpreter implementations
3. Esoteric programming language research
