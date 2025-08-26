#!/bin/bash

# Active Inference Crystal Implementation Runner

set -e

echo "💎 Crystal Active Inference Demo"
echo "================================"

# Check if Crystal is installed
if ! command -v crystal &> /dev/null; then
    echo "❌ Error: Crystal compiler not found"
    echo "Please install Crystal from: https://crystal-lang.org/install/"
    exit 1
fi

echo "✅ Crystal found: $(crystal --version)"

# Run the simulation
echo "🚀 Running Crystal active inference simulation..."
crystal run active_inference.cr

echo ""
echo "✅ Crystal simulation completed successfully!"
