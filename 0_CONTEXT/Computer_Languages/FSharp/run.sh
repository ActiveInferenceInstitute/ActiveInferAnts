#!/bin/bash

# Active Inference F# Implementation Runner

set -e

echo "🔷 F# Active Inference Demo"
echo "==========================="

# Check if .NET SDK is installed
if ! command -v dotnet &> /dev/null; then
    echo "❌ Error: .NET SDK not found"
    echo "Please install .NET SDK from: https://dotnet.microsoft.com/download"
    exit 1
fi

echo "✅ .NET SDK found: $(dotnet --version)"

# Build the implementation
echo "🔨 Building F# implementation..."
dotnet build

# Run the simulation
echo "🚀 Running F# active inference simulation..."
dotnet run

echo ""
echo "✅ F# simulation completed successfully!"
