# Active Inference Multi-Language Runner

This directory contains implementations of Active Inference in 41 different programming languages, each with its own `run.sh` script for easy execution.

## Quick Start

### Run All Implementations
```bash
./run_all.sh
```

### Run Specific Language
```bash
./run_all.sh python
./run_all.sh java
./run_all.sh rust
```

### Parallel Execution
```bash
./run_all.sh --parallel
```

### List Available Languages
```bash
./run_all.sh --list
```

## Options

- `--sequential` (default): Run implementations one by one
- `--parallel`: Run implementations concurrently
- `--list`: Show all available language implementations
- `--no-color`: Disable colored terminal output
- `--help`: Show detailed usage information

## Features

### 🚀 Easy Execution
Each language implementation includes a `run.sh` script that:
- Checks for required dependencies
- Installs missing packages when possible
- Compiles code if necessary
- Runs the simulation with appropriate parameters
- Provides clear success/failure feedback

### 📊 Comprehensive Coverage
Implements Active Inference across programming paradigms:
- **Systems Languages**: C, C++, Rust, Zig, Ada, Assembly
- **Functional Languages**: Haskell, OCaml, F#, Clojure, Elixir, Erlang
- **Scripting Languages**: Python, JavaScript, Lua, Perl, Shell
- **Scientific Languages**: Julia, R, Fortran
- **Modern Languages**: Go, Kotlin, Crystal, Nim
- **Logic Languages**: Prolog, SQL
- **Educational Languages**: Pascal, Jock
- **Esoteric Languages**: Brainfuck

### 🔧 Automated Setup
The runner automatically handles:
- Dependency checking and installation
- Compilation for compiled languages
- Environment setup for virtual machines (JVM, Erlang, etc.)
- Error handling and reporting

## Language Implementations

Each subdirectory contains:
- `README.md`: Detailed documentation and setup instructions
- `run.sh`: Automated execution script
- Source code files with active inference implementation

## Usage Examples

### Run All Languages Sequentially
```bash
./run_all.sh --sequential
```

### Run Only Python Implementation
```bash
./run_all.sh python
```

### Run Multiple Languages in Parallel
```bash
./run_all.sh --parallel
```

### Check System Compatibility
```bash
./run_all.sh --list
```

## Requirements

### System Requirements
- POSIX-compliant shell (bash, zsh)
- Standard Unix utilities (grep, awk, sed, etc.)
- Internet connection for dependency installation

### Language-Specific Requirements
Each language implementation checks for and installs its own dependencies:
- **Python**: numpy, scipy, matplotlib
- **JavaScript**: Node.js, npm packages
- **Rust**: Cargo, crates
- **Java**: JDK, Maven/Gradle
- And many more...

## Output

The runner provides:
- ✅ **Success indicators** for completed implementations
- ❌ **Error reporting** for failed implementations
- 📊 **Progress tracking** with implementation counts
- 🎨 **Colored output** for better readability

## Troubleshooting

### Common Issues

1. **Missing Dependencies**: The runner will attempt to install missing packages
2. **Compilation Errors**: Check that the required compiler is installed
3. **Permission Errors**: Ensure run.sh scripts have execute permissions
4. **Network Issues**: Some installations require internet connectivity

### Getting Help

```bash
./run_all.sh --help
```

## Contributing

When adding new language implementations:

1. Create a subdirectory with the language name
2. Add the main source code files
3. Create a comprehensive README.md
4. Implement a run.sh script that can execute the implementation
5. Update the LANGUAGES array in run_all.sh
6. Test the implementation with `./run_all.sh <language>`

## Architecture

### Runner Design
```
run_all.sh
├── Language detection and validation
├── Dependency checking and installation
├── Sequential or parallel execution
├── Progress tracking and reporting
└── Error handling and recovery
```

### Implementation Structure
```
Language_Directory/
├── README.md          # Documentation
├── run.sh            # Execution script
├── source_files      # Implementation
└── resources/        # Additional files
```

This comprehensive multi-language implementation demonstrates that Active Inference principles can be effectively implemented across virtually every major programming paradigm, from low-level systems programming to high-level scientific computing.
