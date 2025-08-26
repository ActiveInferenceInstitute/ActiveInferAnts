#!/bin/bash

# Active Inference Fortran Implementation Runner

set -e

echo "🔬 Fortran Active Inference Demo"
echo "================================"

# Check if Fortran compiler is installed
if ! command -v gfortran &> /dev/null; then
    echo "❌ Error: GFortran compiler not found"
    echo "Please install GFortran with: sudo apt-get install gfortran"
    exit 1
fi

echo "✅ GFortran found: $(gfortran --version | head -1)"

# Compile the implementation
echo "🔨 Compiling Fortran implementation..."
gfortran -o active_inference active_inference.f90

# Run the simulation
echo "🚀 Running Fortran active inference simulation..."
./active_inference

echo ""
echo "✅ Fortran simulation completed successfully!"
