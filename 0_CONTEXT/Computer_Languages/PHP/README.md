# Active Inference Implementation in PHP

This directory contains a comprehensive implementation of the Active Inference framework using PHP's object-oriented capabilities and array operations.

## Overview

The PHP implementation provides:

- **Object-oriented design** using PHP 8.0+ features (union types, attributes)
- **Array-based matrix operations** for generative model computations
- **Bayesian inference engine** with belief updating and policy selection
- **Multi-agent simulation** capabilities
- **Statistical analysis** tools for agent behavior

## Files

- `ActiveInferenceAgent.php` - Main agent class with complete active inference algorithm
- `run.sh` - Cross-platform runner script with version checking
- `README.md` - This documentation

## Features

### Core Active Inference Components

1. **Generative Model**:
   - A-matrix: Observation likelihood P(o|s)
   - B-matrix: State transitions P(s'|s,a)
   - C-vector: Observation preferences P(o)
   - D-vector: Prior beliefs P(s)

2. **Inference Engine**:
   - Bayesian belief updating using array operations
   - Expected free energy calculation
   - Action selection via EFE minimization
   - Learning from experience

3. **Analysis Tools**:
   - Belief entropy calculation
   - Statistical analysis
   - History tracking
   - Performance metrics

## Usage

### Basic Example

```php
// Create agent with 3 states, 3 observations, 2 actions
$agent = new ActiveInferenceAgent(3, 3, 2, 1.0, 0.1);

// Run simulation
for ($step = 1; $step <= 10; $step++) {
    $observation = random_int(1, 3);
    $action = $agent->step($observation);

    echo "Step $step: Obs=$observation, Action=$action\n";

    $beliefs = $agent->getBeliefs();
    echo "Beliefs: [" . implode(', ', array_map(fn($b) => number_format($b, 3), $beliefs)) . "]\n";
}

// Display results
$agent->printStatistics();
```

### Multi-Agent Simulation

```php
$nAgents = 5;
$agents = [];

// Create multiple agents
for ($i = 0; $i < $nAgents; $i++) {
    $agents[] = new ActiveInferenceAgent(3, 3, 2);
}

// Run multi-agent simulation
for ($step = 1; $step <= 20; $step++) {
    foreach ($agents as $i => $agent) {
        $observation = random_int(1, 3);
        $action = $agent->step($observation);

        $beliefs = $agent->getBeliefs();
        $maxBelief = max($beliefs);

        echo "Agent " . ($i + 1) . ": Obs=$observation, Action=$action, Best Belief=" .
             number_format($maxBelief, 3) . "\n";
    }
}
```

## Requirements

- **PHP 8.0 or later** (for union types and modern features)
- **No external dependencies** - uses only PHP standard library

## Installation

```bash
# Ubuntu/Debian
sudo apt-get install php-cli

# CentOS/RHEL
sudo yum install php-cli

# macOS
brew install php

# Windows
# Download from https://windows.php.net/
```

## Running the Demo

### Automatic (Cross-platform)
```bash
./run.sh
```

### Manual
```bash
php ActiveInferenceAgent.php
```

## Algorithm Details

### Belief Updating
```php
// Bayesian inference: P(s|o) ∝ P(o|s) * P(s)
$likelihood = $this->aMatrix[$observation];
$posterior = array_map(fn($l, $b) => $l * $b, $likelihood, $this->beliefs);
$sum = array_sum($posterior);
$this->beliefs = array_map(fn($p) => $p / $sum, $posterior);
```

### Action Selection
```php
// Minimize expected free energy
$minEfe = PHP_FLOAT_MAX;
$bestAction = 0;

foreach (range(0, $this->nActions - 1) as $action) {
    $predictedBeliefs = $this->predictBeliefs($action);
    $efe = $this->calculateExpectedFreeEnergy($predictedBeliefs);

    if ($efe < $minEfe) {
        $minEfe = $efe;
        $bestAction = $action;
    }
}
```

### Learning
```php
// Simple reinforcement learning
$maxState = array_keys($this->beliefs, max($this->beliefs))[0];
$this->aMatrix[$observation][$maxState] += $this->learningRate;

$rowSum = array_sum($this->aMatrix[$observation]);
for ($s = 0; $s < $this->nStates; $s++) {
    $this->aMatrix[$observation][$s] /= $rowSum;
}
```

## Performance Characteristics

- **Initialization**: O(n_states × n_observations × n_actions)
- **Belief Update**: O(n_states)
- **Action Selection**: O(n_actions × n_states²)
- **Memory Usage**: O(n_states × n_observations × n_actions)

## Web Integration

The implementation can be easily integrated into web applications:

```php
// Example web API endpoint
header('Content-Type: application/json');

$agent = new ActiveInferenceAgent(3, 3, 2);
$observation = (int)($_POST['observation'] ?? 1);
$action = $agent->step($observation);

echo json_encode([
    'action' => $action,
    'beliefs' => $agent->getBeliefs(),
    'statistics' => $agent->getStatistics()
]);
```

## Extension Points

### Custom Generative Models
```php
class CustomAgent extends ActiveInferenceAgent {
    private function initializeGenerativeModel(): void {
        // Custom generative model initialization
        $this->aMatrix = $this->customLikelihoodMatrix();
        $this->bMatrix = $this->customTransitionMatrix();
        // ... etc
    }

    private function customLikelihoodMatrix(): array {
        // Implement custom observation model
        return [...];
    }
}
```

### Database Integration
```php
class PersistentAgent extends ActiveInferenceAgent {
    private PDO $db;

    public function __construct(PDO $db, int $nStates, int $nObservations, int $nActions) {
        parent::__construct($nStates, $nObservations, $nActions);
        $this->db = $db;
        $this->loadFromDatabase();
    }

    public function saveToDatabase(): void {
        // Save agent state to database
        $stmt = $this->db->prepare("INSERT INTO agent_history (...) VALUES (...)");
        $stmt->execute([...]);
    }
}
```

## References

- **Active Inference**: Friston, K. (2010). The free-energy principle
- **Bayesian Inference**: Bishop, C. M. (2006). Pattern Recognition and Machine Learning
- **PHP Documentation**: https://www.php.net/docs.php

## License

This implementation is provided under the MIT License. See the main repository for full license details.
