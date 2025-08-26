#!/bin/bash

# Active Inference JavaScript Implementation Runner

set -e

echo "📜 JavaScript Active Inference Demo"
echo "==================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js not found"
    echo "Please install Node.js from: https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js found: $(node --version)"

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ Error: npm not found"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Run the simulation
echo "🚀 Running JavaScript active inference simulation..."
node active_inference.js

echo ""
echo "🎯 Running ant colony simulation..."
node ant_colony_demo.js

echo ""
echo "✅ JavaScript simulation completed successfully!"
