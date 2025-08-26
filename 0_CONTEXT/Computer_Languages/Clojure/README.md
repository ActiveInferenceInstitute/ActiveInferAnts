# Active Inference Implementation in Clojure

This directory contains a Clojure implementation of the Active Inference framework, leveraging functional programming principles and the JVM ecosystem.

## Overview

The Clojure implementation provides:
- Immutable data structures
- Functional composition
- JVM interoperability
- Rich ecosystem integration

## Core Components

- **core.clj**: Main active inference agent implementation
- **generative_model.clj**: A, B, C, D matrix representations
- **inference.clj**: Bayesian belief updating algorithms
- **environment.clj**: External world interaction interface

## Running

```bash
# Using Leiningen
lein run

# Or with Clojure CLI
clj -M -m active-inference.core
```

## Dependencies

- Clojure 1.11+
- Leiningen or Clojure CLI
- core.matrix for matrix operations

## Architecture

The implementation uses Clojure's immutable data structures and functional programming patterns. The agent is implemented as a series of pure functions with state managed through atoms when necessary.
