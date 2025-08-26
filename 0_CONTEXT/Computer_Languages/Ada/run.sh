#!/bin/bash

# Active Inference Ada Implementation Runner

set -e

echo "🧠 Ada Active Inference Demo"
echo "============================"

# Check if GNAT is installed
if ! command -v gnatmake &> /dev/null; then
    echo "❌ Error: GNAT Ada compiler not found"
    echo "Please install GNAT with: sudo apt-get install gnat"
    exit 1
fi

echo "✅ GNAT found: $(gnatmake --version | head -1)"

# Compile the Ada implementation
echo "🔨 Compiling Ada implementation..."
gnatmake active_inference.adb demo.adb

# Run the simulation
echo "🚀 Running Ada active inference simulation..."
./demo

echo ""
echo "✅ Ada simulation completed successfully!"
