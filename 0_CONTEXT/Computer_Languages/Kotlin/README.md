# Active Inference Implementation in Kotlin

This directory contains a modern Kotlin implementation of active inference with JVM ecosystem integration and functional programming features.

## Overview

The Kotlin implementation provides:
- Modern JVM language features
- Functional programming with immutability
- Comprehensive type safety
- Coroutine-based concurrency

## Core Components

- **ActiveInference.kt**: Main active inference implementation

## Architecture

### Kotlin-Specific Features
The implementation leverages Kotlin's advanced features:

- **Data Classes**: Immutable state representation
- **Sealed Classes**: Type-safe state hierarchies
- **Coroutines**: Asynchronous belief updates
- **Type Inference**: Clean, concise code

### Agent Structure
```kotlin
data class ActiveInferenceAgent(
    val config: AgentConfig,
    val generativeModel: GenerativeModel,
    val currentBeliefs: Vector,
    val history: AgentHistory
)
```

## Dependencies

- Kotlin 1.8+
- Kotlin Standard Library
- Optional: Kotlinx Coroutines for async processing

## Building and Running

```bash
# Compile with Gradle
./gradlew build

# Run the simulation
./gradlew run

# Run specific class
kotlin -cp build/classes/kotlin/main com.activeinference.ActiveInferenceKt
```

## Configuration

```kotlin
data class AgentConfig(
    val nStates: Int = 3,
    val nObservations: Int = 3,
    val nActions: Int = 3,
    val learningRate: Double = 0.1,
    val uncertaintyWeight: Double = 0.1,
    val precision: Double = 1.0
)
```

## Core Algorithms

### Belief Update with Functional Programming
```kotlin
fun updateBeliefs(
    currentBeliefs: Vector,
    observation: Observation,
    generativeModel: GenerativeModel
): Vector {
    return when (generativeModel) {
        is DiscreteGenerativeModel ->
            bayesianUpdate(currentBeliefs, observation, generativeModel)
        is ContinuousGenerativeModel ->
            kalmanUpdate(currentBeliefs, observation, generativeModel)
    }
}
```

### Coroutine-Based Action Selection
```kotlin
suspend fun selectActionAsync(
    agent: ActiveInferenceAgent
): Action = coroutineScope {
    agent.config.actions
        .map { action -> async { calculateEFE(agent, action) } }
        .awaitAll()
        .minByOrNull { it.expectedFreeEnergy }
        ?.action ?: agent.config.actions.first()
}
```

## Performance Characteristics

### Functional Programming Benefits
- **Immutability**: Thread-safe state management
- **Higher-Order Functions**: Flexible algorithm composition
- **Lazy Evaluation**: Efficient computation
- **Type Safety**: Compile-time error prevention

### JVM Integration
- **Interoperability**: Seamless Java integration
- **Performance**: JIT compilation optimization
- **Memory Management**: Automatic garbage collection
- **Multi-threading**: Built-in concurrency support

## Output and Analysis

The implementation generates:
- Real-time belief state tracking
- Action selection statistics
- Performance metrics
- Type-safe result structures

## Extensions

### Advanced Features
- **Multi-platform**: JVM, JS, Native targets
- **Reactive Programming**: Flow-based processing
- **DSL Creation**: Domain-specific languages
- **Android Integration**: Mobile active inference

### Integration Options
- **Spring Boot**: Web application integration
- **Android SDK**: Mobile application development
- **JavaFX**: Desktop GUI applications
- **Microservices**: Distributed system components

## References

### Key Papers
1. **Friston, K. (2010)**: The free-energy principle: a unified brain theory?
2. **Da Costa, L., et al. (2020)**: Active inference on discrete state-spaces
3. **Parr, T., & Friston, K. (2019)**: Generalised free energy and active inference

### Kotlin Resources
1. **Kotlin Documentation**: Official language guide
2. **Kotlin in Action**: Best practices and patterns
3. **Functional Programming in Kotlin**: Advanced concepts
