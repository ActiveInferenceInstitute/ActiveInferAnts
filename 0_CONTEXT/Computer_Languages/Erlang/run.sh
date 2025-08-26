#!/bin/bash

# Active Inference Erlang Implementation Runner

set -e

echo "📡 Erlang Active Inference Demo"
echo "==============================="

# Check if Erlang is installed
if ! command -v erl &> /dev/null; then
    echo "❌ Error: Erlang not found"
    echo "Please install Erlang with: sudo apt-get install erlang"
    exit 1
fi

echo "✅ Erlang found: $(erl -version)"

# Compile the implementation
echo "🔨 Compiling Erlang implementation..."
erlc active_inference.erl

# Run the simulation
echo "🚀 Running Erlang active inference simulation..."
erl -noshell -s active_inference demo -s init stop

echo ""
echo "✅ Erlang simulation completed successfully!"
