#!/bin/bash

# Active Inference Kotlin Implementation Runner

set -e

echo "🎯 Kotlin Active Inference Demo"
echo "==============================="

# Check if Java is installed (Kotlin runs on JVM)
if ! command -v java &> /dev/null; then
    echo "❌ Error: Java not found"
    echo "Please install Java with: sudo apt-get install default-jre"
    exit 1
fi

echo "✅ Java found: $(java --version | head -1)"

# Check if Kotlin is installed
if ! command -v kotlin &> /dev/null; then
    if ! command -v kotlinc &> /dev/null; then
        echo "❌ Error: Kotlin not found"
        echo "Please install Kotlin from: https://kotlinlang.org/docs/getting-started.html"
        exit 1
    fi
fi

echo "✅ Kotlin found"

# Build with Gradle if available
if [ -f "build.gradle.kts" ]; then
    echo "🔨 Building with Gradle..."
    ./gradlew build
    echo "🚀 Running Kotlin active inference simulation..."
    ./gradlew run
else
    # Run directly with Kotlin
    echo "🚀 Running Kotlin active inference simulation..."
    kotlin ActiveInference.kt
fi

echo ""
echo "✅ Kotlin simulation completed successfully!"
