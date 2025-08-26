#!/bin/bash

# Active Inference Jock Implementation Runner

set -e

echo "🚀 Jock Active Inference Demo"
echo "============================"

# Check if Urbit is installed
if ! command -v urbit &> /dev/null; then
    echo "❌ Error: Urbit not found"
    echo "Please install Urbit from: https://urbit.org/getting-started/"
    exit 1
fi

echo "✅ Urbit found"

# Check if Jock is available
if ! command -v jock &> /dev/null; then
    echo "⚠️ Warning: Jock not found in PATH"
    echo "Please ensure Jock is properly installed"
fi

# Start Urbit ship (this would need to be configured properly)
echo "🛸 Starting Urbit ship..."
echo "Note: This would start an Urbit ship and load the Jock implementation"
echo "For a full demo, you would need to:"
echo "1. Start a Urbit ship: urbit -d my-ship"
echo "2. Load the Jock implementation: |load %active-jockference"
echo "3. Run the simulation: |run-active-inference"

echo ""
echo "📚 Jock Implementation Documentation:"
echo "===================================="
echo "The Jock implementation includes:"
echo "- Active_Jockference.md: Main implementation"
echo "- Jock_Documentation.md: Technical specification"
echo "- Urbit_Active_Jockference.md: Urbit integration"
echo ""
echo "This implementation demonstrates:"
echo "- Category theory foundations"
echo "- Formal mathematical structures"
echo "- Distributed processing capabilities"
echo "- Type-safe active inference"

echo ""
echo "✅ Jock documentation available!"
