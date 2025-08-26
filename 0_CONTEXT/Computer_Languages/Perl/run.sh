#!/bin/bash

# Active Inference Perl Implementation Runner

set -e

echo "🐪 Perl Active Inference Demo"
echo "============================="

# Check if Perl is installed
if ! command -v perl &> /dev/null; then
    echo "❌ Error: Perl not found"
    echo "Please install Perl with: sudo apt-get install perl"
    exit 1
fi

echo "✅ Perl found: $(perl --version | head -1)"

# Install CPAN dependencies if needed
echo "📦 Checking/installing CPAN dependencies..."
perl -MCPAN -e 'install Math::Matrix Statistics::Distributions JSON Getopt::Long' 2>/dev/null || {
    echo "⚠️ Warning: Could not install CPAN modules automatically"
    echo "Please run: cpan Math::Matrix Statistics::Distributions JSON Getopt::Long"
}

# Run the simulation
echo "🚀 Running Perl active inference simulation..."
perl Perl_Agent.pl

echo ""
echo "✅ Perl simulation completed successfully!"
