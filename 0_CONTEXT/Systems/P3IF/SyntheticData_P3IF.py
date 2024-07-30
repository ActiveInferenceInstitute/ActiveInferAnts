import json
import random
import os
from faker import Faker
import logging

# Define domain-specific data
DOMAINS = {
    "HealthCare": {
        "properties": [
            "Patient Safety", "Data Privacy", "Treatment Efficacy", "Cost Effectiveness", "Accessibility",
            "Interoperability", "Regulatory Compliance", "Patient Satisfaction", "Staff Efficiency", "Equipment Reliability",
            "Infection Control", "Medication Accuracy", "Diagnostic Precision", "Emergency Readiness", "Continuity of Care",
            "Informed Consent", "Cultural Competence", "Ethical Practice", "Evidence-Based Care", "Patient Empowerment",
            "Preventive Care", "Chronic Disease Management", "Pain Management", "End-of-Life Care", "Mental Health Integration",
            "Telemedicine Capability", "Health Literacy", "Patient Engagement", "Care Coordination", "Quality Assurance",
            "Resource Allocation", "Staff Competency", "Technology Integration", "Patient Rights", "Environmental Safety",
            "Nutritional Care", "Rehabilitation Services", "Pharmaceutical Management", "Genetic Testing", "Personalized Medicine",
            "Palliative Care", "Organ Donation", "Blood Safety", "Radiation Safety", "Waste Management",
            "Disaster Preparedness", "Community Outreach", "Research Ethics", "Medical Education", "Patient Advocacy"
        ],
        "processes": [
            "Patient Registration", "Triage", "Diagnosis", "Treatment Planning", "Medication Administration",
            "Surgery", "Laboratory Testing", "Imaging", "Patient Monitoring", "Discharge Planning",
            "Follow-up Care", "Referral Management", "Emergency Response", "Infection Prevention", "Quality Assurance",
            "Staff Training", "Medical Records Management", "Inventory Management", "Billing and Coding", "Insurance Verification",
            "Appointment Scheduling", "Patient Education", "Consent Obtaining", "Care Coordination", "Risk Assessment",
            "Clinical Trials", "Telemedicine Consultation", "Prescription Management", "Rehabilitation", "Palliative Care",
            "Mental Health Assessment", "Nutritional Assessment", "Pain Management", "Health Screening", "Immunization",
            "Genetic Counseling", "Organ Transplantation", "Blood Transfusion", "Radiation Therapy", "Chemotherapy",
            "Physical Therapy", "Occupational Therapy", "Speech Therapy", "Respiratory Therapy", "Dialysis",
            "Wound Care", "Anesthesia Administration", "Patient Transport", "Sterilization", "Waste Disposal"
        ],
        "perspectives": [
            "Patient", "Physician", "Nurse", "Administrator", "Insurer",
            "Regulator", "Researcher", "Pharmacist", "Technician", "Caregiver",
            "Public Health Official", "Ethicist", "Legal Counsel", "Financial Analyst", "IT Specialist",
            "Social Worker", "Psychologist", "Nutritionist", "Physical Therapist", "Occupational Therapist"
        ]
    },
    "Blockchain": {
        "properties": [
            "Decentralization", "Transparency", "Immutability", "Security", "Consensus",
            "Cryptography", "Scalability", "Interoperability", "Privacy", "Smart Contract Functionality",
            "Energy Efficiency", "Transaction Speed", "Governance", "Tokenization", "Auditability",
            "Fault Tolerance", "Anonymity", "Programmability", "Finality", "Determinism",
            "Latency", "Throughput", "Network Effect", "Incentive Mechanism", "Adaptability",
            "Compliance", "Upgradability", "Quantum Resistance", "Cross-Chain Communication", "Data Integrity",
            "Accessibility", "Usability", "Reversibility", "Sustainability", "Resilience",
            "Composability", "Liquidity", "Atomicity", "Consistency", "Isolation",
            "Durability", "Sharding", "Staking", "Mining Efficiency", "Forking Resistance",
            "Censorship Resistance", "Permissionless Nature", "Trustlessness", "Verifiability", "Portability"
        ],
        "processes": [
            "Transaction Validation", "Block Creation", "Consensus Mechanism", "Mining", "Staking",
            "Smart Contract Execution", "Wallet Management", "Key Generation", "Signature Verification", "Hashing",
            "Node Synchronization", "Network Propagation", "Fork Resolution", "Chain Reorganization", "Merkle Tree Construction",
            "Address Generation", "Token Minting", "Token Burning", "Gas Fee Calculation", "State Transition",
            "Sharding", "Layer 2 Scaling", "Cross-Chain Transfer", "Atomic Swap", "Governance Voting",
            "Oracle Data Feeding", "Identity Verification", "Tokenization", "Initial Coin Offering", "Airdrop",
            "Yield Farming", "Liquidity Provision", "Decentralized Exchange", "Lending and Borrowing", "Insurance Claim Processing",
            "Non-Fungible Token (NFT) Creation", "Decentralized Autonomous Organization (DAO) Operation", "Stablecoin Pegging", "Privacy Preservation", "Zero-Knowledge Proof Generation",
            "Sidechain Operation", "Interoperability Protocol", "Blockchain Indexing", "Block Explorer Operation", "Hard Fork Implementation",
            "Soft Fork Implementation", "Node Discovery", "Peer-to-Peer Communication", "Mempool Management", "Chain Analysis"
        ],
        "perspectives": [
            "Developer", "Miner", "Node Operator", "Token Holder", "Smart Contract Auditor",
            "Regulator", "Investor", "Exchange Operator", "Blockchain Analyst", "Cryptographer",
            "Economist", "Legal Expert", "Privacy Advocate", "Security Researcher", "User Experience Designer",
            "Enterprise Adopter", "Central Bank", "Decentralized Finance (DeFi) User", "NFT Artist", "Governance Participant"
        ]
    },
    "NationalSecurity": {
        "properties": [
            "Intelligence Gathering", "Threat Assessment", "Border Security", "Cybersecurity", "Counter-terrorism",
            "Military Readiness", "Diplomatic Relations", "Economic Security", "Critical Infrastructure Protection", "Emergency Response",
            "Nuclear Deterrence", "Biosecurity", "Information Warfare", "Surveillance Capabilities", "Alliance Management",
            "Weapons Control", "Counterintelligence", "Homeland Defense", "Maritime Security", "Space Security"
        ],
        "processes": [
            "Intelligence Analysis", "Threat Monitoring", "Border Patrol", "Cyber Defense", "Counter-terrorism Operations",
            "Military Training", "Diplomatic Negotiations", "Economic Sanctions", "Infrastructure Hardening", "Crisis Management",
            "Nuclear Arms Control", "Biosurveillance", "Information Operations", "Surveillance Operations", "Alliance Building",
            "Arms Control Verification", "Counterintelligence Operations", "Homeland Security Coordination", "Maritime Patrols", "Space Monitoring"
        ],
        "perspectives": [
            "Intelligence Analyst", "Military Commander", "Diplomat", "Cybersecurity Expert", "Counter-terrorism Specialist",
            "Economic Advisor", "Emergency Response Coordinator", "Nuclear Strategist", "Biosecurity Researcher", "Information Warfare Specialist",
            "Surveillance Technician", "Alliance Coordinator", "Arms Control Inspector", "Homeland Security Officer", "Maritime Security Expert"
        ]
    },
    "PowerGrid": {
        "properties": [
            "Generation Capacity", "Transmission Efficiency", "Distribution Reliability", "Grid Stability", "Energy Storage",
            "Renewable Integration", "Demand Response", "Smart Metering", "Grid Resilience", "Cybersecurity",
            "Load Balancing", "Voltage Regulation", "Frequency Control", "Power Quality", "Fault Tolerance",
            "Interoperability", "Asset Management", "Environmental Impact", "Cost Effectiveness", "Regulatory Compliance"
        ],
        "processes": [
            "Power Generation", "Transmission", "Distribution", "Grid Monitoring", "Energy Storage Management",
            "Renewable Energy Integration", "Demand Forecasting", "Smart Meter Data Collection", "Grid Maintenance", "Cybersecurity Measures",
            "Load Balancing Operations", "Voltage Control", "Frequency Regulation", "Power Quality Management", "Fault Detection and Isolation",
            "System Integration", "Asset Maintenance", "Environmental Impact Assessment", "Cost-Benefit Analysis", "Regulatory Reporting"
        ],
        "perspectives": [
            "Grid Operator", "Power Plant Manager", "Transmission Engineer", "Distribution Technician", "Energy Storage Specialist",
            "Renewable Energy Expert", "Demand Response Manager", "Smart Grid Analyst", "Resilience Planner", "Cybersecurity Specialist",
            "Load Balancing Coordinator", "Voltage Control Engineer", "Frequency Regulation Specialist", "Power Quality Analyst", "Fault Response Team"
        ]
    },
    "Immigration": {
        "properties": [
            "Border Control", "Visa Processing", "Asylum Management", "Integration Programs", "Labor Market Impact",
            "Cultural Diversity", "National Security", "Human Rights", "Demographic Change", "Economic Contribution",
            "Social Cohesion", "Language Acquisition", "Health Screening", "Education Access", "Family Reunification",
            "Citizenship Pathways", "Illegal Immigration Prevention", "Refugee Resettlement", "Skilled Migration", "Temporary Worker Programs"
        ],
        "processes": [
            "Border Patrol", "Visa Application Processing", "Asylum Claim Evaluation", "Integration Program Implementation", "Labor Market Analysis",
            "Cultural Orientation", "Security Screening", "Human Rights Monitoring", "Demographic Data Collection", "Economic Impact Assessment",
            "Community Engagement", "Language Training", "Health Screening Procedures", "Education Placement", "Family Reunification Processing",
            "Citizenship Application Processing", "Illegal Immigration Enforcement", "Refugee Placement", "Skilled Migrant Selection", "Temporary Work Visa Issuance"
        ],
        "perspectives": [
            "Immigration Officer", "Visa Processor", "Asylum Case Worker", "Integration Program Coordinator", "Labor Market Analyst",
            "Cultural Liaison", "Security Screener", "Human Rights Advocate", "Demographer", "Economic Analyst",
            "Community Outreach Specialist", "Language Instructor", "Health Screening Technician", "Education Placement Officer", "Family Reunification Caseworker"
        ]
    },
    "ScienceResearch": {
        "properties": [
            "Hypothesis Formulation", "Experimental Design", "Data Collection", "Statistical Analysis", "Peer Review",
            "Reproducibility", "Ethical Considerations", "Funding Allocation", "Interdisciplinary Collaboration", "Technology Integration",
            "Publication Impact", "Innovation Potential", "Societal Relevance", "Environmental Sustainability", "Long-term Viability",
            "Research Integrity", "Knowledge Dissemination", "Talent Development", "International Cooperation", "Industry Partnership"
        ],
        "processes": [
            "Literature Review", "Hypothesis Testing", "Data Collection", "Statistical Analysis", "Manuscript Preparation",
            "Peer Review Process", "Replication Studies", "Ethics Committee Review", "Grant Writing", "Collaborative Project Management",
            "Technology Implementation", "Impact Factor Calculation", "Innovation Assessment", "Societal Impact Evaluation", "Sustainability Analysis",
            "Research Integrity Training", "Conference Presentations", "Mentorship Programs", "International Collaboration Coordination", "Industry-Academia Partnerships"
        ],
        "perspectives": [
            "Principal Investigator", "Research Assistant", "Statistician", "Peer Reviewer", "Ethics Committee Member",
            "Funding Agency Representative", "Interdisciplinary Collaborator", "Technology Specialist", "Journal Editor", "Innovation Officer",
            "Science Policy Advisor", "Sustainability Researcher", "Research Integrity Officer", "Science Communicator", "Graduate Student Mentor"
        ]
    },
    "MathEducation": {
        "properties": [
            "Conceptual Understanding", "Procedural Fluency", "Problem-Solving Skills", "Mathematical Reasoning", "Curriculum Design",
            "Assessment Methods", "Technology Integration", "Equity and Access", "Teacher Preparation", "Student Engagement",
            "Math Anxiety Reduction", "Real-World Application", "Interdisciplinary Connections", "Differentiated Instruction", "Mathematical Modeling",
            "Computational Thinking", "Mathematical Communication", "Growth Mindset Development", "Collaborative Learning", "Mathematical Creativity"
        ],
        "processes": [
            "Lesson Planning", "Concept Explanation", "Problem Set Design", "Reasoning Exercises", "Curriculum Development",
            "Assessment Creation", "Educational Technology Implementation", "Equity-Focused Teaching", "Teacher Training", "Engagement Strategies",
            "Anxiety Reduction Techniques", "Real-World Problem Integration", "Cross-Subject Collaboration", "Differentiated Teaching", "Modeling Activities",
            "Computational Thinking Exercises", "Mathematical Discussion Facilitation", "Mindset Coaching", "Group Project Coordination", "Creative Problem Design"
        ],
        "perspectives": [
            "Math Teacher", "Curriculum Developer", "Educational Psychologist", "Ed-Tech Specialist", "Equity and Inclusion Officer",
            "Teacher Trainer", "Student Engagement Specialist", "Math Anxiety Counselor", "Industry Liaison", "Interdisciplinary Educator",
            "Special Education Teacher", "Mathematical Modeler", "Computer Science Educator", "Math Communication Coach", "Growth Mindset Trainer"
        ]
    },
    "GovernmentAccessibility": {
        "properties": [
            "Physical Accessibility", "Digital Accessibility", "Language Accessibility", "Information Clarity", "Service Availability",
            "Assistive Technology Support", "Inclusive Design", "Staff Training", "Public Awareness", "Feedback Mechanisms",
            "Compliance Monitoring", "Reasonable Accommodations", "Emergency Preparedness", "Cultural Sensitivity", "Outreach Programs",
            "Accessible Transportation", "Voting Accessibility", "Healthcare Access", "Education Access", "Employment Support"
        ],
        "processes": [
            "Accessibility Audits", "Website Optimization", "Translation Services", "Plain Language Writing", "Service Delivery Planning",
            "Assistive Tech Implementation", "Universal Design Application", "Accessibility Training", "Public Information Campaigns", "Feedback Collection",
            "Compliance Reporting", "Accommodation Request Processing", "Emergency Response Planning", "Cultural Competence Training", "Community Outreach",
            "Transportation Planning", "Voting System Design", "Healthcare Coordination", "Education Support Services", "Job Placement Assistance"
        ],
        "perspectives": [
            "Accessibility Coordinator", "Web Accessibility Specialist", "Language Access Coordinator", "Plain Language Expert", "Service Delivery Manager",
            "Assistive Technology Specialist", "Universal Design Architect", "Training Coordinator", "Public Relations Officer", "Feedback Analysis Specialist",
            "Compliance Officer", "Accommodations Coordinator", "Emergency Preparedness Planner", "Cultural Liaison", "Outreach Coordinator"
        ]
    },
    "ATM_withdrawal": {
        "properties": [
            "Transaction Security", "User Authentication", "Cash Availability", "Machine Reliability", "Network Connectivity",
            "Transaction Speed", "User Interface", "Error Handling", "Maintenance Scheduling", "Fraud Detection",
            "Compliance", "Accessibility", "Energy Efficiency", "Data Privacy", "Service Availability"
        ],
        "processes": [
            "Card Insertion", "PIN Entry", "Account Verification", "Transaction Processing", "Cash Dispensing",
            "Receipt Printing", "Balance Inquiry", "Mini Statement Printing", "Fund Transfer", "Transaction Cancellation",
            "Error Reporting", "Maintenance Check", "Software Update", "Network Monitoring", "Fraud Monitoring"
        ],
        "perspectives": [
            "User", "Bank Official", "ATM Technician", "Security Analyst", "Network Administrator",
            "Compliance Officer", "Maintenance Staff", "Customer Service Representative", "Fraud Investigator", "Software Developer"
        ]
    }
}

def generate_synthetic_data(domain_name):
    fake = Faker()
    domain = DOMAINS[domain_name]
    
    # Generate patterns
    patterns = []
    pattern_id = 1
    for item_type in ["property", "process", "perspective"]:
        plural_type = "properties" if item_type == "property" else "perspectives" if item_type == "perspective" else item_type + "es"
        for item in domain[plural_type]:
            pattern = {
                "id": pattern_id,
                "name": item,
                "description": fake.sentence(),
                "type": item_type
            }
            patterns.append(pattern)
            pattern_id += 1

    # Generate relationships
    relationships = []
    relationship_id = 1
    num_relationships = 100  # Set the number of relationships to match p3if_export.json
    for _ in range(num_relationships):
        property_id = random.choice([p["id"] for p in patterns if p["type"] == "property"] + [None])
        process_id = random.choice([p["id"] for p in patterns if p["type"] == "process"] + [None])
        perspective_id = random.choice([p["id"] for p in patterns if p["type"] == "perspective"] + [None])
        
        # Ensure at least one of property_id, process_id, or perspective_id is not None
        while property_id is None and process_id is None and perspective_id is None:
            property_id = random.choice([p["id"] for p in patterns if p["type"] == "property"] + [None])
            process_id = random.choice([p["id"] for p in patterns if p["type"] == "process"] + [None])
            perspective_id = random.choice([p["id"] for p in patterns if p["type"] == "perspective"] + [None])
        
        relationship = {
            "id": relationship_id,
            "property_id": property_id,
            "process_id": process_id,
            "perspective_id": perspective_id,
            "strength": round(random.uniform(0, 1), 4)
        }
        relationships.append(relationship)
        relationship_id += 1

    # Create the final structure
    data = {
        "patterns": patterns,
        "relationships": relationships
    }

    return data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Ensure the directory exists
    os.makedirs("P3IF_export", exist_ok=True)
    
    for domain in DOMAINS.keys():
        try:
            data = generate_synthetic_data(domain)
            
            # Write the data to a JSON file
            filename = f"P3IF_export/p3if_export_{domain.lower()}.json"
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Generated synthetic data for {domain} domain: {filename}")
        except Exception as e:
            logger.error(f"Error generating data for {domain} domain: {str(e)}")

if __name__ == "__main__":
    main()