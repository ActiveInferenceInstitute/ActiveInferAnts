#!/bin/bash

# Active Inference Racket Implementation Runner

set -e

echo "🏓 Racket Active Inference Demo"
echo "==============================="

# Check if Racket is installed
if ! command -v racket &> /dev/null; then
    echo "❌ Error: Racket not found"
    echo "Please install Racket from: https://racket-lang.org/download/"
    exit 1
fi

echo "✅ Racket found: $(racket --version)"

# Run the simulation
echo "🚀 Running Racket active inference simulation..."
racket active_inference.rkt

echo ""
echo "✅ Racket simulation completed successfully!"
