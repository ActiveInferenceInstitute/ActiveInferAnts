#!/bin/bash

# Active Inference MATLAB/Octave Demo Runner

set -e

echo "🧠 MATLAB/Octave Active Inference Demo"
echo "====================================="

# Check for MATLAB
if command -v matlab &> /dev/null; then
    echo "✅ MATLAB found: $(matlab -help | head -1)"
    echo "🚀 Running MATLAB implementation..."

    # Create temporary MATLAB script
    cat > /tmp/run_matlab.m << 'EOF'
addpath('.');
demo;
exit;
EOF

    # Run MATLAB in batch mode
    matlab -batch "run('/tmp/run_matlab.m')" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ MATLAB simulation completed successfully!"
    else
        echo "❌ MATLAB execution failed."
        exit 1
    fi

# Check for Octave
elif command -v octave &> /dev/null; then
    echo "✅ Octave found: $(octave --version | head -1)"
    echo "🚀 Running Octave implementation..."

    # Run Octave in batch mode
    octave --no-gui --eval "
    addpath('.');
    demo;
    " 2>/dev/null

    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Octave simulation completed successfully!"
    else
        echo "❌ Octave execution failed."
        exit 1
    fi

else
    echo "❌ Neither MATLAB nor Octave found"
    echo "Please install MATLAB or GNU Octave:"
    echo "  MATLAB: https://www.mathworks.com/products/matlab.html"
    echo "  Octave: sudo apt-get install octave (Ubuntu/Debian)"
    echo "          brew install octave (macOS)"
    exit 1
fi
