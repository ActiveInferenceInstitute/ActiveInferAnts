#!/bin/bash

# Active Inference TypeScript Implementation Runner

set -e

echo "🔷 TypeScript Active Inference Demo"
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

# Check if TypeScript is installed
if ! command -v tsc &> /dev/null; then
    echo "📦 Installing TypeScript..."
    npm install -g typescript
fi

echo "✅ TypeScript found: $(tsc --version)"

# Install dependencies
echo "📦 Installing project dependencies..."
npm install

# Build the TypeScript implementation
echo "🔨 Compiling TypeScript implementation..."
npm run build

# Run the simulation
echo "🚀 Running TypeScript active inference simulation..."
npm start

echo ""
echo "✅ TypeScript simulation completed successfully!"
