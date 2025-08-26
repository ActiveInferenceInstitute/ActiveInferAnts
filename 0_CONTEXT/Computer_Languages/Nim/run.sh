#!/bin/bash

# Active Inference Nim Implementation Runner

set -e

echo "👑 Nim Active Inference Demo"
echo "============================"

# Check if Nim is installed
if ! command -v nim &> /dev/null; then
    echo "❌ Error: Nim not found"
    echo "Please install Nim from: https://nim-lang.org/install.html"
    exit 1
fi

echo "✅ Nim found: $(nim --version | head -1)"

# Compile the implementation
echo "🔨 Compiling Nim implementation..."
nim c -r active_inference.nim

echo ""
echo "✅ Nim simulation completed successfully!"
