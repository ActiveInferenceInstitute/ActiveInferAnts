#!/bin/bash

# Active Inference Go Implementation Runner

set -e

echo "🐹 Go Active Inference Demo"
echo "==========================="

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "❌ Error: Go not found"
    echo "Please install Go from: https://golang.org/dl/"
    exit 1
fi

echo "✅ Go found: $(go version)"

# Build the implementation
echo "🔨 Building Go implementation..."
go build *.go

# Run the simulation
echo "🚀 Running Go active inference simulation..."
./Golang

echo ""
echo "✅ Go simulation completed successfully!"
