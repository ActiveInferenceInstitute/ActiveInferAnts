#!/bin/bash

# Active Inference SQL Implementation Runner

set -e

echo "🗄️ SQL Active Inference Demo"
echo "==========================="

# Check if a database system is available
DB_FOUND=false

# Check for PostgreSQL
if command -v psql &> /dev/null; then
    echo "✅ PostgreSQL found: $(psql --version | head -1)"
    DB_SYSTEM="postgresql"
    DB_FOUND=true
fi

# Check for MySQL
if command -v mysql &> /dev/null; then
    echo "✅ MySQL found: $(mysql --version | head -1)"
    if [ "$DB_FOUND" = false ]; then
        DB_SYSTEM="mysql"
        DB_FOUND=true
    fi
fi

# Check for SQLite
if command -v sqlite3 &> /dev/null; then
    echo "✅ SQLite found: $(sqlite3 --version)"
    if [ "$DB_FOUND" = false ]; then
        DB_SYSTEM="sqlite"
        DB_FOUND=true
    fi
fi

if [ "$DB_FOUND" = false ]; then
    echo "❌ Error: No SQL database system found"
    echo "Please install PostgreSQL, MySQL, or SQLite"
    exit 1
fi

echo "📊 Using $DB_SYSTEM for the simulation"

# Setup database and run simulation
case $DB_SYSTEM in
    postgresql)
        echo "🐘 Setting up PostgreSQL database..."
        sudo -u postgres createdb active_inference 2>/dev/null || echo "Database may already exist"
        psql -d active_inference -f SQL.sql
        echo "🚀 Running PostgreSQL active inference simulation..."
        psql -d active_inference -c "CALL run_simulation();"
        ;;
    mysql)
        echo "🦈 Setting up MySQL database..."
        mysql -e "CREATE DATABASE IF NOT EXISTS active_inference;"
        mysql active_inference < SQL.sql
        echo "🚀 Running MySQL active inference simulation..."
        mysql active_inference -e "CALL run_simulation();"
        ;;
    sqlite)
        echo "📱 Setting up SQLite database..."
        sqlite3 active_inference.db < SQL.sql
        echo "🚀 Running SQLite active inference simulation..."
        sqlite3 active_inference.db "SELECT 'Running SQL Active Inference Simulation...';"
        sqlite3 active_inference.db "CALL run_simulation();" 2>/dev/null || echo "Note: SQLite stored procedures have limited support"
        ;;
esac

echo ""
echo "✅ SQL simulation completed successfully!"
