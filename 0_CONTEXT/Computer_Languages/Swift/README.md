# Active Inference Implementation in Swift

This directory contains a comprehensive implementation of the Active Inference framework using Apple's Swift programming language, featuring modern Swift features, type safety, and performance optimizations.

## Overview

The Swift implementation provides:

- **Modern Swift Features**: Structs, enums, optionals, and protocol-oriented programming
- **Type Safety**: Strong compile-time type checking and memory safety
- **Performance**: Optimized for both macOS and iOS platforms
- **Cross-Platform Support**: Compatible with Apple's ecosystem (macOS, iOS, tvOS, watchOS, visionOS)
- **Swift Package Manager**: Modern dependency management and project structure

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
   - Statistical analysis with Swift collections
   - Performance metrics and history tracking

## Project Structure

```
Swift/
├── Sources/
│   └── ActiveInference/
│       └── ActiveInferenceAgent.swift
├── Tests/
│   └── ActiveInferenceTests/
│       └── ActiveInferenceTests.swift
├── Package.swift
├── run.sh
└── README.md
```

## Usage

### Basic Example

```swift
import ActiveInference

// Create agent with custom configuration
let config = AgentConfig(
    nStates: 4,
    nObservations: 3,
    nActions: 2,
    precision: 1.0,
    learningRate: 0.1
)

let agent = ActiveInferenceAgent(config: config)

// Run simulation
for step in 1...10 {
    let observation = Int.random(in: 0..<config.nObservations)
    let (action, freeEnergy) = agent.step(observation: observation)

    print("Step \(step): Obs=\(observation), Action=\(action), FE=\(freeEnergy)")
    print("Beliefs: \(agent.getBeliefs())")
}

// Display results
agent.printStatistics()
```

### Multi-Agent Simulation

```swift
import ActiveInference

let nAgents = 5
let agents = (0..<nAgents).map { _ in ActiveInferenceAgent() }

// Run multi-agent simulation
for step in 1...20 {
    for (i, agent) in agents.enumerated() {
        let observation = Int.random(in: 0..<3)
        let (action, _) = agent.step(observation: observation)

        let beliefs = agent.getBeliefs()
        let maxBelief = beliefs.max() ?? 0.0

        print("Agent \(i + 1): Obs=\(observation), Action=\(action), Best Belief=\(String(format: "%.3f", maxBelief))")
    }
}
```

## Requirements

- **Swift 5.5+** (for modern features and performance)
- **Xcode 13+** or **Swift command line tools**
- **macOS 12.0+** or **Linux** (with Swift toolchain)

## Installation

### Option 1: Using Xcode (macOS)
```bash
# Install Xcode from App Store or developer.apple.com
xcode-select --install  # Install command line tools
```

### Option 2: Using Swift Toolchain (Cross-platform)
```bash
# Ubuntu/Debian
sudo apt-get install swiftlang

# CentOS/RHEL
sudo yum install swift-lang

# Download from swift.org for other platforms
```

## Running the Demo

### Automatic (Cross-platform)
```bash
./run.sh
```

### Manual with Swift Package Manager
```bash
swift run
```

### Manual compilation
```bash
swiftc -o ActiveInferenceSwift ActiveInferenceAgent.swift
./ActiveInferenceSwift
```

## Algorithm Details

### Belief Updating
```swift
// Bayesian inference: P(s|o) ∝ P(o|s) * P(s)
let likelihood = generativeModel.aMatrix[observation]
let posterior = zip(likelihood, currentBeliefs).map { $0 * $1 }
let sum = posterior.reduce(0, +)
let normalizedBeliefs = sum > 0 ? posterior.map { $0 / sum } : posterior
```

### Action Selection
```swift
// Minimize expected free energy
let efes = (0..<config.nActions).map { action -> (Int, Double) in
    (action, calculateExpectedFreeEnergy(action: action))
}
let (bestAction, _) = efes.min { $0.1 < $1.1 }!
```

### Learning
```swift
// Simple reinforcement learning
guard let maxState = currentBeliefs.enumerated().max(by: { $0.element < $1.element })?.offset else {
    return
}
// Update generative model probabilities
```

## Performance Characteristics

- **Initialization**: O(n_states × n_observations × n_actions)
- **Belief Update**: O(n_states)
- **Action Selection**: O(n_actions × n_states²)
- **Memory Usage**: O(n_states × n_observations × n_actions)

## Advanced Features

### Functional Composition
```swift
// Compose multiple agents for complex simulations
let agents = (1...10).map { _ in ActiveInferenceAgent(config: config) }

// Run parallel simulation
let results = agents.map { agent in
    (1...100).map { _ in
        let obs = Int.random(in: 0..<3)
        agent.step(observation: obs)
    }
}
```

### Custom Generative Models
```swift
struct CustomModel: GenerativeModel {
    let aMatrix: [[Double]]
    let bMatrix: [[[Double]]]
    let cVector: [Double]
    let dVector: [Double]
    let customParameters: [String: Double]

    init(aMatrix: [[Double]], bMatrix: [[[Double]]], cVector: [Double], dVector: [Double], customParameters: [String: Double]) {
        self.aMatrix = aMatrix
        self.bMatrix = bMatrix
        self.cVector = cVector
        self.dVector = dVector
        self.customParameters = customParameters
    }
}
```

### Testing with XCTest
```swift
import XCTest
@testable import ActiveInference

class ActiveInferenceTests: XCTestCase {
    func testBeliefUpdate() {
        let agent = ActiveInferenceAgent()
        let initialBeliefs = agent.getBeliefs()

        agent.updateBeliefs(observation: 0)

        let newBeliefs = agent.getBeliefs()
        XCTAssertEqual(newBeliefs.reduce(0, +), 1.0, accuracy: 0.001)
        XCTAssertNotEqual(initialBeliefs, newBeliefs)
    }
}
```

## Ecosystem Integration

### Swift Package Manager
```swift
// Add to Package.swift dependencies
dependencies: [
    .package(url: "https://github.com/apple/swift-numerics", from: "1.0.0")
]
```

### Xcode Integration
- **Playground Support**: Interactive experimentation
- **iOS Integration**: Use in iOS apps for cognitive modeling
- **macOS Integration**: Desktop applications with GUI
- **Server-Side Swift**: Backend services with Vapor

### Cross-Platform Compatibility
- **Apple Platforms**: macOS, iOS, tvOS, watchOS, visionOS
- **Linux**: Server deployments
- **Windows**: Limited support via Swift toolchain

## Error Handling

The implementation includes comprehensive error handling:

```swift
do {
    let agent = ActiveInferenceAgent()
    let (action, freeEnergy) = try agent.step(observation: -1) // Invalid observation
} catch {
    print("Error: \(error.localizedDescription)")
}
```

## References

- **Active Inference**: Friston, K. (2010). The free-energy principle
- **Swift Language**: https://swift.org/
- **Apple Developer Documentation**: https://developer.apple.com/documentation/swift
- **Bayesian Inference**: Bishop, C. M. (2006). Pattern Recognition and Machine Learning

## License

This implementation is provided under the MIT License. See the main repository for full license details.
