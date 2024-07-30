import subprocess
import sys
import os
from typing import Union, List, Dict, Any

def execute_command(command: List[str]) -> None:
    """
    Executes a given command using subprocess and handles errors.
    
    Parameters:
    - command (List[str]): The command to execute as a list of strings.
    """
    try:
        subprocess.run(command, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode()
        print(f"Command execution failed with error: {error_msg}", file=sys.stderr)
        sys.exit(1)

def clone_repo(git_url: str, target_dir: str) -> None:
    """
    Clones a single GitHub repository into the specified target directory.
    
    Parameters:
    - git_url (str): The GitHub repository URL to clone.
    - target_dir (str): The directory to clone the repository into.
    """
    repo_name = git_url.split('/')[-1]  # Extracts repo name from URL
    full_path = os.path.join(target_dir, repo_name)
    clone_command = ["git", "clone", git_url, full_path]
    
    execute_command(clone_command)
    print(f"Successfully cloned {git_url} into {full_path}.")

def clone_repos(repo_urls: Union[List[str], Dict[str, str]], target_dir: str = "repos/") -> None:
    """
    Clones a list or dictionary of GitHub repositories into the specified target directory.
    If no target directory is specified, it clones into the 'repos/' directory.
    
    Parameters:
    - repo_urls (Union[List[str], Dict[str, str]]): A list or dictionary of GitHub repository URLs to clone.
    - target_dir (str, optional): The directory to clone the repositories into.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    if isinstance(repo_urls, dict):
        repo_urls = list(repo_urls.values())
    
    for git_url in repo_urls:
        clone_repo(git_url, target_dir)

# Flags to determine which categories to clone
CLONE_THEBRAIN = False
CLONE_GTD = False
CLONE_GANTT = False
CLONE_NOSTR = False
CLONE_SYNERGETICS = False
CLONE_ANTS = False
CLONE_ACTIVE_INFERENCE = False
CLONE_MULTIAGENT_LLM = False
CLONE_TASK_EXECUTION_AI_AGI = False
CLONE_MULTIAGENT_AI = False
CLONE_GENERAL_LLM_RESOURCES = False
CLONE_SOCIAL_MEDIA_INTEROPERABILITY = False
CLONE_HOLOCHAIN = False
CLONE_EBPF = True
CLONE_KAFKA = False

# Repositories to clone
repos_to_clone = {
    "TheBrain": [
        "https://github.com/TheBrainTech/thebrain-api-quickstart-python",
        "https://github.com/sanderdatema/thebrain2markdown",
        "https://github.com/retorquere/zotero-thebrain-export",
        "https://github.com/simoncos/thebrain2dot",
        "https://github.com/TheBrainTech/thebrain-api-quickstart-blazor",
        "https://github.com/TheBrainTech/thebrain-api-quickstart-node",
        "https://github.com/TheBrainTech/xwt",
        "https://github.com/cdebattista/thebrain-apiclient",
        "https://github.com/MattGyverLee/TheBrain-API-Playground"
    ],
    "GTD": [
        "https://github.com/connermcd/gtd",
        "https://github.com/engineyard/todo",
        "https://github.com/tewen/gtd-scripts"
    ],
    "Gantt": [
        "https://github.com/neuronetio/gantt-schedule-timeline-calendar",
        "https://github.com/frappe/gantt",
        "https://github.com/neuronetio/gantt-elastic"
    ],
    "Nostr": [
        "https://github.com/nostr-protocol/nostr",
        "https://github.com/fiatjaf/nostr-tools",
        "https://github.com/limina1/indextr-client",
        "https://github.com/fiatjaf/quill-asciidoc",
        "https://github.com/fiatjaf/svelte-asciidoc",
        "https://github.com/github-tijlxyz/wikinostr",
        "https://github.com/aljazceru/awesome-nostr",
        "https://github.com/nostr-connect/connect"
    ],
    "Synergetics": [
        "https://github.com/4dsolutions/MartianMath",
        "https://github.com/4dsolutions/m4w",
        "https://github.com/4dsolutions/python_camp",
        "https://github.com/4dsolutions/School_of_Tomorrow",
        "https://github.com/4dsolutions/DigitalMathematics",
        "https://github.com/4dsolutions/Curriculum_Development"
    ],
    "Ants": [
        "https://github.com/Social-Insect-Genomics/",
        "https://github.com/johnssproul/Insect_REs",
        "https://github.com/pbfrandsen/insect_genome_assemblies",
        "https://github.com/PeterMulhair/DToL_insects",
        "https://github.com/fohebert/GenomeAnnotation",
        "https://github.com/guillemylla/Crickets_Genome_Annotation"
    ],
    "ActiveInference": [
        "https://github.com/ActiveInferenceInstitute/ActiveBlockference",
        "https://github.com/infer-actively/pymdp",
        "https://github.com/cadCAD-org/cadcad-ri"
    ],
    "MultiagentLLM": [
        "https://github.com/nickm980/smallville",
        "https://github.com/chatarena/chatarena",
        "https://github.com/OpenGVLab/GITM",
        "https://github.com/OpenBMB/AgentVerse",
        "https://github.com/BladeTransformerLLC/OvercookedGPT",
        "https://github.com/101dotxyz/GPTeam",
        "https://github.com/mkturkcan/generative-agents"
    ],
    "TaskExecutionAIAGI": [
        "https://docs.superagent.sh/concepts#prompts",
        "https://github.com/Significant-Gravitas/Auto-GPT",
        "https://github.com/SamurAIGPT/Camel-AutoGPT",
        "https://github.com/Josh-XT/AGiXT",
        "https://github.com/reworkd/AgentGPT",
        "https://github.com/muellerberndt/mini-agi",
        "https://github.com/enricoros/big-agi",
        "https://github.com/TransformerOptimus/SuperAGI",
        "https://github.com/TransformerOptimus/SuperAGI"
    ],
    "MultiagentAI": [
        "https://github.com/deepmind/open_spiel",
        "https://github.com/NeuralMMO/environment",
        "https://github.com/datamllab/rlcard",
        "https://github.com/Farama-Foundation/MAgent2",
        "https://github.com/salesforce/ai-economist"
    ],
    "GeneralLLMResources": [
        "https://github.com/filipecalegario/awesome-generative-ai",
        "https://github.com/EmbraceAGI/Awesome-AGI",
        "https://github.com/tigerneil/awesome-deep-rl",
        "https://github.com/wel3kxial/AIGC_Resources",
        "https://github.com/imaurer/awesome-decentralized-llm",
        "https://github.com/gabriben/awesome-generative-information-retrieval",
        "https://github.com/hwchase17/langchain",
        "https://github.com/Mooler0410/LLMsPracticalGuide",
        "https://github.com/microsoft/LMOps",
        "https://github.com/ennucore/clippy"
    ],
    "SocialMediaInteroperability": [
        "https://github.com/42wim/matterbridge"
    ],
    "Holochain": [
        "https://github.com/holochain/holochain",
        "https://github.com/holochain-open-dev/holochain-open-dev",
        "https://github.com/lightningrodlabs/acorn",
        "https://github.com/f13end/Holochain-Projects",
        "https://github.com/holochain-apps/holochain-apps",
        "https://github.com/holochain/scaffolding",
        "https://github.com/holochain/holochain-client-rust",
        "https://github.com/holochain/holochain-client-js",
        "https://github.com/holochain/launcher-tauri",
        "https://github.com/holochain/wind-tunnel",
        "https://github.com/Holo-Host/hpos-service-crates",
        "https://github.com/Holo-Host/host-console-ui",
        "https://github.com/Holo-Host/ui-common-library",
        "https://github.com/Holo-Host/holo-auto-installer"
    ],
    "eBPF": [
        "https://github.com/cilium/ebpf",
        "https://github.com/zoidyzoidzoid/awesome-ebpf",
        "https://github.com/eunomia-bpf/bpf-developer-tutorial",
        "https://github.com/microsoft/ebpf-for-windows",
        "https://github.com/lizrice/learning-ebpf",
        "https://github.com/lizrice/ebpf-beginners",
        "https://github.com/xdp-project/bpf-examples",
        "https://github.com/KindlingProject/kindling",
        "https://github.com/iovisor/bcc",
        "https://github.com/cilium/cilium"
    ],
    "Kafka": [
        "https://github.com/apache/kafka",
        "https://github.com/confluentinc/kafka-tutorials",
        "https://github.com/monksy/awesome-kafka",
        "https://github.com/confluentinc/kafka-streams-examples",
        "https://github.com/confluentinc/examples",
        "https://github.com/provectus/kafka-ui",
        "https://github.com/pmoskovi/kafka-learning-resources",
        "https://github.com/streamthoughts/awesome-opensource-contribs-kafka",
        "https://github.com/MocMilo/kafka-project",
        "https://github.com/hifly81/kafka-examples",
        "https://github.com/bstashchuk/apache-kafka-course",
        "https://github.com/hpang123/Kafka"
    ]
}

# Enhanced cloning process with category-based organization
if __name__ == "__main__":
    target_dir = input("Enter the target directory (default is 'repos/'): ").strip() or "repos/"
    
    if CLONE_THEBRAIN:
        print("Cloning TheBrain repositories...")
        clone_repos(repos_to_clone["TheBrain"], os.path.join(target_dir, "TheBrain"))
    
    if CLONE_GTD:
        print("Cloning GTD repositories...")
        clone_repos(repos_to_clone["GTD"], os.path.join(target_dir, "GTD"))
    
    if CLONE_GANTT:
        print("Cloning Gantt repositories...")
        clone_repos(repos_to_clone["Gantt"], os.path.join(target_dir, "Gantt"))
    
    if CLONE_NOSTR:
        print("Cloning Nostr repositories...")
        clone_repos(repos_to_clone["Nostr"], os.path.join(target_dir, "Nostr"))
    
    if CLONE_SYNERGETICS:
        print("Cloning Synergetics repositories...")
        clone_repos(repos_to_clone["Synergetics"], os.path.join(target_dir, "Synergetics"))
    
    if CLONE_ANTS:
        print("Cloning Ants repositories...")
        clone_repos(repos_to_clone["Ants"], os.path.join(target_dir, "Ants"))
    
    if CLONE_ACTIVE_INFERENCE:
        print("Cloning Active Inference repositories...")
        clone_repos(repos_to_clone["ActiveInference"], os.path.join(target_dir, "ActiveInference"))
    
    if CLONE_MULTIAGENT_LLM:
        print("Cloning Multiagent LLM repositories...")
        clone_repos(repos_to_clone["MultiagentLLM"], os.path.join(target_dir, "MultiagentLLM"))
    
    if CLONE_TASK_EXECUTION_AI_AGI:
        print("Cloning Task Execution AI and AGI repositories...")
        clone_repos(repos_to_clone["TaskExecutionAIAGI"], os.path.join(target_dir, "TaskExecutionAIAGI"))
    
    if CLONE_MULTIAGENT_AI:
        print("Cloning Multiagent AI repositories...")
        clone_repos(repos_to_clone["MultiagentAI"], os.path.join(target_dir, "MultiagentAI"))
    
    if CLONE_GENERAL_LLM_RESOURCES:
        print("Cloning General LLM resources repositories...")
        clone_repos(repos_to_clone["GeneralLLMResources"], os.path.join(target_dir, "GeneralLLMResources"))
    
    if CLONE_SOCIAL_MEDIA_INTEROPERABILITY:
        print("Cloning Social Media Interoperability repositories...")
        clone_repos(repos_to_clone["SocialMediaInteroperability"], os.path.join(target_dir, "SocialMediaInteroperability"))
    
    if CLONE_HOLOCHAIN:
        print("Cloning Holochain repositories...")
        clone_repos(repos_to_clone["Holochain"], os.path.join(target_dir, "Holochain"))
    
    if CLONE_EBPF:
        print("Cloning eBPF repositories...")
        clone_repos(repos_to_clone["eBPF"], os.path.join(target_dir, "eBPF"))
    
    if CLONE_KAFKA:
        print("Cloning Kafka repositories...")
        clone_repos(repos_to_clone["Kafka"], os.path.join(target_dir, "Kafka"))