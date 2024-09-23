# Active InferAnts

Welcome to the **Active InferAnts** project! This README provides a comprehensive overview of the package, its features, installation instructions, usage examples, contribution guidelines, and detailed insights into the project's structure and key components.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
    - [0_CONTEXT](#0_context)
    - [1_PREPARE](#1_prepare)
    - [2_OPERATE](#2_operate)
    - [3_MEASURE](#3_measure)
    - [4_REPORT](#4_report)
    - [5_FOLLOWUP](#5_followup)
    - [6_API](#6_api)
    - [9_OTHER](#9_other)
6. [Detailed Components](#detailed-components)
    - [Active_BPMNferAnts](#active_bpmnferants)
    - [Coda Modules](#coda-modules)
    - [TheoryTranslator](#theorytranslator)
    - [Utilities](#utilities)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)
10. [Contact](#contact)

## Overview

**Active InferAnts** is a Python package engineered to facilitate Active Inference across various applications, with a specialized focus on ant colony optimization and related optimization challenges. The package integrates advanced algorithms and robust data structures to deliver efficient and precise inference capabilities, merging the principles of active inference with problem-solving strategies inspired by ant colony behavior.

Leveraging modular design and comprehensive documentation, **Active InferAnts** serves as both a research tool and a foundation for developing sophisticated optimization solutions.

## Features

- **Advanced Inference Algorithms**: Implements state-of-the-art active inference methods, including variational message passing and belief propagation.
- **Ant Colony Optimization**: Offers specialized algorithms tailored for complex optimization problems using ant colony metaphors.
- **Modular Design**: Features a highly modular architecture, enabling seamless integration and extension of new algorithms and problem domains.
- **Comprehensive Documentation**: Provides detailed documentation, including API references, tutorials, and examples to assist users in effectively utilizing the package.
- **Performance Optimization**: Optimized for high performance and scalability, supporting parallel processing and GPU acceleration where applicable.
- **Visualization Tools**: Includes built-in tools for visualizing ant colony behavior, optimization processes, and inference results.
- **Customizable Parameters**: Allows flexible parameter settings to adapt algorithms to diverse problem domains and specific use cases.
- **Secure Utilities**: Incorporates utility modules for encryption and hashing to ensure data security.

## Installation

To set up **Active InferAnts** for development:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ActiveInferenceInstitute/ActiveInferAnts.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd ActiveInferAnts
    ```
3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

> **Note**: A PyPI release is planned for future updates, enabling installation via `pip install ActiveInferAnts`.

## Usage

After installation, you can start using **Active InferAnts** in your projects. Here's a basic example:

```python
from active_infer_ants import InferenceModel

# Initialize the inference model
model = InferenceModel(parameters)

# Run the inference
results = model.run()

# Visualize the results
model.visualize(results)
```

For more detailed examples and tutorials, refer to the [Documentation](https://github.com/ActiveInferenceInstitute/ActiveInferAnts/wiki).

## Project Structure (Example)

- `0_CONTEXT`: Contains contextual information and high-level documentation.
    - `Computer_Languages`: Implementations in various programming languages.
- `1_PREPARE`: Scripts and modules for data preparation and preprocessing.
    - `Methods`: Processing methods.
    - `Utils`: Utility functions.
- `9_OTHER`: Miscellaneous files and utilities.
    - `BPMN`: BPMN-related files.
    - `Coda`: Integration modules with Coda applications.

## Detailed Components

### Active_BPMNferAnts

Located in `9_OTHER/BPMN/`, **Active_BPMNferAnts.py** is responsible for interfacing with BPMN models, enabling the application of active inference methods to optimize business processes. The accompanying `.bpmn` files provide the necessary templates for visualizing and simulating these processes.

### Coda Modules

The `9_OTHER/Coda/` directory contains modules that integrate **Active InferAnts** with Coda applications. **Coda_ActiveInferAnts.py** facilitates data exchange and processing, while the markdown files document the API summaries and detailed specifications essential for developers looking to extend or utilize the Coda integrations.

### TheoryTranslator

The `1_PREPARE/Methods/TheoryTranslator/` directory houses **TheoryTranslator.py**, which serves as a pivotal tool in converting theoretical models of active inference into practical algorithms. This module ensures that the mathematical foundations are accurately represented in the codebase, maintaining the integrity of the optimization processes.

### Utilities

Under `1_PREPARE/Utils/`, the `encryption.py` and `hashing.py` scripts provide essential security features. **encryption.py** includes functions for data encryption, ensuring that sensitive information remains protected, while **hashing.py** offers hashing mechanisms for data integrity and secure storage, critical for maintaining the reliability of the inference models.

## Contributing

Contributions to **Active InferAnts** are highly encouraged! To contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Implement your changes** and **commit** them with clear, descriptive messages:
    ```bash
    git commit -m "Add feature X"
    ```
4. **Push** your changes to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```
5. **Submit a pull request** to the main repository.

Please ensure that your code adheres to the project's coding standards and includes appropriate tests and documentation.

## License

**Active InferAnts** is open-source software licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software in accordance with the terms of the license.

## Acknowledgments

We gratefully acknowledge the contributions of researchers and developers in the fields of ant colony optimization and active inference. Their foundational work has been instrumental in the development of this project.

## Contact

For questions, support, or further information, please contact us at [blanket@activeinference.institute](mailto:blanket@activeinference.institute).