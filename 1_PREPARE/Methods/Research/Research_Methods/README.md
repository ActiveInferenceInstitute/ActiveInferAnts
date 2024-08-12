# Research Methods Version 2

This document outlines the second iteration of research methodologies, building upon the concepts explored in the `./Research_Methods/` directory. The objective is to present these methodologies in a more generalized, comprehensible, and applicable manner.

## Abstracted and Generalized Methods

### Enhanced Handling of Combinatorics and Prompt Schema
We currently handle Entities, Grants, and Catechisms by concatenating them in a single way. To improve, we need to:
- Handle a broader range of elements.
- Select combinations/orderings of elements.
- Sub-sample/filter elements.
- Use different prompt schemas (e.g., Grant_Summary+Entity to assess relevance, Full_Grant_Call to summarize a grant, Entity and review flexibility).
- Maintain interpretability more efficiently than using long file names and continually exporting to detailed text files.

### Improved File and Directory Management
1. Enhance handling of file names and directory paths.

### Enhanced and Flexible LLM Interactions
2. **Current State**: The OpenAI API call method is implemented separately in the Pro-Grant writing and review scripts.
   **Improvement Goal**: Create a single script to process a directory of text files (prompts) and produce a directory with the LLM-processed text files. This will provide clearer and more flexible LLM interactions, improving usability and consistency.
   **Reference**: Use https://github.com/openai/openai-python and https://openai.com/index/introducing-structured-outputs-in-the-api/

### Linguistic Meta-Analysis Across a Directory
3. **Current State**: Distinct scripts exist for the meta-analysis of Pre-Pro-Grants, Pro-Grants, and Pro-Grant reviews.
   **Improvement Goal**: Develop a unified script capable of processing a directory of text files and generating a comprehensive meta-analysis output. This will streamline the process and enhance efficiency.

### Support for Various Document Schemas and Formats
4. **Goal**: Extend existing scripts to handle different types of document schemas and formats, such as single paragraphs, single pages, sub-sections, etc.
   **Rationale**: Supporting various document schemas and formats will increase the flexibility and applicability of the research methodologies, allowing them to be used with a wider range of input data and generating outputs tailored to specific requirements.

## Feature Extensions
- Incorporate flexible linguistic features abstracted from the LLM substrate, such as: Extend_Length, Professionalize, Review, Translate, Summarize, Make_Into_Table, Make_Section/Paper_Outline, Write_From_Outline, etc.
- Include access to and incorporation of external knowledge bases, such as scientific papers or API calls, especially for specific and technical information.
- Support various input/output formats, including visual and auditory.
- Provide comprehensive FAQ, Q&A, methods documentation, and accessibility features.
