#!/bin/bash

# Active Inference Zig Implementation Runner

set -e

echo "⚡ Zig Active Inference Demo"
echo "==========================="

# Check if Zig is installed
if ! command -v zig &> /dev/null; then
    echo "❌ Error: Zig not found"
    echo "Please install Zig from: https://ziglang.org/download/"
    exit 1
fi

echo "✅ Zig found: $(zig version)"

# Build the implementation
echo "🔨 Building Zig implementation..."
zig build-exe active_inference.zig

# Run the simulation
echo "🚀 Running Zig active inference simulation..."
./active_inference

# Run with optimizations
echo "⚡ Running optimized version..."
zig build-exe -O ReleaseFast active_inference.zig
./active_inference

echo ""
echo "✅ Zig simulation completed successfully!"
