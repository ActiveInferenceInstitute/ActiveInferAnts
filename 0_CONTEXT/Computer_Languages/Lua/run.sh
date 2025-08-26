#!/bin/bash

# Active Inference Lua Implementation Runner

set -e

echo "🌙 Lua Active Inference Demo"
echo "============================"

# Check if Lua is installed
if ! command -v lua &> /dev/null; then
    echo "❌ Error: Lua not found"
    echo "Please install Lua with: sudo apt-get install lua5.3"
    exit 1
fi

echo "✅ Lua found: $(lua -v)"

# Run the simulation
echo "🚀 Running Lua active inference simulation..."
lua active_inference.lua

echo ""
echo "✅ Lua simulation completed successfully!"
