#!/bin/bash

# Active Inference Ruby Demo Runner

set -e

echo "🧠 Active Inference Ruby Implementation"
echo "====================================="

# Check for Ruby
if ! command -v ruby &> /dev/null; then
    echo "❌ Ruby not found"
    echo "Please install Ruby:"
    echo "  Ubuntu/Debian: sudo apt-get install ruby-full"
    echo "  CentOS/RHEL: sudo yum install ruby"
    echo "  macOS: brew install ruby"
    echo "  Windows: https://rubyinstaller.org/"
    exit 1
fi

echo "✅ Ruby found: $(ruby --version | head -1)"

# Check Ruby version (Ruby 2.5+ recommended for modern features)
RUBY_VERSION=$(ruby -e "print Gem.ruby_version")
REQUIRED_VERSION="2.5.0"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$RUBY_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
    echo "✅ Ruby version $RUBY_VERSION meets requirements"
else
    echo "⚠️  Ruby version $RUBY_VERSION may not support all features (Ruby 2.5+ recommended)"
fi

echo "🚀 Running Ruby active inference simulation..."

# Run the Ruby implementation
ruby active_inference_agent.rb

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Ruby simulation completed successfully!"
else
    echo "❌ Ruby execution failed."
    exit 1
fi
