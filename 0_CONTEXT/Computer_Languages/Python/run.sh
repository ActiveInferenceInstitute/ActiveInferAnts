#!/bin/bash

# Active Inference Python Implementation Runner

set -e

echo "🐍 Python Active Inference Demo"
echo "==============================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 not found"
    echo "Please install Python 3 with: sudo apt-get install python3"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Install dependencies
echo "📦 Installing Python dependencies..."
pip3 install numpy scipy matplotlib seaborn pandas || {
    echo "⚠️ Warning: Could not install packages globally, trying user install..."
    pip3 install --user numpy scipy matplotlib seaborn pandas
}

# Run the main implementation
echo "🚀 Running Python active inference simulation..."
python3 Student_Teacher.py

# Generate visualizations
echo "📊 Generating visualization plots..."
python3 -c "
from Student_Teacher import StudentTeacherPOMDP
import matplotlib.pyplot as plt

# Create and visualize matrices
pomdp = StudentTeacherPOMDP(4, 3, 2)
pomdp.plot_matrices()
plt.close('all')
print('Visualization plots generated in output/ directory')
"

echo ""
echo "✅ Python simulation completed successfully!"
echo "📁 Check the output/ directory for generated visualizations!"
