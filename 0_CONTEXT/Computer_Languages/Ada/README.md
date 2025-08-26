# Active Inference Implementation in Ada

This directory contains an Ada implementation of the Active Inference framework, emphasizing safety, reliability, and strong typing for safety-critical applications.

## Overview

The Ada implementation provides:
- Strong compile-time guarantees
- Real-time performance characteristics
- Safety-critical reliability features
- Contract-based programming

## Core Components

- **Agent Package**: Main active inference agent implementation
- **Generative_Model**: A, B, C, D matrix representations
- **Inference_Engine**: Bayesian belief updating algorithms
- **Environment**: External world interaction interface

## Building and Running

```bash
# Using GNAT
gnatmake active_inference.adb
./active_inference
```

## Dependencies

- GNAT Ada compiler
- Ada standard library

## Architecture

The implementation follows Ada's package structure with strong encapsulation and type safety. The agent uses tasking for concurrent belief updates and action selection.
