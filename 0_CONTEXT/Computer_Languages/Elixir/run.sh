#!/bin/bash

# Active Inference Elixir Implementation Runner

set -e

echo "🧪 Elixir Active Inference Demo"
echo "==============================="

# Check if Elixir is installed
if ! command -v elixir &> /dev/null; then
    echo "❌ Error: Elixir not found"
    echo "Please install Elixir from: https://elixir-lang.org/install.html"
    exit 1
fi

echo "✅ Elixir found: $(elixir --version)"

# Check if Mix is available
if ! command -v mix &> /dev/null; then
    echo "❌ Error: Mix not found"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
mix deps.get

# Compile and run the simulation
echo "🚀 Running Elixir active inference simulation..."
mix run demo.exs

echo ""
echo "✅ Elixir simulation completed successfully!"
