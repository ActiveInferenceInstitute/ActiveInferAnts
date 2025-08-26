#!/bin/bash

# Active Inference Haskell Implementation Runner

set -e

echo "λ Haskell Active Inference Demo"
echo "==============================="

# Check if Haskell Stack is installed
if ! command -v stack &> /dev/null; then
    echo "❌ Error: Haskell Stack not found"
    echo "Please install Stack from: https://docs.haskellstack.org/en/stable/README/"
    exit 1
fi

echo "✅ Stack found: $(stack --version)"

# Build the implementation
echo "🔨 Building Haskell implementation..."
stack build

# Run the simulation
echo "🚀 Running Haskell active inference simulation..."
stack run

echo ""
echo "✅ Haskell simulation completed successfully!"
