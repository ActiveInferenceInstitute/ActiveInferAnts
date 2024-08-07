All models and utilities are structured using JSON to leverage the API's capabilities effectively.

### JSON Files

1. **Entity.json**:
    - **Attributes**:
        - Name
        - Type
        - Description
        - Preferences
        - Affordances
        - Capacities
        - Constraints
        - Stances
        - Values
        - More...

2. **Document.json**:
    - **Properties**:
        - Genre
        - Format
        - Type
        - Title
        - Author
        - Date
        - Sections
        - Content
        - Summary
        - Tags
        - Categories
        - Additional metadata

3. **Prompt.json**:
    - **Prompt Types**:
        - Summarize
        - Extract
        - Classify
        - Translate languages
        - Explain as
        - Make ASCII art
        - Others...

### Python Files

1. **Utils.py**:
    - **Functions**:
        - Deterministic data transformations
        - Probabilistic (LLM) data transformations
        - Enhancing data processing capabilities