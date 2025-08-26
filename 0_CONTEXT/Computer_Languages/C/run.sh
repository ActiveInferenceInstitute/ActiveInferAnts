#!/bin/bash

# Active Inference C Implementation Runner

set -e

echo "🔧 C Active Inference Demo"
echo "=========================="

# Check if GCC is installed
if ! command -v gcc &> /dev/null; then
    echo "❌ Error: GCC compiler not found"
    echo "Please install GCC with: sudo apt-get install gcc"
    exit 1
fi

echo "✅ GCC found: $(gcc --version | head -1)"

# Compile the implementation
echo "🔨 Compiling C implementation..."
gcc -o active_inference Active_Inference.c teacher_model.c -lm

# Run the simulation
echo "🚀 Running C active inference simulation..."
./active_inference

# Optional: Run with debugging
if [ "$1" = "--debug" ]; then
    echo "🐛 Running with debugging..."
    gcc -g -o active_inference_debug Active_Inference.c teacher_model.c -lm
    gdb -ex "run" -ex "quit" ./active_inference_debug
fi

echo ""
echo "✅ C simulation completed successfully!"
