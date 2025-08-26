#!/bin/bash

# Active Inference Java Implementation Runner

set -e

echo "☕ Java Active Inference Demo"
echo "============================"

# Check if Java is installed
if ! command -v java &> /dev/null; then
    echo "❌ Error: Java not found"
    echo "Please install Java with: sudo apt-get install default-jre"
    exit 1
fi

if ! command -v javac &> /dev/null; then
    echo "❌ Error: Java compiler not found"
    echo "Please install JDK with: sudo apt-get install default-jdk"
    exit 1
fi

echo "✅ Java found: $(java --version | head -1)"
echo "✅ JavaC found: $(javac --version)"

# Compile the implementation
echo "🔨 Compiling Java implementation..."
javac *.java

# Run the simulation
echo "🚀 Running Java active inference simulation..."
java AntColony

echo ""
echo "✅ Java simulation completed successfully!"
