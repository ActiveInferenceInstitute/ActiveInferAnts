#!/bin/bash

# Active Inference Brainfuck Implementation Runner

set -e

echo "🧠 Brainfuck Active Inference Demo"
echo "==================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 not found"
    echo "Please install Python 3 with: sudo apt-get install python3"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check for required Python packages
python3 -c "import numpy, scipy, matplotlib, seaborn, networkx, fastdtw, sklearn" 2>/dev/null || {
    echo "❌ Error: Missing required Python packages"
    echo "Please install with: pip install numpy scipy matplotlib seaborn networkx fastdtw scikit-learn"
    exit 1
}

echo "✅ All Python dependencies found"

# Create default configuration if it doesn't exist
if [ ! -f config.json ]; then
    echo "📝 Creating default configuration..."
    cat > config.json << 'CONFIG_EOF'
{
    "max_iterations": 100,
    "visualization_enabled": true,
    "output_directory": "./output",
    "logging_level": "INFO",
    "initial_values": {
        "sensory_input": 10,
        "prediction": 10,
        "learning_rate": 3,
        "precision": 5,
        "temporal_integration": 1,
        "exploration_factor": 2,
        "model_complexity": 3,
        "goal_directed_behavior": 4,
        "uncertainty": 2
    }
}
CONFIG_EOF
fi

# Run the main Brainfuck simulation
echo "🚀 Running Brainfuck active inference simulation..."
python3 Brainfuck_ActiveInference.py

# Run advanced analysis if requested
if [ "$1" = "--analysis" ]; then
    echo "📊 Running advanced analysis..."
    python3 analysis.py
    
    echo "🏗️ Running category theory analysis..."
    python3 category_theory.py
fi

echo ""
echo "✅ Brainfuck simulation completed successfully!"
