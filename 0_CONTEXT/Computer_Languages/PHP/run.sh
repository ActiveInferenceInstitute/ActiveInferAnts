#!/bin/bash

# Active Inference PHP Demo Runner

set -e

echo "🧠 Active Inference PHP Implementation"
echo "====================================="

# Check for PHP
if ! command -v php &> /dev/null; then
    echo "❌ PHP not found"
    echo "Please install PHP:"
    echo "  Ubuntu/Debian: sudo apt-get install php-cli"
    echo "  CentOS/RHEL: sudo yum install php-cli"
    echo "  macOS: brew install php"
    exit 1
fi

echo "✅ PHP found: $(php --version | head -1)"

# Check PHP version (requires PHP 8.0+ for union types)
PHP_VERSION=$(php -r "echo PHP_VERSION;")
REQUIRED_VERSION="8.0.0"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PHP_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
    echo "✅ PHP version $PHP_VERSION meets requirements"
else
    echo "⚠️  PHP version $PHP_VERSION may not support all features (PHP 8.0+ recommended)"
fi

echo "🚀 Running PHP active inference simulation..."

# Run the PHP implementation
php ActiveInferenceAgent.php

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ PHP simulation completed successfully!"
else
    echo "❌ PHP execution failed."
    exit 1
fi
