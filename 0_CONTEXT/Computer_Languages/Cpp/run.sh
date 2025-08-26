#!/bin/bash

# Active Inference C++ Implementation Runner

set -e

echo "🔧 C++ Active Inference Demo"
echo "============================"

# Check if C++ compiler is installed
if ! command -v g++ &> /dev/null; then
    echo "❌ Error: G++ compiler not found"
    echo "Please install G++ with: sudo apt-get install g++"
    exit 1
fi

echo "✅ G++ found: $(g++) --version | head -1)"

# Check if CMake is installed
if ! command -v cmake &> /dev/null; then
    echo "❌ Error: CMake not found"
    echo "Please install CMake with: sudo apt-get install cmake"
    exit 1
fi

echo "✅ CMake found: $(cmake --version | head -1)"

# Create build directory
mkdir -p build
cd build

# Configure with CMake
echo "🔨 Configuring with CMake..."
cmake ..

# Build the implementation
echo "🔨 Building C++ implementation..."
make

if [ $? -eq 0 ]; then
    # Run the simulation
    echo "🚀 Running C++ active inference simulation..."
    ./ActiveInferenceDemo

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ C++ simulation completed successfully!"

        # Show performance info if requested
        if [ "$1" = "--bench" ]; then
            echo "📊 Performance metrics:"
            echo "   - Built with optimization flags"
            echo "   - Uses Eigen library for matrix operations"
            echo "   - Multi-threaded ant colony simulation"
        fi
    else
        echo "❌ C++ execution failed."
        exit 1
    fi
else
    echo "❌ C++ build failed."
    exit 1
fi

cd ..

