#!/bin/bash

# Active Inference Clojure Implementation Runner

set -e

echo "🌟 Clojure Active Inference Demo"
echo "==============================="

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "❌ Error: Java not found"
    echo "Please install Java with: sudo apt-get install default-jre"
    exit 1
fi

echo "✅ Java found: $(java --version | head -1)"

# Check if Leiningen is installed
if ! command -v lein &> /dev/null; then
    echo "❌ Error: Leiningen not found"
    echo "Please install Leiningen from: https://leiningen.org/"
    exit 1
fi

echo "✅ Leiningen found: $(lein version)"

# Install dependencies
echo "📦 Installing dependencies..."
lein deps

# Run the simulation
echo "🚀 Running Clojure active inference simulation..."
lein run

echo ""
echo "✅ Clojure simulation completed successfully!"
