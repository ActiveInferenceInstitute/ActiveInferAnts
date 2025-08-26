#!/bin/bash

# Active Inference OCaml Implementation Runner

set -e

echo "🐪 OCaml Active Inference Demo"
echo "=============================="

# Check if OCaml is installed
if ! command -v ocaml &> /dev/null; then
    echo "❌ Error: OCaml not found"
    echo "Please install OCaml with: sudo apt-get install ocaml"
    exit 1
fi

echo "✅ OCaml found: $(ocaml --version)"

# Run the simulation
echo "🚀 Running OCaml active inference simulation..."
ocaml active_inference.ml

echo ""
echo "✅ OCaml simulation completed successfully!"
