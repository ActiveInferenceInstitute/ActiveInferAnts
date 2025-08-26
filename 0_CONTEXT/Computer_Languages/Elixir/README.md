# Active Inference Implementation in Elixir

This directory contains an Elixir implementation of the Active Inference framework, leveraging the Erlang VM for concurrency and fault-tolerance.

## Overview

The Elixir implementation provides:
- Concurrent agent processes
- Fault-tolerant belief updates
- Distributed computation capabilities
- OTP patterns and supervision trees

## Core Components

- **lib/agent.ex**: Main active inference agent using GenServer
- **lib/generative_model.ex**: A, B, C, D matrix representations
- **lib/inference.ex**: Bayesian belief updating algorithms
- **lib/environment.ex**: External world interaction interface

## Running

```bash
# Using Mix
mix deps.get
mix run

# Interactive mode
iex -S mix
```

## Dependencies

- Elixir 1.14+
- Erlang/OTP 25+
- Matrix library (optional)

## Architecture

The implementation uses Elixir's actor model with GenServer processes for individual agents. Each agent runs in its own process, enabling concurrent belief updates and action selection. The system uses OTP supervision trees for fault tolerance.
