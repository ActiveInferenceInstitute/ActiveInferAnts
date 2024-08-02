# Meta-Grants Methodology 📊🔬

This document outlines a comprehensive methodology for generating, analyzing, and reviewing grant proposals using advanced scripts and meta-analysis techniques. The process described herein is designed to facilitate a systematic and rigorous approach to grant writing, evaluation, and analysis.

## Terminology 📚

| Term | Description |
|------|-------------|
| Grant | The fully formatted, submission-ready document. It adheres to specific page requirements, font specifications, and includes necessary attachments such as letters of support and detailed budgets. |
| Pro-Grant | A fully specified and answered Catechism that serves as the basis for generating a complete grant proposal. |
| Pre-Pro-Grant | The input for the grant writing tool, consisting of a set of structured instructions that guide the tool in generating a pro-grant. |

## Methodology Overview 🔎

The meta-grants process employs a suite of sophisticated scripts:

1. PreProGrants_Write.py
2. ProGrant_Write-with-LLM.py
3. ProGrant_Review-with-LLM.py
4. Grants_Summarize-with-LLM.py
5. ProGrant_Meta-Analysis.py
6. PreProGrant_Meta-Analysis.py

## Script Descriptions and Functionalities 🖥️

### Data Preparation 📁

Prior to script execution, ensure the following directories are populated with relevant content:

1. `../Entities/`: Contains subdirectories for each entity, including .py files describing their capabilities and methodological approaches.
2. `../Grants/`: Contains .md files detailing specific grant calls and their requirements.
3. `../Catechisms/`: Contains .md files with comprehensive project description questionnaires.

Additionally, create an `LLM_keys.key` file to store your OpenAI API key. This file is included in .gitignore to ensure it is not shared in open-source repositories.

### 1. PreProGrants_Write.py

This script generates synthetic PRE-PRO-GRANTS by concatenating prompts in the format of "Entity X Grant X Catechism" combinations. Its primary functions include:

- Loading and processing content from the Entities, Grants, and Catechisms folders.
- Combining this content to create structured, concatenated outputs.
- Outputting the generated prompts to the `./Writing_Outputs/PreProGrants/` directory.

### 2. ProGrant_Write-with-LLM.py

This script utilizes a Large Language Model (LLM) to generate PRO-GRANTs based on the pre-pro-grants created by PreProGrants_Write.py. It simulates an entity responding to a grant call using the format specified in the Catechism. Key functions include:

- Reading and processing pre-pro-grant files from the `./Writing_Outputs/PreProGrants/` directory.
- Sending structured prompts to the OpenAI API for processing.
- Saving the generated pro-grants in the `./Writing_Outputs/Written_ProGrants/` directory.

### 3. ProGrant_Review-with-LLM.py

This script employs an LLM to conduct comprehensive reviews of the generated pro-grants. Its functions include:

- Reading pro-grant files from the `./Writing_Outputs/Written_ProGrants/` directory.
- Submitting each pro-grant to the OpenAI API for detailed review and analysis.
- Saving the generated reviews in the `./Writing_Outputs/ProGrant_Reviews/` directory.

### 4. Grants_Summarize-with-LLM.py

This script leverages an LLM to create concise summaries of grant applications. It performs the following operations:

- Reading grant application files from the `../Grants/` directory.
- Submitting each application to the OpenAI API for summarization.
- Saving the generated summaries in the `./Writing_Outputs/Summarized_Grants/` directory.

### 5. ProGrant_Meta-Analysis.py

This script conducts sophisticated meta-analysis on the generated pro-grants. It includes the following analytical processes:

- TF-IDF (Term Frequency-Inverse Document Frequency) analysis to identify key terms in each pro-grant.
- Document clustering using K-means and Hierarchical clustering algorithms.
- Dimensionality reduction techniques including PCA (Principal Component Analysis), t-SNE (t-Distributed Stochastic Neighbor Embedding), and SVD (Singular Value Decomposition).
- Generation of various data visualizations including word clouds, heatmaps, and cluster plots.

### 6. PreProGrant_Meta-Analysis.py

This script performs meta-analysis on the pre-pro-grants, offering insights into the initial instruction sets. Its functionalities mirror those of ProGrant_Meta-Analysis.py but focus on the pre-pro-grant data.

This comprehensive suite of scripts provides a robust framework for systematic grant proposal generation, analysis, and evaluation, leveraging advanced natural language processing and machine learning techniques.