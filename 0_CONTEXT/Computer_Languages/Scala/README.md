# Active Inference Implementation in Scala

This directory contains a comprehensive implementation of the Active Inference framework using Scala's functional programming capabilities, immutable data structures, and strong type system.

## Overview

The Scala implementation provides:

- **Functional Programming**: Pure functions, immutable data structures, and composability
- **Type Safety**: Strong static typing with case classes and pattern matching
- **Immutable Generative Models**: Thread-safe and predictable state management
- **Comprehensive Testing**: Built-in test framework with ScalaTest integration
- **Performance**: JIT-compiled performance with JVM optimizations

## Features

### Core Active Inference Components

1. **Generative Model**:
   - A-matrix: Observation likelihood P(o|s)
   - B-matrix: State transitions P(s'|s,a)
   - C-vector: Observation preferences P(o)
   - D-vector: Prior beliefs P(s)

2. **Inference Engine**:
   - Bayesian belief updating with functional operations
   - Expected free energy calculation
   - Action selection via EFE minimization
   - Learning from experience

3. **Analysis Tools**:
   - Belief entropy calculation
   - Statistical analysis with immutable collections
   - Performance metrics and history tracking

## Project Structure

```
Scala/
├── src/main/scala/
│   └── activeinference/
│       └── ActiveInferenceAgent.scala
├── build.sbt
├── run.sh
└── README.md
```

## Usage

### Basic Example

```scala
import activeinference._

// Create agent with custom configuration
val config = AgentConfig(
  nStates = 4,
  nObservations = 3,
  nActions = 2,
  precision = 1.0,
  learningRate = 0.1
)

val agent = new ActiveInferenceAgent(config)

// Run simulation
for (step <- 1 to 10) {
  val observation = scala.util.Random.nextInt(config.nObservations)
  val (action, freeEnergy) = agent.step(observation)

  println(s"Step $step: Obs=$observation, Action=$action, FE=$freeEnergy")
  println(s"Beliefs: ${agent.getBeliefs}")
}

// Display results
agent.printStatistics()
```

### Multi-Agent Simulation

```scala
import activeinference._

val nAgents = 5
val agents = (1 to nAgents).map(_ => new ActiveInferenceAgent(AgentConfig()))

// Run multi-agent simulation
for (step <- 1 to 20) {
  agents.zipWithIndex.foreach { case (agent, i) =>
    val observation = scala.util.Random.nextInt(3)
    val (action, _) = agent.step(observation)

    val beliefs = agent.getBeliefs
    val maxBelief = beliefs.max

    println(f"Agent ${i + 1}: Obs=$observation, Action=$action, Best Belief=$maxBelief%.3f")
  }
}
```

## Requirements

- **Scala 2.13+** (for modern features and performance)
- **SBT 1.x** (recommended for dependency management)
- **JVM 11+** (for runtime execution)

## Installation

### Option 1: Using SBT (Recommended)
```bash
# Ubuntu/Debian
sudo apt-get install openjdk-11-jdk scala

# macOS
brew install openjdk@11 scala sbt

# Or download SBT from: https://www.scala-sbt.org/download.html
```

### Option 2: Using Scala CLI
```bash
# Install Scala CLI
curl -fL https://github.com/VirtusLab/scala-cli/releases/latest/download/scala-cli-x86_64-pc-linux.gz | gzip -d > scala-cli
chmod +x scala-cli
sudo mv scala-cli /usr/local/bin/
```

## Running the Demo

### Automatic (Cross-platform)
```bash
./run.sh
```

### Manual with SBT
```bash
sbt run
```

### Manual with Scala CLI
```bash
scala-cli run .
```

## Algorithm Details

### Belief Updating
```scala
// Bayesian inference: P(s|o) ∝ P(o|s) * P(s)
val likelihood = generativeModel.aMatrix(observation)
val posterior = likelihood.zip(currentBeliefs).map { case (l, b) => l * b }
val sum = posterior.sum
val normalizedBeliefs = if (sum > 0) posterior.map(_ / sum) else posterior
```

### Action Selection
```scala
// Minimize expected free energy
val efes = (0 until config.nActions).map { action =>
  action -> calculateExpectedFreeEnergy(action)
}
val (bestAction, _) = efes.minBy(_._2)
```

### Learning
```scala
// Simple reinforcement learning with immutable updates
val maxState = currentBeliefs.zipWithIndex.maxBy(_._1)._2
val updatedAMatrix = updateObservationLikelihood(maxState, observation)
// Create new GenerativeModel with updated matrix
```

## Performance Characteristics

- **Initialization**: O(n_states × n_observations × n_actions)
- **Belief Update**: O(n_states)
- **Action Selection**: O(n_actions × n_states²)
- **Memory Usage**: O(n_states × n_observations × n_actions)

## Advanced Features

### Functional Composition
```scala
// Compose multiple agents for complex simulations
val agents = List.fill(10)(new ActiveInferenceAgent(config))

// Run parallel simulation
val results = agents.par.map { agent =>
  (1 to 100).foldLeft(agent) { (a, _) =>
    val obs = Random.nextInt(3)
    a.step(obs)._1
    a
  }
}
```

### Custom Generative Models
```scala
case class CustomModel(
  aMatrix: Vector[Vector[Double]],
  bMatrix: Vector[Vector[Vector[Double]]],
  customParameters: Map[String, Double]
) extends GenerativeModel(aMatrix, bMatrix, Vector.fill(3)(0.0), Vector.fill(4)(0.25))

val customAgent = new ActiveInferenceAgent(config) {
  override def initializeGenerativeModel(): GenerativeModel = {
    // Custom initialization logic
    CustomModel(...)
  }
}
```

### Testing
```scala
class ActiveInferenceSpec extends FlatSpec with Matchers {
  "ActiveInferenceAgent" should "update beliefs correctly" in {
    val agent = new ActiveInferenceAgent(AgentConfig(nStates = 2))
    val initialBeliefs = agent.getBeliefs

    agent.updateBeliefs(0)

    val newBeliefs = agent.getBeliefs
    newBeliefs.sum should be (1.0 +- 0.001)
    newBeliefs should not equal initialBeliefs
  }
}
```

## Ecosystem Integration

### SBT Dependencies
```scala
libraryDependencies ++= Seq(
  "org.scalatest" %% "scalatest" % "3.2.17" % Test,
  "org.scalanlp" %% "breeze" % "2.1.0" // For matrix operations
)
```

### IDE Support
- **IntelliJ IDEA**: Native Scala support
- **VS Code**: With Metals extension
- **SBT Integration**: Built-in project management

## References

- **Active Inference**: Friston, K. (2010). The free-energy principle
- **Scala Language**: https://www.scala-lang.org/
- **Functional Programming**: "Functional Programming in Scala" by Chiusano and Bjarnason
- **Bayesian Inference**: Bishop, C. M. (2006). Pattern Recognition and Machine Learning

## License

This implementation is provided under the MIT License. See the main repository for full license details.
