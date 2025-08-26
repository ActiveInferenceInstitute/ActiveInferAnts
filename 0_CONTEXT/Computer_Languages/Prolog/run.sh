#!/bin/bash

# Active Inference Prolog Implementation Runner

set -e

echo "🎯 Prolog Active Inference Demo"
echo "==============================="

# Check if SWI-Prolog is installed
if ! command -v swipl &> /dev/null; then
    echo "❌ Error: SWI-Prolog not found"
    echo "Please install SWI-Prolog with: sudo apt-get install swi-prolog"
    exit 1
fi

echo "✅ SWI-Prolog found: $(swipl --version)"

# Run the simulation
echo "🚀 Running Prolog active inference simulation..."
swipl -s active_inference.pl -g "demo(0), halt."

echo ""
echo "✅ Prolog simulation completed successfully!"
