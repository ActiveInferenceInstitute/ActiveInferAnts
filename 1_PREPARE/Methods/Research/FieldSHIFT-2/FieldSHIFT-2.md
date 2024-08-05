# FieldSHIFT-2: Advanced Domain Shifting Framework

FieldSHIFT-2 is a sophisticated system for executing domain shifting operations. It provides a high-level interface for users to transform input domains into shifted domains and generate corresponding dissertation outlines.

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [Key Components](#key-components)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

FieldSHIFT-2 takes input domains, generates pro-shifted domains, performs domain shifting, and creates dissertation outlines based on the shifted domains. 
It also includes translation & linguistic analysis capabilities for comprehensive evaluation of the results.

## Directory Structure
```
FieldSHIFT-2/
├── FieldSHIFT-2.py
├── generate_pro_shift_domains.py
├── shift_domains.py
├── dissertation_generator.py
├── utils.py
├── config.py
├── language_analysis.py
├── requirements.txt
├── README.md
└── Inputs_and_Outputs/
    ├── Domain/
    ├── Pro-Shifted_Domain/
    ├── Shifted_Domain/
    ├── Shifted_Domain_Dissertation_Outline/
    └── Analyses/
```
## Key Components

### FieldSHIFT-2.py
- **Input**: Configuration file (specified via --config argument)
- **Output**: Manages and orchestrates the entire domain shifting process, writing results to all designated output folders.
- **Functionality**: Acts as the main entry point for the FieldSHIFT-2 framework, coordinating the execution of various modules and ensuring the workflow progresses smoothly from input to final output.

### generate_pro_shift_domains.py
- **Input**: Domain files from `Inputs_and_Outputs/Domain/`
- **Output**: Pro-shifted domain files in `Inputs_and_Outputs/Pro-Shifted_Domain/`
- **Functionality**: Processes raw domain files to generate pro-shifted domains, which serve as intermediate representations before the final domain shift. This step involves initial transformations and preparations for more advanced domain shifting.

### shift_domains.py
- **Input**: Pro-shifted domain files from `Inputs_and_Outputs/Pro-Shifted_Domain/`
- **Output**: Shifted domain files in `Inputs_and_Outputs/Shifted_Domain/`
- **Functionality**: Executes the core domain shifting operations, transforming pro-shifted domains into their final shifted versions. This module leverages advanced language models to perform sophisticated domain transformations.

### dissertation_outline_generator.py
- **Input**: Shifted domain files from `Inputs_and_Outputs/Shifted_Domain/`
- **Output**: Dissertation outline files in `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Functionality**: Generates structured dissertation outlines based on the shifted domain files, ensuring coherence and logical flow. This module creates a high-level framework for dissertations, organizing content into a clear and logical structure.

### dissertation_generator.py
- **Input**: Dissertation outline files from `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Output**: Complete dissertation drafts in `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Functionality**: Expands dissertation outlines into full drafts, adding detailed content and ensuring academic rigor. This module enhances the outlines with comprehensive sections, including introduction, methodology, results, and discussion.

### dissertation_improver.py
- **Input**: Dissertation drafts from `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Output**: Improved dissertation drafts in `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Functionality**: Enhances the quality of dissertation drafts by refining content, improving clarity, and ensuring adherence to academic standards. This module focuses on polishing the drafts to meet high academic and publication standards.

### dissertation_translation.py
- **Input**: Dissertation drafts from `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Output**: Translated dissertation drafts in `Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline/`
- **Functionality**: Translates dissertation drafts into different languages, maintaining the original meaning and context. This module ensures that the dissertations are accessible to a broader audience by providing accurate translations.

### language_analysis.py
- **Input**: All folders in `Inputs_and_Outputs/`
- **Output**: Analysis results in `Inputs_and_Outputs/Analyses/`
- **Functionality**: Performs comprehensive linguistic analysis on all input and output files, providing insights into language patterns, quality, and consistency. This module evaluates the linguistic aspects of the content, ensuring high-quality and consistent language use across all documents.

### utils.py
- **Functionality**: Provides utility functions for file I/O, logging, and LLM setup. This module contains helper functions to streamline file operations, manage logs, and configure language models, ensuring smooth operation across the entire project. It is used by all other modules to perform common tasks efficiently.

### config.py
- **Input**: Configuration file specified by command-line argument
- **Output**: Configuration dictionary used by other modules
- **Functionality**: Loads and parses the configuration file, providing a configuration dictionary that other modules use to access settings and parameters. This module ensures that all components of the framework are correctly configured and can access necessary parameters.

## Installation

1. Clone the repository

## Usage

Run the scripts. 

## Configuration

Create a Python configuration file specifying:
- Input/output directories
- Domain file paths
- Prompts
- LLM parameters
- Analysis parameters

## Contributing

Contribute on Github.
Contact blanket@activeinference.institute 

## License

...