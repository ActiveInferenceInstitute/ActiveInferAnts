#!/bin/bash

# Active Inference Assembly Implementation Runner

set -e

echo "🔧 Assembly Active Inference Demo"
echo "================================="

# Check if NASM is installed
if ! command -v nasm &> /dev/null; then
    echo "❌ Error: NASM assembler not found"
    echo "Please install NASM with: sudo apt-get install nasm"
    exit 1
fi

echo "✅ NASM found: $(nasm --version | head -1)"

# Check if LD is available
if ! command -v ld &> /dev/null; then
    echo "❌ Error: LD linker not found"
    exit 1
fi

# Assemble the implementation
echo "🔨 Assembling active_inference.asm..."
nasm -f elf64 active_inference.asm

# Link the object file
echo "🔗 Linking active_inference.o..."
ld active_inference.o -o active_inference

# Run the simulation
echo "🚀 Running Assembly active inference simulation..."
./active_inference

echo ""
echo "✅ Assembly simulation completed successfully!"
