This folder currently contains some experiments and drafts related to translating Python/Julia Active Inference code into Rust (4-4-2024, DAF).

Currently, this Rust folder is in the `0_CONTEXT/system_design/` folder because the code is a collaborative work in progress, at the System Design stage (e.g. a Rust coder or other can suggest radically new architectures or approaches here).

## Primary Goals:

1. To use Language/Code models & documented methods to translate/transform open-source Python and Julia Active Inference code into open-source Rust Active Inference code.
2. To develop a noisy, non-expert draft/sketch of an Active Inference Ant colony multiscale simulation in Rust language, in order to learn/highlight/explore the unique performance and security features of the Rust language. 
3. To provide an initial basis for further open-source development at the intersection of Active Inference, Rust, and Ants.

## Methods

- `Cursor.sh 0.31` was used, with the `GPT-4` model. Other cloud-based and local language/code models were also used; however, in this specific initial work, it was mostly with Cursor/GPT-4. 
- First, I used the `/9_OTHER/clone_github_users.py` script to bring in many open Github repos from a few target usernames. 
- Then in Cursor, I used the "Resync Index" feature (gear on top right -> Features --> Resync Index) to open the affordance of drawing in the semantics of the contextualized context.
- I copied over some of the Python scripts from other folders, changing the file extension to `.rs`, and prepending the word "Rust" to the filename.
- Here are some examples of prompts that I iteratively used and modified several times, in the popup window & also sidechat, sometimes in series and other times in parallel, to initially translate and then subsequently add and improve: 

  - Explain what this code does in the context of the codebase and language. 
  - Translate this completely into Rust. 
  - Write a Rust equivalent of this code, and confirm that it is equivalent. 
  - Develop and improve this meta-configuration file to leverage as many unique and performant/secure aspects of Rust as possible.
  - Confirm that this is an accurate and complete Rust file for the Ant colony multiscale simulation.
  - Verify that this is valid & professional Rust syntax and semantics. 
  - Develop and improve this Rust script to comprehensively cover what is needed for an Active Inference simulation of an ant simulation. 
  - Write the best possible Rust Active Inference ant agent, given this codebase. 
  - Write that script totally given best practices in RxInfer & pymdp. 
  - Develop the most semantically dense possible prompt for GPT-4 in this genre.
  - Develop and expand this to include unique security features of Rust language. 
  - Develop and professionalize that script, to include all relevant/powerful security tools/approaches in Rust.
  - Develop all of this into concise and comprehensive Rust code. 
  - Compare and contrast `@Rust.config.rs` and `@Rust.Security.rs`.
  - Write a Meta-Script given all of the codebase, to help coordinate all the Rust code we have.
  - Develop and flesh out all sections left uncompleted in methods. 
  - Write a comprehensive best-practices Rust file that runs and checks all Ubuntu computational specs, settings, constraints, etc. that makes it better to run locally. 
  - Develop and improve this important Rust code, with an emphasis on RAM security. 
  - Develop and improve this with a nod towards security and federated decentralized capacities in Rust language and Ant colonies. 
