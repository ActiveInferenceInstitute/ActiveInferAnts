# Active Inference Implementation in Python

This directory contains a comprehensive Python implementation of active inference with teacher-student learning dynamics and scientific computing capabilities.

## Overview

The Python implementation provides:
- Scientific computing with NumPy and SciPy
- Teacher-student POMDP framework
- Rich visualization with matplotlib
- Comprehensive analysis tools

## Core Components

- **Student_Teacher.py**: Main teacher-student implementation
- **teacher_wrapper.py**: Teacher model wrapper
- **output/**: Generated visualizations and results

## Architecture

### Teacher-Student Framework
The implementation features a sophisticated teacher-student learning model:

#### Teacher Model
```python
class TeacherModel:
    def __init__(self, n_states):
        self.knowledge = np.zeros(n_states)
        self.growth_rate = 0.1
        self.max_knowledge = 1.0

    def update_knowledge(self, state):
        # Logistic growth model
        current = self.knowledge[state]
        exp_gr = np.exp(self.growth_rate)
        self.knowledge[state] = (self.max_knowledge * current * exp_gr) / \
                               (self.max_knowledge + current * (exp_gr - 1))

    def suggest_resource(self, student_beliefs):
        # Intelligent resource allocation
        gaps = (self.max_knowledge - self.knowledge) * student_beliefs
        return np.argmax(gaps)
```

#### Student Model
```python
class StudentTeacherPOMDP:
    def __init__(self, n_states, n_observations, n_actions):
        self.n_states = n_states
        self.A = self.initialize_matrix(n_observations, n_states)  # Likelihood
        self.B = self.initialize_matrix(n_states, n_actions)      # Transition
        self.C = self.initialize_vector(n_observations)            # Preferences
        self.D = self.initialize_vector(n_states)                  # Prior

    def update_beliefs(self, observation):
        # Bayesian belief updating
        likelihood = self.A[observation, :]
        posterior = likelihood * self.beliefs
        self.beliefs = posterior / np.sum(posterior)
```

## Dependencies

- Python 3.7+
- NumPy: Matrix operations and numerical computing
- SciPy: Scientific computing and optimization
- Matplotlib: Visualization and plotting
- Seaborn: Statistical visualization
- Pandas: Data manipulation and analysis

## Installing Dependencies

```bash
pip install numpy scipy matplotlib seaborn pandas
```

## Building and Running

```bash
# Run the main implementation
python Student_Teacher.py

# Run with custom parameters
python Student_Teacher.py --states 6 --steps 200

# Run teacher model analysis
python teacher_wrapper.py

# Generate visualizations
python -c "from Student_Teacher import StudentTeacherPOMDP; pomdp = StudentTeacherPOMDP(4, 3, 2); pomdp.plot_matrices()"
```

## Configuration

The implementation supports flexible configuration:

```python
# Simulation parameters
config = {
    'n_states': 4,
    'n_observations': 3,
    'n_actions': 2,
    'learning_rate': 0.1,
    'precision': 1.0,
    'uncertainty_weight': 0.1,
    'max_iterations': 100,
    'convergence_threshold': 1e-6,
    'visualization_enabled': True
}
```

## Core Algorithms

### Belief Update Algorithm
```python
def update_beliefs(self, observation):
    likelihood = self.A[observation, :]
    posterior = likelihood * self.beliefs

    # Normalize to ensure probabilities sum to 1
    if np.sum(posterior) > 0:
        self.beliefs = posterior / np.sum(posterior)
    else:
        # Handle zero posterior case
        self.beliefs = np.ones(self.n_states) / self.n_states
```

### Free Energy Calculation
```python
def calculate_free_energy(self, policy):
    # Expected free energy calculation
    efe = 0
    for action in policy:
        # Calculate expected surprise
        predicted_beliefs = self.predict_beliefs(action)
        expected_surprise = self.calculate_expected_surprise(predicted_beliefs)
        efe += np.sum(self.beliefs * expected_surprise)
    return efe
```

### Teacher-Student Learning
```python
def infer_policy(self, policies):
    best_policy = None
    min_free_energy = float('inf')

    for policy in policies:
        fe = self.calculate_free_energy(policy)
        if fe < min_free_energy:
            min_free_energy = fe
            best_policy = policy

    return best_policy
```

## Visualization and Analysis

### Generated Outputs
The implementation creates comprehensive visualizations:

- **Matrix Visualizations**: A, B, C, D matrices as heatmaps
- **Belief Evolution**: Time series of belief state changes
- **Teacher Knowledge**: Growth curves and knowledge distribution
- **Learning Progress**: Performance metrics over time

### Output Files
- `A_matrix.png`: Likelihood matrix visualization
- `B_matrix.png`: Transition matrix visualization
- `student_beliefs_final.png`: Final belief state
- `teacher_knowledge_final.png`: Final teacher knowledge

## Performance Characteristics

### Computational Efficiency
- **Matrix Operations**: Optimized NumPy vectorized operations
- **Memory Usage**: Efficient data structures with minimal overhead
- **Scalability**: Linear scaling with state space size
- **Parallel Processing**: Optional multiprocessing support

### Scientific Computing
- **Numerical Stability**: Robust floating-point calculations
- **Statistical Analysis**: Built-in hypothesis testing
- **Optimization**: Gradient-based and heuristic optimization
- **Data Analysis**: Comprehensive statistical tools

## Extensions

### Advanced Features
- **Machine Learning Integration**: Scikit-learn compatibility
- **Deep Learning**: PyTorch/TensorFlow integration
- **Reinforcement Learning**: OpenAI Gym compatibility
- **Real-time Processing**: Streaming data analysis

### Integration Options
- **Web Applications**: Flask/Django integration
- **Database Systems**: SQL/NoSQL database integration
- **Cloud Computing**: AWS/Google Cloud deployment
- **Real-time Dashboards**: Interactive visualization

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Python Resources
1. **Python Data Science Handbook**: Scientific computing guide
2. **Numerical Python**: Advanced NumPy techniques
3. **Python for Scientific Computing**: Best practices and optimization
