# Meta-Grants README

This document outlines the comprehensive process for generating and analyzing grant proposals using synthetic prompts and meta-analysis techniques. The methodology described herein is designed to facilitate a systematic approach to grant writing and evaluation.

## Overview

The meta-grants process is a sophisticated three-step procedure:
1. Preparation of Input Data
2. Generation of Synthetic Grant Prompts
3. Meta-Analysis of Generated Prompts

## Step 1: Preparation of Input Data

Prior to executing the main scripts, it is imperative to ensure that the following directories are populated with pertinent and well-structured content:

1. `../Entities/`: This directory should contain subdirectories for each entity under consideration. Each subdirectory must include .py files that comprehensively describe the entity's technical capabilities and perspectival approaches.

2. `../Grants/`: This folder should be populated with .md files, each detailing specific grant calls and their associated requirements. These files serve as the foundation for tailoring proposals to various funding opportunities.

3. `../Catechisms/`: This directory should contain .md files comprising comprehensive project description questions. These catechisms guide the structure and content of the generated grant proposals.

## Step 2: Generation of Synthetic Grant Prompts

Execute the `Write_Grant_Synthetic_Prompt.py` script to generate sophisticated synthetic grant proposal prompts. This script performs the following critical functions:

1. Systematically loads and processes content from the Entities, Grants, and Catechisms folders.
2. Utilizes advanced algorithms to combine this content, creating comprehensive and tailored grant proposal prompts.
3. Outputs the generated prompts to the `./Writing_Outputs/Grant_Prompts/` directory for further analysis and refinement.

To initiate the script, use the following command in your terminal:
