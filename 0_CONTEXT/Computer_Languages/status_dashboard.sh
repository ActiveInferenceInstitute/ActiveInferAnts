#!/bin/bash

# Active Inference Multi-Language Status Dashboard

set -e

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Dashboard header
show_header() {
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${WHITE}                    🧠 ACTIVE INFERENCE MULTI-LANGUAGE DASHBOARD${BLUE}                ║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Language status check
check_language_status() {
    local lang="$1"
    local lang_dir="$2"
    local status=""
    local details=""

    if [ ! -d "$lang_dir" ]; then
        status="${RED}❌ Missing${NC}"
        details="Directory not found"
    elif [ ! -f "$lang_dir/README.md" ]; then
        status="${YELLOW}⚠️ No Docs${NC}"
        details="Missing README.md"
    elif [ ! -f "$lang_dir/run.sh" ]; then
        status="${YELLOW}⚠️ No Run${NC}"
        details="Missing run.sh"
    elif [ ! -x "$lang_dir/run.sh" ]; then
        status="${YELLOW}⚠️ Not Exec${NC}"
        details="run.sh not executable"
    else
        # Check if main source file exists
        local main_file=""
        case "$lang" in
            "Python") main_file="$lang_dir/Student_Teacher.py" ;;
            "JavaScript") main_file="$lang_dir/active_inference.js" ;;
            "Java") main_file="$lang_dir/AntColony.java" ;;
            "C") main_file="$lang_dir/Active_Inference.c" ;;
            "Cpp") main_file="$lang_dir/src/main.cpp" ;;
            "Rust") main_file="$lang_dir/src/main.rs" ;;
            "Go") main_file="$lang_dir/*.go" ;;
            "Haskell") main_file="$lang_dir/app/Main.hs" ;;
            "TypeScript") main_file="$lang_dir/src/ActiveInferenceAgent.ts" ;;
            *) main_file="$lang_dir/*.$lang_dir" ;;
        esac

        if ls $main_file 1> /dev/null 2>&1; then
            status="${GREEN}✅ Complete${NC}"
            details="Fully implemented"
        else
            status="${YELLOW}⚠️ No Code${NC}"
            details="Missing source files"
        fi
    fi

    printf "  %-12s %s - %s\n" "$lang:" "$status" "$details"
}

# Show system information
show_system_info() {
    echo -e "${CYAN}📊 System Information${NC}"
    echo -e "${WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # OS Information
    if command -v lsb_release &> /dev/null; then
        echo -e "  🖥️  OS: $(lsb_release -d | cut -f2)"
    elif [ -f /etc/os-release ]; then
        echo -e "  🖥️  OS: $(grep PRETTY_NAME /etc/os-release | cut -d'=' -f2 | tr -d '"')"
    fi

    # CPU Information
    if command -v nproc &> /dev/null; then
        echo -e "  🧠 CPU Cores: $(nproc)"
    fi

    # Memory Information
    if command -v free &> /dev/null; then
        local mem_info=$(free -h | grep "^Mem:")
        echo -e "  🧠 Memory: $(echo $mem_info | awk '{print $2}') total, $(echo $mem_info | awk '{print $3}') used"
    fi

    # Available languages/compilers
    echo -e "  🛠️  Available Tools:"
    local tools=("python3" "java" "javac" "gcc" "g++" "rustc" "cargo" "go" "node" "npm" "dotnet" "ghc" "erl" "elixir" "lua" "ruby" "php" "perl" "racket" "sbcl" "scala" "kotlin" "swift" "dart" "nim" "crystal" "v" "odin" "zig")
    local available_tools=()

    for tool in "${tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            available_tools+=("$tool")
        fi
    done

    echo -e "     $(echo "${available_tools[*]}" | tr ' ' ', ')"

    echo ""
}

# Show implementation statistics
show_statistics() {
    echo -e "${CYAN}📈 Implementation Statistics${NC}"
    echo -e "${WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    local total_langs=$(find . -maxdepth 1 -type d -not -name "." -not -name ".." | wc -l)
    local readme_count=$(find . -name "README.md" -type f | wc -l)
    local run_count=$(find . -name "run.sh" -type f | wc -l)
    local exec_count=$(find . -name "run.sh" -type f -executable | wc -l)

    echo -e "  📁 Total Language Directories: $total_langs"
    echo -e "  📖 README Files: $readme_count"
    echo -e "  🚀 Run Scripts: $run_count"
    echo -e "  ⚙️ Executable Scripts: $exec_count"

    # Language categories
    local systems_langs=$(echo "Ada Assembly C Cpp Rust Zig Go Nim Crystal" | wc -w)
    local functional_langs=$(echo "Haskell OCaml FSharp Clojure Elixir Erlang Lisp Scheme Racket" | wc -w)
    local scripting_langs=$(echo "Python JavaScript TypeScript Lua Perl Ruby PHP Shell" | wc -w)
    local scientific_langs=$(echo "Julia R Fortran MATLAB Octave" | wc -w)
    local jvm_langs=$(echo "Java Kotlin Scala Groovy" | wc -w)
    local ml_langs=$(echo "Prolog Mercury Curry" | wc -w)

    echo -e "  🏗️ Systems Languages: $systems_langs"
    echo -e "  λ Functional Languages: $functional_langs"
    echo -e "  📜 Scripting Languages: $scripting_langs"
    echo -e "  🔬 Scientific Languages: $scientific_langs"
    echo -e "  ☕ JVM Languages: $jvm_langs"
    echo -e "  🧠 Logic Languages: $ml_langs"

    echo ""
}

# Show language implementations
show_implementations() {
    echo -e "${CYAN}🧠 Language Implementations${NC}"
    echo -e "${WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Define language categories - map display names to actual directory names
    declare -A categories=(
        ["Systems"]="Ada:Ada Assembly:Assembly C:C Cpp:Cpp Rust:Rust Zig:Zig Nim:Nim Crystal:Crystal Odin:Odin V:V"
        ["Functional"]="Haskell:Haskell OCaml:OCaml FSharp:FSharp Clojure:Clojure Elixir:Elixir Erlang:Erlang Racket:Racket"
        ["Scripting"]="Python:Python JavaScript:JavaScript TypeScript:TypeScript Lua:Lua Perl:Perl Shell:Shell"
        ["Scientific"]="Julia:Julia R:R Fortran:Fortran"
        ["JVM"]="Java:Java Kotlin:Kotlin"
        ["Logic"]="Prolog:Prolog SQL:SQL Jock:Jock"
        ["Esoteric"]="Brainfuck:Brainfuck"
        ["Compiled"]="Golang:Golang"
    )

    for category in "${!categories[@]}"; do
        echo -e "${PURPLE}$category Languages:${NC}"
        local langs="${categories[$category]}"

        if [ -z "$langs" ]; then
            echo -e "  ${YELLOW}None implemented${NC}"
        else
            for lang_info in $langs; do
                local lang="${lang_info%:*}"
                local dir="${lang_info#*:}"
                check_language_status "$lang" "$dir"
            done
        fi
        echo ""
    done
}

# Show recent activity
show_recent_activity() {
    echo -e "${CYAN}📅 Recent Activity${NC}"
    echo -e "${WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    echo -e "  📁 Latest Modified Directories:"
    find . -maxdepth 1 -type d -not -name "." -not -name ".." -printf '%T@ %p\n' | sort -n | tail -5 | while read -r timestamp dir; do
        printf "    %s - %s\n" "$(date -d @"${timestamp%.*}" '+%Y-%m-%d %H:%M')" "$(basename "$dir")"
    done

    echo ""
    echo -e "  📝 Latest Modified Files:"
    find . -name "*.md" -o -name "*.sh" -o -name "*.rs" -o -name "*.py" -o -name "*.js" -o -name "*.java" | head -10 | xargs ls -lt | head -5 | while read -r line; do
        echo "    $line" | awk '{print "    " $6 " " $7 " " $8 " " $9}'
    done

    echo ""
}

# Show recommendations
show_recommendations() {
    echo -e "${CYAN}💡 Recommendations${NC}"
    echo -e "${WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Check for missing READMEs
    local missing_readme=$(find . -maxdepth 1 -type d -not -name "." -not -name ".." | while read -r dir; do
        if [ ! -f "$dir/README.md" ]; then
            basename "$dir"
        fi
    done)

    if [ -n "$missing_readme" ]; then
        echo -e "  📖 Missing README.md in:"
        echo "$missing_readme" | while read -r lang; do
            echo -e "     ${YELLOW}⚠️ $lang${NC}"
        done
    fi

    # Check for non-executable run scripts
    local non_exec=$(find . -name "run.sh" -type f -not -executable)
    if [ -n "$non_exec" ]; then
        echo -e "  🚫 Non-executable run.sh files:"
        echo "$non_exec" | while read -r file; do
            echo -e "     ${YELLOW}⚠️ $file${NC}"
        done
    fi

    # Suggest improvements
    echo -e "  🚀 Suggested Improvements:"
    echo -e "     ${BLUE}• Add more language implementations${NC}"
    echo -e "     ${BLUE}• Create comprehensive testing suite${NC}"
    echo -e "     ${BLUE}• Add performance benchmarking${NC}"
    echo -e "     ${BLUE}• Implement language comparison tools${NC}"
    echo -e "     ${BLUE}• Add continuous integration${NC}"

    echo ""
}

# Main dashboard function
main() {
    show_header
    show_system_info
    show_statistics
    show_implementations
    show_recent_activity
    show_recommendations

    echo -e "${GREEN}🎉 Dashboard Complete!${NC}"
    echo ""
    echo -e "${BLUE}💡 Use './run_all.sh' to run all implementations${NC}"
    echo -e "${BLUE}💡 Use './run_all.sh --list' to see available languages${NC}"
    echo -e "${BLUE}💡 Use './run_all.sh <language>' to run specific implementation${NC}"
}

# Run main dashboard
main "$@"
