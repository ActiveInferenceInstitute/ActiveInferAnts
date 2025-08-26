#!/bin/bash

# Active Inference Odin Implementation Runner

set -e

echo "⚔️ Odin Active Inference Demo"
echo "============================"

# Check if Odin compiler is installed
if ! command -v odin &> /dev/null; then
    echo "❌ Error: Odin compiler not found"
    echo "Please install Odin from: https://github.com/odin-lang/Odin"
    echo ""
    echo "Installation options:"
    echo "1. From source:"
    echo "   git clone https://github.com/odin-lang/Odin"
    echo "   cd Odin && ./build.sh"
    echo ""
    echo "2. Download pre-built binaries from releases page"
    exit 1
fi

echo "✅ Odin compiler found: $(odin --version)"

# Run the simulation
echo "🚀 Running Odin active inference simulation..."
odin run active_inference.odin

echo ""
echo "✅ Odin simulation completed successfully!"

# Optional: Show build information
if [ "$1" = "--build-info" ]; then
    echo ""
    echo "🔨 Build Information:"
    echo "=================="
    echo "Source file: active_inference.odin"
    echo "Odin compiler: $(odin --version)"
    echo "Build mode: Interpreted (odin run)"
    echo ""
    echo "💡 For optimized builds, use:"
    echo "   odin build active_inference.odin -o:speed  # Optimized build"
    echo "   ./active_inference  # Run compiled binary"
    echo ""
    echo "📚 Odin Language Features Used:"
    echo "   • Struct-based agent design"
    echo "   • Procedural programming paradigm"
    echo "   • Manual memory management"
    echo "   • Type-safe array operations"
    echo "   • Mathematical functions from core library"
fi
