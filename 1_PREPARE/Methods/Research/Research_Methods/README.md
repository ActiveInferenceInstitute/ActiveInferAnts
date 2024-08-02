# Meta-Grants README 📊🔬

This document outlines the comprehensive process for generating, analyzing, and reviewing grant proposals using various scripts and meta-analysis techniques. The methodology described herein is designed to facilitate a systematic approach to grant writing, evaluation, and analysis.

## Terminology 📚

| Term | Description |
|------|-------------|
| Grant | The fully formatted, ready-to-be-submitted document. It includes page requirements, font specifications, and attachments such as letters and budgets. |
| Pro-Grant | A fully specified/answered Catechism that is ready to be used to generate a grant. |
| Pre-Pro-Grant | The input for the grant writing tool. It consists of a set of instructions that the tool will follow to generate a pro-grant. |

## Overview 🔎

The meta-grants process involves several sophisticated scripts:

1. PreProGrants_Write.py
2. ProGrant_Write-with-LLM.py
3. ProGrant_Review-with-LLM.py
4. Grants_Summarize-with-LLM.py
5. ProGrant_Meta-Analysis.py

## Script Descriptions 🖥️

### 1. PreProGrants_Write.py

This script generates synthetic grant proposal prompts. Its primary functions include:

- Loading content from the Entities, Grants, and Catechisms folders.
- Combining this content to create comprehensive and tailored grant proposal prompts.
- Outputting the generated prompts to the `./Writing_Outputs/Grant_Prompts/` directory.

### 2. ProGrant_Write-with-LLM.py

This script utilizes a Language Learning Model (LLM) to generate grant proposals based on the prompts created by PreProGrants_Write.py. It performs the following tasks:

- Reading the prompt files from the input directory.
- Sending prompts to the OpenAI API for processing.
- Saving the generated grant proposals in the output directory.

### 3. ProGrant_Review-with-LLM.py

This script employs an LLM to review the generated grant proposals. Its functions include:

- Reading the grant proposal files from the input directory.
- Sending each proposal to the OpenAI API for review.
- Saving the reviews in the output directory.

### 4. Grants_Summarize-with-LLM.py

This script summarizes grant applications using an LLM. It performs the following operations:

- Reading grant application files from the input directory.
- Sending each application to the OpenAI API for summarization.
- Saving the summaries in the output directory.

### 5. ProGrant_Meta-Analysis.py

This script conducts meta-analysis on the generated grant proposals. It includes the following analytical processes:

- TF-IDF analysis to identify top terms in each proposal.
- Document clustering using K-means and Hierarchical clustering.
- Dimensionality reduction using PCA, t-SNE, and SVD.
- Generation of various visualizations including word clouds, heatmaps, and cluster plots.

## Preparation of Input Data 📁

Prior to executing these scripts, ensure that the following directories are populated with relevant content:

1. `../Entities/`: Contains subdirectories for each entity, including .py files describing their capabilities and approaches.
2. `../Grants/`: Contains .md files detailing specific grant calls and requirements.
3. `../Catechisms/`: Contains .md files with comprehensive project description questions.

## Execution Instructions 🚀

To run any of these scripts, use the following command in your terminal:
