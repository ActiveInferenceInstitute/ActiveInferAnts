#!/bin/bash

# Active Inference Pascal Implementation Runner

set -e

echo "📚 Pascal Active Inference Demo"
echo "==============================="

# Check if Free Pascal is installed
if ! command -v fpc &> /dev/null; then
    echo "❌ Error: Free Pascal compiler not found"
    echo "Please install Free Pascal with: sudo apt-get install fpc"
    exit 1
fi

echo "✅ Free Pascal found: $(fpc --version | head -1)"

# Compile the implementation
echo "🔨 Compiling Pascal implementation..."
fpc active_inference.pas

# Run the simulation
echo "🚀 Running Pascal active inference simulation..."
./active_inference

echo ""
echo "✅ Pascal simulation completed successfully!"
