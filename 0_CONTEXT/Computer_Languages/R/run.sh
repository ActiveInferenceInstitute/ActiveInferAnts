#!/bin/bash

# Active Inference R Implementation Runner

set -e

echo "📊 R Active Inference Demo"
echo "=========================="

# Check if R is installed
if ! command -v R &> /dev/null; then
    echo "❌ Error: R not found"
    echo "Please install R from: https://cran.r-project.org/"
    exit 1
fi

echo "✅ R found: $(R --version | head -1)"

# Run the simulation
echo "🚀 Running R active inference simulation..."
Rscript active_inference.R

echo ""
echo "✅ R simulation completed successfully!"
