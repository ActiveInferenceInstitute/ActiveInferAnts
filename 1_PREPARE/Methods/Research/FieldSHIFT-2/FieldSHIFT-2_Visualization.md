# Visualization

The following ASCII art illustrates the flow of the FieldSHIFT-2 framework:

   Input Domain
        │
        ▼
┌───────────────────┐
│ generate_pro_shift│
│     domains.py    │
└───────────────────┘
        │
        ▼
  Pro-Shifted Domain
        │
        ▼
┌───────────────────┐
│  shift_domains.py │
└───────────────────┘
        │
        ▼
    Shifted Domain
        │
        ▼
┌───────────────────┐
│   dissertation_   │
│outline_generator.py│
└───────────────────┘
        │
        ▼
 Dissertation Outline
        │
        ▼
┌───────────────────┐
│   dissertation_   │
│   generator.py    │
└───────────────────┘
        │
        ▼
 Dissertation Draft
        │
        ▼
┌───────────────────┐
│   dissertation_   │
│    improver.py    │
└───────────────────┘
        │
        ▼
 Improved Dissertation
        │
        ▼
        ┌───────────────────────────────┬───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────────┐           ┌───────────────────┐           ┌───────────────────┐
│   dissertation_   │           │   dissertation_   │           │ grant_relevance_  │
│   translation.py  │           │   explainer.py    │           │ evaluation.py     │
└───────────────────┘           └───────────────────┘           └───────────────────┘
        │                               │                               │
        ▼                               ▼                               ▼
Translated Dissertation         Explained Dissertation         Grant Relevance Results
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────────┐           ┌───────────────────┐           ┌───────────────────┐
│ language_analysis │           │ grant_relevance_  │           │ final_grant_      │
│       .py         │           │ evaluation.py     │           │ evaluation.py     │
└───────────────────┘           └───────────────────┘           └───────────────────┘
        │                               │                               │
        ▼                               ▼                               ▼
  Analysis Results               Grant Relevance Results         Final Grant Evaluation

This visualization demonstrates the sequential flow of data through the various components of the FieldSHIFT-2 framework, from the initial input domain to the final analysis and grant relevance results.
