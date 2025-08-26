#!/bin/bash

# Active Inference V Language Implementation Runner

set -e

echo "⚡ V Language Active Inference Demo"
echo "==================================="

# Check if V compiler is installed
if ! command -v v &> /dev/null; then
    echo "❌ Error: V compiler not found"
    echo "Please install V from: https://github.com/vlang/v"
    echo ""
    echo "Installation options:"
    echo "1. From source:"
    echo "   git clone https://github.com/vlang/v"
    echo "   cd v && make && sudo ./v symlink"
    echo ""
    echo "2. Using package manager:"
    echo "   Ubuntu/Debian: sudo apt install vlang"
    echo "   Arch Linux: yay -S vlang"
    exit 1
fi

echo "✅ V compiler found: $(v --version)"

# Check V version
v_version=$(v --version | head -1)
echo "📋 V Version: $v_version"

# Run the simulation
echo "🚀 Running V active inference simulation..."
v run active_inference.v

echo ""
echo "✅ V simulation completed successfully!"

# Optional: Show build information
if [ "$1" = "--build-info" ]; then
    echo ""
    echo "🔨 Build Information:"
    echo "=================="
    echo "Source file: active_inference.v"
    echo "V compiler: $v_version"
    echo "Build mode: Interpreted (v run)"
    echo ""
    echo "💡 For optimized builds, use:"
    echo "   v -prod active_inference.v  # Optimized release build"
    echo "   v -cc gcc active_inference.v  # Use GCC backend"
    echo "   ./active_inference  # Run compiled binary"
fi
