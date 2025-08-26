# Active Inference in JavaScript

This directory contains a JavaScript implementation of the Active Inference framework, demonstrating core concepts through single agents and multi-agent ant colony simulations.

## Overview

The implementation includes:

- **ActiveInferenceAgent**: Core active inference agent with belief updating and policy selection
- **AntColonyEnvironment**: Multi-agent environment for collective intelligence demonstrations
- **Comprehensive demos**: Examples showing various aspects of active inference

## Features

- 🧠 **Core Active Inference**: Belief updating, expected free energy minimization, policy selection
- 🐜 **Ant Colony Simulation**: Multi-agent system with pheromone communication
- 📊 **Analysis Tools**: Behavior analysis and performance metrics
- 🎯 **Educational Examples**: Clear demonstrations of active inference concepts

## Installation

```bash
# Install dependencies
npm install

# Run the ant colony demo
npm run demo

# Run tests
npm test

# Start interactive session
npm start
```

## Dependencies

- **mathjs**: Mathematical operations and matrix handling
- **plotly.js**: Visualization (for future extensions)

## Core Concepts

### Active Inference Agent

```javascript
const agent = new ActiveInferenceAgent({
    nStates: 3,           // Number of hidden states
    nObservations: 3,     // Number of observation types
    nActions: 3,          // Number of possible actions
    uncertaintyWeight: 0.1 // Epistemic value weighting
});

// Perception-action cycle
const observation = 1;  // Some observation
const action = agent.step(observation);
```

### Key Methods

- `updateBeliefs(observation)`: Bayesian belief updating
- `selectAction()`: Expected free energy minimization
- `calculateVariationalFreeEnergy()`: Free energy computation
- `step(observation)`: Complete perception-action cycle

## Ant Colony Simulation

The ant colony demonstrates collective intelligence through:

- **Pheromone Communication**: Ants lay and follow pheromone trails
- **Foraging Behavior**: Coordinated food collection
- **Emergent Patterns**: Collective decision-making and path optimization

```javascript
const environment = new AntColonyEnvironment({
    nAnts: 5,        // Number of ants
    gridSize: 10,    // Environment size
    foodSources: 3   // Number of food sources
});

// Run simulation
const results = environment.runSimulation(50);
```

## Examples

### Single Agent Demo

```bash
node ant_colony_demo.js
```

Shows a single active inference agent learning through interaction with its environment.

### Multi-Agent Simulation

```javascript
import { AntColonyEnvironment } from './active_inference.js';

const env = new AntColonyEnvironment({ nAnts: 10 });
const results = env.runSimulation(100);

console.log(`Food collected: ${env.getFoodCollected()}`);
console.log(`Total pheromones: ${env.getTotalPheromones()}`);
```

## Mathematical Foundations

### Generative Model

The implementation uses a standard POMDP-like generative model:

- **A Matrix**: Likelihood mapping (observations given states)
- **B Matrix**: State transition probabilities (states given actions)
- **C Vector**: Preferences over observations
- **D Vector**: Prior beliefs about initial states

### Free Energy Minimization

Active inference minimizes variational free energy:

```
F = E_q[ln q(s) - ln p(o,s)]
```

Where:
- `q(s)`: Current beliefs about states
- `p(o,s)`: Likelihood of observations given states

### Expected Free Energy

Actions are selected by minimizing expected free energy:

```
G(π) = E_{q(s'|π)}[ln q(s'|π) - ln p(o'|s')] + γ H[q(s'|π)]
```

## Performance

- **Single Agent**: Fast inference with matrix operations
- **Multi-Agent**: Scales well with reasonable ant numbers
- **Memory**: Efficient matrix storage using mathjs

## Educational Value

This implementation is designed for:

- **Learning Active Inference**: Clear, well-documented code
- **Algorithm Understanding**: Step-by-step implementations
- **Experimentation**: Easy to modify and extend
- **Visualization**: Data collection for analysis

## Future Extensions

- [ ] Web-based visualization dashboard
- [ ] Real-time simulation interface
- [ ] Parameter optimization
- [ ] Advanced learning mechanisms
- [ ] Integration with machine learning frameworks

## References

1. Friston, K. (2010). The free-energy principle: a unified brain theory?
2. Da Costa, L., et al. (2020). Active inference on discrete state-spaces
3. Parr, T., & Friston, K. (2019). Generalised free energy and active inference

## License

MIT License - see package.json for details.
