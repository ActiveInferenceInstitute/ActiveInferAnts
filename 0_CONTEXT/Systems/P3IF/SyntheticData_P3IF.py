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
            "Social Worker", "Psychologist", "Nutritionist", "Physical Therapist", "Occupational Therapist",
            "Speech Therapist", "Radiologist", "Surgeon", "Anesthesiologist", "Emergency Medical Technician",
            "Laboratory Technician", "Pathologist", "Geneticist", "Oncologist", "Pediatrician",
            "Geriatrician", "Psychiatrist", "Neurologist", "Cardiologist", "Endocrinologist",
            "Dermatologist", "Ophthalmologist", "Dentist", "Pharmacologist", "Biomedical Engineer",
            "Health Economist", "Epidemiologist", "Biostatistician", "Medical Illustrator", "Health Educator",
            "Patient Advocate", "Hospital Chaplain", "Risk Manager", "Quality Improvement Specialist", "Infection Control Specialist"
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
            "Enterprise Adopter", "Central Bank", "Decentralized Finance (DeFi) User", "NFT Artist", "Governance Participant",
            "Protocol Designer", "Blockchain Architect", "Consensus Algorithm Researcher", "Cryptoeconomist", "Blockchain Educator",
            "Blockchain Journalist", "Venture Capitalist", "Blockchain Consultant", "Compliance Officer", "Blockchain Ethicist",
            "Blockchain Governance Specialist", "Tokenomics Expert", "Blockchain Data Scientist", "Smart Contract Developer", "Blockchain Infrastructure Provider",
            "Blockchain Marketing Specialist", "Blockchain Community Manager", "Blockchain Product Manager", "Blockchain UI/UX Designer", "Blockchain Quality Assurance Tester",
            "Blockchain Integration Specialist", "Blockchain Security Auditor", "Blockchain Scalability Researcher", "Blockchain Interoperability Specialist", "Blockchain Sustainability Expert",
            "Blockchain Policy Advisor", "Blockchain Social Impact Specialist", "Blockchain Identity Management Expert", "Blockchain Privacy Researcher", "Blockchain Forensics Analyst"
        ]
    },
    "VideoChat": {
        "properties": [
            "Video Quality", "Audio Quality", "Latency", "Bandwidth Efficiency", "Scalability",
            "Security", "Privacy", "Cross-Platform Compatibility", "User Interface", "Screen Sharing",
            "Recording Capability", "Encryption", "Noise Cancellation", "Virtual Background", "Accessibility",
            "Multi-Party Support", "Mobile Optimization", "Network Adaptability", "Integration Capabilities", "Customization Options",
            "Breakout Rooms", "Live Streaming", "Chat Functionality", "File Sharing", "Whiteboard Feature",
            "Gesture Recognition", "Facial Recognition", "Language Translation", "Closed Captioning", "Emoji Reactions",
            "Attendance Tracking", "Polling/Voting", "Waiting Room", "Host Controls", "Background Blur",
            "Echo Cancellation", "Lip Synchronization", "Bandwidth Management", "Device Compatibility", "Cloud Storage",
            "API Availability", "Analytics Dashboard", "Compliance (GDPR, HIPAA)", "Single Sign-On", "End-to-End Encryption",
            "Firewall Traversal", "Quality of Service (QoS)", "Adaptive Bitrate Streaming", "Low-Light Enhancement", "360-Degree Video Support"
        ],
        "processes": [
            "Video Encoding", "Audio Encoding", "Data Compression", "Packet Transmission", "Jitter Buffer Management",
            "Echo Cancellation", "Noise Suppression", "Video Rendering", "Audio Rendering", "Synchronization",
            "Bandwidth Allocation", "Error Concealment", "Packet Loss Recovery", "Frame Rate Adaptation", "Resolution Scaling",
            "User Authentication", "Session Initiation", "Media Negotiation", "NAT Traversal", "Encryption/Decryption",
            "Screen Capture", "Audio Mixing", "Video Mixing", "Recording", "Transcoding",
            "Background Subtraction", "Facial Detection", "Audio Level Detection", "Gesture Recognition", "Lip Movement Analysis",
            "Network Quality Monitoring", "Adaptive Streaming", "Device Enumeration", "Audio Routing", "Video Filtering",
            "Chat Message Processing", "File Transfer", "Whiteboard Rendering", "Breakout Room Management", "Poll Creation and Analysis",
            "Attendance Logging", "Language Detection", "Speech-to-Text Conversion", "Text-to-Speech Conversion", "Emoji Rendering",
            "Analytics Data Collection", "API Request Handling", "Cloud Synchronization", "Low-Light Image Enhancement", "360-Degree Video Processing"
        ],
        "perspectives": [
            "End User", "IT Administrator", "Software Developer", "Network Engineer", "Security Specialist",
            "User Experience Designer", "Product Manager", "Quality Assurance Tester", "Customer Support Representative", "Sales Representative",
            "Marketing Specialist", "Business Analyst", "Data Scientist", "Legal Counsel", "Compliance Officer",
            "Accessibility Expert", "Localization Specialist", "Training Coordinator", "System Integrator", "Cloud Architect",
            "Mobile Developer", "Web Developer", "DevOps Engineer", "Database Administrator", "UI Designer",
            "UX Researcher", "Content Creator", "Educator", "Healthcare Professional", "Financial Advisor",
            "Human Resources Manager", "Event Organizer", "Project Manager", "Executive", "Entrepreneur",
            "Journalist", "Politician", "Entertainer", "Social Media Influencer", "Customer",
            "Investor", "Regulator", "Privacy Advocate", "Ethical AI Specialist", "Telecommunications Expert",
            "Usability Tester", "Ergonomics Specialist", "Cognitive Psychologist", "Audiologist", "Ophthalmologist"
        ]
    },
    "ActiveInferenceGrantProposal": {
        "properties": [
            "Theoretical Soundness", "Empirical Evidence", "Interdisciplinary Approach", "Novelty", "Practical Applicability",
            "Scalability", "Computational Efficiency", "Biological Plausibility", "Predictive Power", "Explanatory Power",
            "Model Complexity", "Data Requirements", "Interpretability", "Generalizability", "Robustness",
            "Ethical Considerations", "Societal Impact", "Alignment with Funding Priorities", "Cost-Effectiveness", "Timeline Feasibility",
            "Risk Assessment", "Potential for Collaboration", "Publication Potential", "Intellectual Property", "Educational Value",
            "Clinical Relevance", "Technological Innovation", "Methodological Rigor", "Reproducibility", "Sustainability",
            "Adaptability to New Domains", "Integration with Existing Theories", "Potential for Paradigm Shift", "Quantitative Metrics", "Qualitative Insights",
            "Cross-Cultural Applicability", "Long-term Research Potential", "Short-term Deliverables", "Alignment with Institutional Goals", "Public Engagement",
            "Policy Implications", "Economic Viability", "Environmental Considerations", "Ethical AI Alignment", "Potential for Spin-off Research",
            "Interdepartmental Synergies", "International Collaboration Potential", "Industry Partnership Opportunities", "Funding Diversification", "Career Development Aspects"
        ],
        "processes": [
            "Literature Review", "Hypothesis Formulation", "Experimental Design", "Data Collection", "Statistical Analysis",
            "Model Development", "Simulation", "Empirical Testing", "Peer Review", "Grant Writing",
            "Ethics Approval", "Participant Recruitment", "Data Preprocessing", "Feature Engineering", "Model Training",
            "Hyperparameter Optimization", "Cross-Validation", "Error Analysis", "Results Interpretation", "Manuscript Preparation",
            "Conference Presentation", "Code Documentation", "Data Management", "Team Coordination", "Budget Planning",
            "Progress Reporting", "Stakeholder Engagement", "Risk Mitigation", "Quality Assurance", "Knowledge Dissemination",
            "Intellectual Property Protection", "Collaboration Management", "Resource Allocation", "Timeline Management", "Performance Evaluation",
            "Feedback Incorporation", "Iterative Refinement", "Scalability Testing", "Interdisciplinary Integration", "Theoretical Framework Development",
            "Computational Implementation", "Biological Validation", "Clinical Translation", "Policy Brief Preparation", "Public Communication",
            "Funding Acquisition", "Team Recruitment", "Equipment Procurement", "Software Development", "Data Visualization",
            "Ethical Compliance Monitoring", "Impact Assessment", "Long-term Planning", "Knowledge Transfer", "Community Outreach"
        ],
        "perspectives": [
            "Principal Investigator", "Co-Investigator", "Research Assistant", "Statistician", "Data Scientist",
            "Neuroscientist", "Cognitive Psychologist", "Computer Scientist", "Mathematician", "Philosopher",
            "Ethicist", "Funding Agency Representative", "Institutional Review Board Member", "Graduate Student", "Postdoctoral Researcher",
            "Lab Manager", "Collaborator", "Industry Partner", "Policy Maker", "Journal Editor",
            "Peer Reviewer", "Research Participant", "Clinical Practitioner", "AI Ethics Specialist", "Science Communicator",
            "Grant Administrator", "Department Head", "University Dean", "Intellectual Property Lawyer", "Bioethicist",
            "Computational Neuroscientist", "Roboticist", "Cognitive Scientist", "Systems Biologist", "Theoretical Physicist",
            "Machine Learning Engineer", "Neuroengineer", "Behavioral Economist", "Developmental Psychologist", "Evolutionary Biologist",
            "Computational Psychiatrist", "Neuroprosthetics Specialist", "Brain-Computer Interface Expert", "Neuroethicist", "Science Policy Advisor",
            "Public Health Researcher", "Environmental Scientist", "Social Psychologist", "Anthropologist", "Education Researcher"
        ]
    },
    "NationalSecurity": {
        "properties": [
            "Intelligence Gathering", "Threat Assessment", "Border Security", "Cybersecurity", "Counter-terrorism",
            "Military Readiness", "Diplomatic Relations", "Economic Security", "Critical Infrastructure Protection", "Emergency Response",
            "Nuclear Deterrence", "Biosecurity", "Information Warfare", "Surveillance Capabilities", "Alliance Management",
            "Weapons Control", "Counterintelligence", "Homeland Defense", "Maritime Security", "Space Security",
            "Energy Security", "Food Security", "Public Health Preparedness", "Transportation Security", "Financial System Stability",
            "Environmental Security", "Technological Superiority", "Strategic Communications", "Cultural Understanding", "Resilience",
            "Non-Proliferation", "Arms Control", "Disaster Preparedness", "Chemical Security", "Radiological Security",
            "Asymmetric Warfare Defense", "Insider Threat Mitigation", "Supply Chain Security", "Electromagnetic Pulse Protection", "Quantum Technology Security",
            "Artificial Intelligence Security", "Biometric Security", "Drone Defense", "Social Media Monitoring", "Refugee Management",
            "Pandemic Response", "Climate Change Adaptation", "Geopolitical Risk Management", "Psychological Operations Defense", "Critical Mineral Security"
        ],
        "processes": [
            "Intelligence Analysis", "Threat Monitoring", "Border Patrol", "Cyber Defense", "Counter-terrorism Operations",
            "Military Training", "Diplomatic Negotiations", "Economic Sanctions", "Infrastructure Hardening", "Crisis Management",
            "Nuclear Arms Control", "Biosurveillance", "Information Operations", "Surveillance Operations", "Alliance Building",
            "Arms Control Verification", "Counterintelligence Operations", "Homeland Security Coordination", "Maritime Patrols", "Space Monitoring",
            "Energy Resource Protection", "Food Supply Chain Monitoring", "Public Health Emergency Response", "Transportation System Security", "Financial System Monitoring",
            "Environmental Threat Assessment", "Technology Development", "Strategic Messaging", "Cultural Intelligence Gathering", "Resilience Planning",
            "Non-Proliferation Treaty Enforcement", "Arms Reduction Negotiations", "Disaster Response Drills", "Chemical Facility Inspections", "Radiological Detection",
            "Asymmetric Threat Analysis", "Insider Threat Screening", "Supply Chain Risk Management", "EMP Hardening", "Quantum Encryption Development",
            "AI Ethics Implementation", "Biometric Data Management", "Anti-Drone Systems Deployment", "Social Media Analysis", "Refugee Screening",
            "Pandemic Preparedness Planning", "Climate Change Impact Assessment", "Geopolitical Scenario Planning", "Psychological Operations Analysis", "Critical Mineral Stockpiling"
        ],
        "perspectives": [
            "Intelligence Analyst", "Military Commander", "Diplomat", "Cybersecurity Expert", "Counter-terrorism Specialist",
            "Economic Advisor", "Emergency Response Coordinator", "Nuclear Strategist", "Biosecurity Researcher", "Information Warfare Specialist",
            "Surveillance Technician", "Alliance Coordinator", "Arms Control Inspector", "Homeland Security Officer", "Maritime Security Expert",
            "Space Security Analyst", "Energy Security Advisor", "Food Security Specialist", "Public Health Official", "Transportation Security Manager",
            "Financial System Regulator", "Environmental Security Analyst", "Technology Development Officer", "Strategic Communications Expert", "Cultural Anthropologist",
            "Resilience Planner", "Non-Proliferation Treaty Negotiator", "Arms Reduction Specialist", "Disaster Management Expert", "Chemical Security Inspector",
            "Radiological Defense Specialist", "Asymmetric Warfare Analyst", "Insider Threat Investigator", "Supply Chain Security Manager", "EMP Defense Engineer",
            "Quantum Security Researcher", "AI Ethics Officer", "Biometric Systems Engineer", "Drone Defense Specialist", "Social Media Intelligence Analyst",
            "Refugee Coordinator", "Pandemic Response Planner", "Climate Change Security Advisor", "Geopolitical Risk Analyst", "Psychological Operations Specialist",
            "Critical Mineral Strategist", "Border Control Officer", "Customs Inspector", "Infrastructure Protection Specialist", "Crisis Communications Manager"
        ]
    },
    "PowerGrid": {
        "properties": [
            "Generation Capacity", "Transmission Efficiency", "Distribution Reliability", "Grid Stability", "Energy Storage",
            "Renewable Integration", "Demand Response", "Smart Metering", "Grid Resilience", "Cybersecurity",
            "Load Balancing", "Voltage Regulation", "Frequency Control", "Power Quality", "Fault Tolerance",
            "Interoperability", "Asset Management", "Environmental Impact", "Cost Effectiveness", "Regulatory Compliance",
            "Grid Modernization", "Microgrid Integration", "Peak Load Management", "Outage Management", "Power System Flexibility",
            "Grid Congestion Management", "Transmission Capacity", "Substation Automation", "Advanced Metering Infrastructure", "Distributed Energy Resources",
            "Grid Interconnection", "Power System Reliability", "Energy Efficiency", "Demand Forecasting", "Grid Monitoring",
            "Power System Protection", "Reactive Power Compensation", "Harmonics Mitigation", "Islanding Detection", "Fault Location",
            "Power System Restoration", "Grid Code Compliance", "Power Market Integration", "Cross-Border Power Trading", "Grid Data Analytics",
            "Power System Simulation", "Grid Optimization", "Transmission Rights", "Ancillary Services", "Grid Inertia Management"
        ],
        "processes": [
            "Power Generation", "Transmission", "Distribution", "Grid Monitoring", "Energy Storage Management",
            "Renewable Energy Integration", "Demand Forecasting", "Smart Meter Data Collection", "Grid Maintenance", "Cybersecurity Measures",
            "Load Balancing Operations", "Voltage Control", "Frequency Regulation", "Power Quality Management", "Fault Detection and Isolation",
            "System Integration", "Asset Maintenance", "Environmental Impact Assessment", "Cost-Benefit Analysis", "Regulatory Reporting",
            "Grid Modernization Planning", "Microgrid Operation", "Peak Shaving", "Outage Response", "Flexibility Assessment",
            "Congestion Management", "Transmission Capacity Planning", "Substation Control", "AMI Data Management", "DER Integration",
            "Interconnection Studies", "Reliability Analysis", "Energy Auditing", "Load Forecasting", "SCADA Operations",
            "Protection System Coordination", "VAR Compensation", "Power Quality Analysis", "Anti-Islanding Control", "Fault Locating",
            "Black Start Procedures", "Grid Code Compliance Checking", "Market Clearing", "Cross-Border Scheduling", "Big Data Analytics",
            "Power System Modeling", "Grid Optimization Algorithms", "Transmission Rights Allocation", "Ancillary Service Provision", "Synthetic Inertia Control"
        ],
        "perspectives": [
            "Grid Operator", "Power Plant Manager", "Transmission Engineer", "Distribution Technician", "Energy Storage Specialist",
            "Renewable Energy Expert", "Demand Response Manager", "Smart Grid Analyst", "Resilience Planner", "Cybersecurity Specialist",
            "Load Balancing Coordinator", "Voltage Control Engineer", "Frequency Regulation Specialist", "Power Quality Analyst", "Fault Response Team",
            "System Integration Engineer", "Asset Manager", "Environmental Impact Assessor", "Financial Analyst", "Regulatory Compliance Officer",
            "Grid Modernization Strategist", "Microgrid Designer", "Peak Load Analyst", "Outage Management Coordinator", "Flexibility Market Operator",
            "Congestion Management Specialist", "Transmission Planner", "Substation Engineer", "AMI Systems Manager", "DER Integration Specialist",
            "Interconnection Analyst", "Reliability Coordinator", "Energy Efficiency Consultant", "Load Forecasting Analyst", "SCADA Engineer",
            "Protection System Engineer", "Power Factor Correction Specialist", "Harmonics Mitigation Expert", "Islanding Detection Specialist", "Fault Location Analyst",
            "Restoration Coordinator", "Grid Code Compliance Auditor", "Power Market Analyst", "Cross-Border Trading Specialist", "Data Scientist",
            "Power System Simulator", "Grid Optimization Engineer", "Transmission Rights Trader", "Ancillary Services Coordinator", "Grid Inertia Specialist"
        ]
    },
    "Immigration": {
        "properties": [
            "Border Control", "Visa Processing", "Asylum Management", "Integration Programs", "Labor Market Impact",
            "Cultural Diversity", "National Security", "Human Rights", "Demographic Change", "Economic Contribution",
            "Social Cohesion", "Language Acquisition", "Health Screening", "Education Access", "Family Reunification",
            "Citizenship Pathways", "Illegal Immigration Prevention", "Refugee Resettlement", "Skilled Migration", "Temporary Worker Programs",
            "Immigration Policy", "Deportation Procedures", "Detention Facilities", "Legal Aid Services", "Immigrant Entrepreneurship",
            "Remittance Flows", "Brain Drain/Gain", "Dual Citizenship", "Naturalization Process", "Immigration Quotas",
            "Border Technology", "Immigrant Rights", "Cultural Assimilation", "Diaspora Communities", "Human Trafficking Prevention",
            "Seasonal Worker Programs", "Immigration Fraud Detection", "Sanctuary Cities", "Immigration Court System", "Immigrant Health Care",
            "Language Interpretation Services", "Cross-Border Cooperation", "Immigration Data Management", "Immigrant Voting Rights", "Second Generation Integration",
            "Immigration Research", "Immigrant Mental Health", "Unaccompanied Minor Management", "Immigration Advocacy", "Immigrant Education Programs"
        ],
        "processes": [
            "Border Patrol", "Visa Application Processing", "Asylum Claim Evaluation", "Integration Program Implementation", "Labor Market Analysis",
            "Cultural Orientation", "Security Screening", "Human Rights Monitoring", "Demographic Data Collection", "Economic Impact Assessment",
            "Community Engagement", "Language Training", "Health Screening Procedures", "Education Placement", "Family Reunification Processing",
            "Citizenship Application Processing", "Illegal Immigration Enforcement", "Refugee Placement", "Skilled Migrant Selection", "Temporary Work Visa Issuance",
            "Policy Development", "Deportation Proceedings", "Detention Center Management", "Legal Aid Provision", "Entrepreneurship Support",
            "Remittance Tracking", "Brain Drain/Gain Analysis", "Dual Citizenship Processing", "Naturalization Ceremony", "Quota System Management",
            "Border Technology Implementation", "Rights Education", "Cultural Assimilation Programs", "Diaspora Engagement", "Anti-Trafficking Operations",
            "Seasonal Worker Coordination", "Fraud Investigation", "Sanctuary City Policy Enforcement", "Immigration Court Proceedings", "Immigrant Healthcare Provision",
            "Interpretation Service Coordination", "International Border Cooperation", "Immigration Database Management", "Voter Registration for Immigrants", "Second Generation Support Programs",
            "Immigration Research Studies", "Mental Health Service Provision", "Unaccompanied Minor Care", "Advocacy Campaign Management", "Immigrant Education Curriculum Development"
        ],
        "perspectives": [
            "Immigration Officer", "Visa Processor", "Asylum Case Worker", "Integration Program Coordinator", "Labor Market Analyst",
            "Cultural Liaison", "Security Screener", "Human Rights Advocate", "Demographer", "Economic Analyst",
            "Community Outreach Specialist", "Language Instructor", "Health Screening Technician", "Education Placement Officer", "Family Reunification Caseworker",
            "Citizenship Test Administrator", "Border Patrol Agent", "Refugee Resettlement Coordinator", "Skilled Migration Recruiter", "Temporary Visa Officer",
            "Immigration Policy Advisor", "Deportation Officer", "Detention Facility Manager", "Immigration Lawyer", "Immigrant Entrepreneur Mentor",
            "Remittance Analyst", "Brain Drain/Gain Researcher", "Dual Citizenship Processor", "Naturalization Ceremony Official", "Immigration Quota Analyst",
            "Border Technology Specialist", "Immigrant Rights Educator", "Cultural Assimilation Coach", "Diaspora Community Leader", "Anti-Trafficking Investigator",
            "Seasonal Worker Program Manager", "Immigration Fraud Investigator", "Sanctuary City Policy Maker", "Immigration Judge", "Immigrant Healthcare Provider",
            "Language Interpreter", "Cross-Border Cooperation Officer", "Immigration Data Analyst", "Immigrant Voting Rights Advocate", "Second Generation Integration Specialist",
            "Immigration Researcher", "Immigrant Mental Health Counselor", "Unaccompanied Minor Case Manager", "Immigration Advocate", "Immigrant Education Specialist"
        ]
    },
    "ScienceResearch": {
        "properties": [
            "Hypothesis Formulation", "Experimental Design", "Data Collection", "Statistical Analysis", "Peer Review",
            "Reproducibility", "Ethical Considerations", "Funding Allocation", "Interdisciplinary Collaboration", "Technology Integration",
            "Publication Impact", "Innovation Potential", "Societal Relevance", "Environmental Sustainability", "Long-term Viability",
            "Research Integrity", "Knowledge Dissemination", "Talent Development", "International Cooperation", "Industry Partnership",
            "Open Access", "Big Data Management", "Research Infrastructure", "Scientific Method Application", "Research Ethics",
            "Grant Writing", "Laboratory Safety", "Intellectual Property", "Science Communication", "Research Policy",
            "Scientific Literacy", "Research Commercialization", "Citizen Science", "Research Networking", "Scientific Conferences",
            "Research Quality Assurance", "Scientific Instrumentation", "Research Methodology", "Scientific Publishing", "Research Impact Assessment",
            "Science Education", "Research Data Sharing", "Scientific Collaboration Tools", "Research Funding Diversity", "Scientific Advisory Boards",
            "Research Career Development", "Scientific Peer Networks", "Research Project Management", "Scientific Outreach", "Research Evaluation Metrics"
        ],
        "processes": [
            "Literature Review", "Hypothesis Testing", "Data Collection", "Statistical Analysis", "Manuscript Preparation",
            "Peer Review Process", "Replication Studies", "Ethics Committee Review", "Grant Writing", "Collaborative Project Management",
            "Technology Implementation", "Impact Factor Calculation", "Innovation Assessment", "Societal Impact Evaluation", "Sustainability Analysis",
            "Research Integrity Training", "Conference Presentations", "Mentorship Programs", "International Collaboration Coordination", "Industry-Academia Partnerships",
            "Open Access Publishing", "Big Data Analysis", "Research Facility Management", "Experimental Protocol Development", "Ethics Approval Process",
            "Funding Proposal Submission", "Laboratory Safety Training", "Patent Application", "Public Science Communication", "Research Policy Development",
            "Scientific Literacy Programs", "Technology Transfer", "Citizen Science Project Coordination", "Research Network Building", "Conference Organization",
            "Quality Control Procedures", "Equipment Calibration", "Research Design", "Journal Submission", "Impact Measurement",
            "Curriculum Development", "Data Repository Management", "Collaboration Platform Implementation", "Diverse Funding Source Identification", "Advisory Board Meetings",
            "Career Counseling", "Peer Network Facilitation", "Project Timeline Management", "Public Engagement Events", "Bibliometric Analysis"
        ],
        "perspectives": [
            "Principal Investigator", "Research Assistant", "Statistician", "Peer Reviewer", "Ethics Committee Member",
            "Funding Agency Representative", "Interdisciplinary Collaborator", "Technology Specialist", "Journal Editor", "Innovation Officer",
            "Science Policy Advisor", "Sustainability Researcher", "Research Integrity Officer", "Science Communicator", "Graduate Student Mentor",
            "Open Access Advocate", "Data Scientist", "Research Facility Manager", "Methodologist", "Research Ethicist",
            "Grant Writer", "Laboratory Safety Officer", "Intellectual Property Lawyer", "Science Journalist", "Research Policy Maker",
            "Science Educator", "Technology Transfer Officer", "Citizen Science Coordinator", "Research Network Administrator", "Conference Organizer",
            "Quality Assurance Specialist", "Scientific Instrument Technician", "Research Design Consultant", "Scientific Publisher", "Impact Assessment Specialist",
            "Curriculum Developer", "Data Repository Manager", "Collaboration Tool Developer", "Funding Diversity Specialist", "Scientific Advisory Board Member",
            "Career Development Officer", "Peer Network Facilitator", "Project Manager", "Outreach Coordinator", "Bibliometrician"
        ]
    },
    "MathEducation": {
        "properties": [
            "Conceptual Understanding", "Procedural Fluency", "Problem-Solving Skills", "Mathematical Reasoning", "Curriculum Design",
            "Assessment Methods", "Technology Integration", "Equity and Access", "Teacher Preparation", "Student Engagement",
            "Math Anxiety Reduction", "Real-World Application", "Interdisciplinary Connections", "Differentiated Instruction", "Mathematical Modeling",
            "Computational Thinking", "Mathematical Communication", "Growth Mindset Development", "Collaborative Learning", "Mathematical Creativity",
            "Numeracy Skills", "Geometric Visualization", "Algebraic Thinking", "Statistical Literacy", "Mathematical Proof",
            "Mental Math Strategies", "Math Language Development", "Mathematical Argumentation", "Error Analysis", "Mathematical Representations",
            "Math History Integration", "STEM Integration", "Math Competition Preparation", "Math Club Activities", "Parent Math Education",
            "Math Homework Strategies", "Math Study Skills", "Math Test-Taking Strategies", "Math Remediation", "Advanced Math Topics",
            "Math Curriculum Sequencing", "Math Textbook Selection", "Math Manipulatives Use", "Math Games and Puzzles", "Math Project-Based Learning",
            "Math Journaling", "Math Portfolio Assessment", "Math Tutoring Programs", "Math Teacher Professional Development", "Math Education Research"
        ],
        "processes": [
            "Lesson Planning", "Concept Explanation", "Problem Set Design", "Reasoning Exercises", "Curriculum Development",
            "Assessment Creation", "Educational Technology Implementation", "Equity-Focused Teaching", "Teacher Training", "Engagement Strategies",
            "Anxiety Reduction Techniques", "Real-World Problem Integration", "Cross-Subject Collaboration", "Differentiated Teaching", "Modeling Activities",
            "Computational Thinking Exercises", "Mathematical Discussion Facilitation", "Mindset Coaching", "Group Project Coordination", "Creative Problem Design",
            "Numeracy Skill Building", "Geometric Visualization Exercises", "Algebraic Thinking Development", "Statistical Data Analysis", "Proof Writing Instruction",
            "Mental Math Practice", "Math Vocabulary Instruction", "Argumentation Skill Development", "Error Pattern Identification", "Multiple Representation Use",
            "Math History Lesson Integration", "STEM Project Design", "Competition Problem Solving", "Math Club Organization", "Parent Math Workshops",
            "Homework Design and Review", "Study Skill Instruction", "Test Preparation", "Remedial Instruction", "Advanced Topic Introduction",
            "Curriculum Mapping", "Textbook Evaluation", "Manipulative Selection and Use", "Game-Based Learning Implementation", "Project Design and Management",
            "Journal Prompt Creation", "Portfolio Assessment Design", "Tutor Training", "Professional Development Planning", "Action Research Conduction"
        ],
        "perspectives": [
            "Math Teacher", "Curriculum Developer", "Educational Psychologist", "Ed-Tech Specialist", "Equity and Inclusion Officer",
            "Teacher Trainer", "Student Engagement Specialist", "Math Anxiety Counselor", "Industry Liaison", "Interdisciplinary Educator",
            "Special Education Teacher", "Mathematical Modeler", "Computer Science Educator", "Math Communication Coach", "Growth Mindset Trainer",
            "Numeracy Skills Specialist", "Geometry Teacher", "Algebra Instructor", "Statistics Educator", "Mathematical Proof Expert",
            "Mental Math Coach", "Math Language Specialist", "Mathematical Argumentation Coach", "Error Analysis Specialist", "Math Representation Expert",
            "Math Historian", "STEM Coordinator", "Math Competition Coach", "Math Club Advisor", "Parent Education Coordinator",
            "Homework Strategy Specialist", "Study Skills Coach", "Test Prep Specialist", "Math Remediation Expert", "Advanced Math Instructor",
            "Curriculum Sequencing Specialist", "Textbook Selection Committee Member", "Math Manipulatives Specialist", "Educational Game Designer", "Project-Based Learning Facilitator",
            "Math Journaling Coach", "Portfolio Assessment Specialist", "Math Tutor Coordinator", "Professional Development Facilitator", "Math Education Researcher",
            "Differentiated Instruction Specialist", "Math Technology Integration Expert", "Assessment Design Specialist", "Math Literacy Coach", "Data Analysis in Education Expert"
        ]
    },
    "GovernmentAccessibility": {
        "properties": [
            "Physical Accessibility", "Digital Accessibility", "Language Accessibility", "Information Clarity", "Service Availability",
            "Assistive Technology Support", "Inclusive Design", "Staff Training", "Public Awareness", "Feedback Mechanisms",
            "Compliance Monitoring", "Reasonable Accommodations", "Emergency Preparedness", "Cultural Sensitivity", "Outreach Programs",
            "Accessible Transportation", "Voting Accessibility", "Healthcare Access", "Education Access", "Employment Support",
            "Sign Language Interpretation", "Braille Services", "Audio Description", "Captioning Services", "Easy Read Documents",
            "Wheelchair Accessibility", "Sensory-Friendly Environments", "Accessible Websites", "Mobile App Accessibility", "Accessible Documents",
            "Multilingual Services", "Assistive Listening Systems", "Visual Aids", "Tactile Maps", "Accessible Kiosks",
            "Remote Access Services", "Accessible Meeting Spaces", "Inclusive Hiring Practices", "Disability Awareness Training", "Accessible Public Events",
            "Accessible Recreational Facilities", "Accessible Housing Information", "Accessible Complaint Procedures", "Inclusive Policy Making", "Accessible Voting Machines",
            "Accessible Emergency Alerts", "Inclusive Civic Engagement", "Accessible Public Transportation", "Accessible Government Buildings", "Universal Design Implementation"
        ],
        "processes": [
            "Accessibility Audits", "Website Optimization", "Translation Services", "Plain Language Writing", "Service Delivery Planning",
            "Assistive Tech Implementation", "Universal Design Application", "Accessibility Training", "Public Information Campaigns", "Feedback Collection",
            "Compliance Reporting", "Accommodation Request Processing", "Emergency Response Planning", "Cultural Competence Training", "Community Outreach",
            "Transportation Planning", "Voting System Design", "Healthcare Coordination", "Education Support Services", "Job Placement Assistance",
            "Sign Language Interpreter Scheduling", "Braille Document Production", "Audio Description Creation", "Caption Generation", "Easy Read Document Development",
            "Wheelchair Ramp Installation", "Sensory Room Design", "Web Accessibility Testing", "Mobile App Accessibility Testing", "Document Accessibility Conversion",
            "Language Line Services", "Assistive Listening Device Maintenance", "Visual Aid Creation", "Tactile Map Production", "Kiosk Accessibility Upgrade",
            "Remote Service Implementation", "Accessible Meeting Space Design", "Inclusive Recruitment", "Disability Etiquette Training", "Accessible Event Planning",
            "Recreational Facility Adaptation", "Housing Accessibility Information Compilation", "Complaint Procedure Simplification", "Inclusive Policy Development", "Voting Machine Accessibility Testing",
            "Emergency Alert System Adaptation", "Civic Engagement Accessibility Planning", "Public Transit Accessibility Improvement", "Government Building Accessibility Renovation", "Universal Design Consultation"
        ],
        "perspectives": [
            "Accessibility Coordinator", "Web Accessibility Specialist", "Language Access Coordinator", "Plain Language Expert", "Service Delivery Manager",
            "Assistive Technology Specialist", "Universal Design Architect", "Training Coordinator", "Public Relations Officer", "Feedback Analysis Specialist",
            "Compliance Officer", "Accommodations Coordinator", "Emergency Preparedness Planner", "Cultural Liaison", "Outreach Coordinator",
            "Transportation Planner", "Voting Rights Advocate", "Healthcare Access Specialist", "Education Accessibility Expert", "Employment Support Coordinator",
            "Sign Language Interpreter", "Braille Transcriptionist", "Audio Description Specialist", "Captioning Professional", "Easy Read Document Creator",
            "Accessibility Consultant", "Sensory Integration Specialist", "Web Developer", "Mobile App Developer", "Document Accessibility Specialist",
            "Multilingual Services Coordinator", "Assistive Listening Technician", "Visual Information Designer", "Tactile Graphics Specialist", "Kiosk Design Engineer",
            "Remote Services Technician", "Facilities Manager", "Inclusive HR Specialist", "Disability Awareness Trainer", "Event Accessibility Planner",
            "Recreation Therapist", "Housing Accessibility Advisor", "Ombudsman", "Policy Analyst", "Voting Technology Specialist",
            "Emergency Communications Expert", "Civic Engagement Coordinator", "Public Transit Accessibility Specialist", "Architectural Accessibility Expert", "Universal Design Consultant"
        ]
    },
    "ATM_withdrawal": {
        "properties": [
            "Transaction Security", "User Authentication", "Cash Availability", "Machine Reliability", "Network Connectivity",
            "Transaction Speed", "User Interface", "Error Handling", "Maintenance Scheduling", "Fraud Detection",
            "Compliance", "Accessibility", "Energy Efficiency", "Data Privacy", "Service Availability",
            "Card Reader Functionality", "PIN Encryption", "Cash Dispensing Accuracy", "Receipt Printing Quality", "Screen Visibility",
            "Keypad Responsiveness", "Software Stability", "Hardware Durability", "Network Latency", "Transaction Logging",
            "Audit Trail", "Biometric Authentication", "Multi-Factor Authentication", "Cash Recycling", "Foreign Currency Support",
            "Contactless Technology", "Mobile Integration", "Remote Monitoring", "Thermal Management", "Power Backup",
            "Vandalism Resistance", "Environmental Adaptability", "Noise Level", "Queue Management", "Customer Support Integration",
            "Language Support", "Braille Support", "Audio Guidance", "Camera Surveillance", "Anti-Skimming Measures",
            "EMV Chip Technology", "NFC Capability", "Software Update Mechanism", "Diagnostic Capabilities", "Cash Forecasting"
        ],
        "processes": [
            "Card Insertion", "PIN Entry", "Account Verification", "Transaction Processing", "Cash Dispensing",
            "Receipt Printing", "Balance Inquiry", "Mini Statement Printing", "Fund Transfer", "Transaction Cancellation",
            "Error Reporting", "Maintenance Check", "Software Update", "Network Monitoring", "Fraud Monitoring",
            "Cash Replenishment", "Journal Printing", "User Authentication", "Transaction Authorization", "Cash Counting",
            "Receipt Paper Replacement", "Screen Calibration", "Keypad Testing", "Camera Adjustment", "Network Troubleshooting",
            "Software Diagnostics", "Hardware Inspection", "Security Seal Verification", "Cash Cassette Balancing", "Transaction Reconciliation",
            "Audit Log Generation", "Biometric Data Capture", "Encryption Key Management", "Cash Recycling Process", "Currency Verification",
            "Contactless Transaction Processing", "Mobile App Integration", "Remote Diagnostics", "Temperature Monitoring", "Power System Check",
            "Physical Security Check", "Environmental Adaptation", "Noise Level Testing", "Queue Time Monitoring", "Customer Support Routing",
            "Language Selection", "Braille Interface Activation", "Audio Guidance Triggering", "Video Feed Recording", "Anti-Skimming Detection",
            "EMV Chip Reading", "NFC Data Exchange", "Software Patch Installation", "Self-Diagnostic Routine", "Cash Demand Forecasting"
        ],
        "perspectives": [
            "User", "Bank Official", "ATM Technician", "Security Analyst", "Network Administrator",
            "Compliance Officer", "Maintenance Staff", "Customer Service Representative", "Fraud Investigator", "Software Developer",
            "Hardware Engineer", "Cash Management Specialist", "User Experience Designer", "Accessibility Consultant", "Energy Efficiency Expert",
            "Data Privacy Officer", "Service Level Manager", "Card Technology Specialist", "Encryption Expert", "Cash Handling Specialist",
            "Printer Technician", "Display Technology Expert", "Input Device Specialist", "Software Quality Assurance", "Durability Tester",
            "Network Performance Analyst", "Transaction Auditor", "Biometrics Specialist", "Authentication Expert", "Cash Recycling Technician",
            "Foreign Exchange Specialist", "Contactless Payment Expert", "Mobile Integration Specialist", "Remote Monitoring Technician", "Thermal Engineer",
            "Power Systems Engineer", "Physical Security Specialist", "Environmental Adaptation Expert", "Acoustics Engineer", "Queue Management Specialist",
            "Customer Support Integration Expert", "Localization Specialist", "Braille Technology Expert", "Audio Systems Engineer", "Surveillance Specialist",
            "Anti-Fraud Technology Expert", "EMV Technology Specialist", "NFC Technology Expert", "Software Update Manager", "Diagnostic Systems Developer",
            "Cash Forecasting Analyst"
        ]
    },
    "ClimateChange": {
        "properties": [
            "Global Temperature Rise", "Sea Level Rise", "Ocean Acidification", "Extreme Weather Events", "Biodiversity Loss",
            "Carbon Emissions", "Deforestation", "Renewable Energy Adoption", "Climate Policy", "Public Awareness",
            "Greenhouse Gas Concentrations", "Arctic Ice Melt", "Permafrost Thawing", "Desertification", "Coral Reef Bleaching",
            "Agricultural Productivity", "Water Scarcity", "Vector-Borne Diseases", "Climate Migration", "Ecosystem Resilience",
            "Carbon Sequestration", "Urban Heat Islands", "Albedo Effect", "Methane Release", "Ozone Depletion",
            "Climate Justice", "Sustainable Development", "Circular Economy", "Green Infrastructure", "Climate Finance",
            "Air Quality", "Soil Degradation", "Glacial Retreat", "Ocean Circulation Changes", "Wildfire Frequency",
            "Coastal Erosion", "Food Security", "Energy Transition", "Climate Litigation", "Carbon Pricing",
            "Biodiversity Hotspots", "Tipping Points", "Climate Feedback Loops", "Geoengineering", "Climate Refugees",
            "Sustainable Transportation", "Green Building", "Waste Management", "Climate Education", "Indigenous Knowledge"
        ],
        "processes": [
            "Emissions Monitoring", "Climate Modeling", "Policy Implementation", "Renewable Energy Integration", "Reforestation",
            "Carbon Capture and Storage", "Sustainable Agriculture", "Climate Education", "Disaster Risk Reduction", "Adaptation Planning",
            "International Negotiations", "Green Technology Innovation", "Emissions Trading", "Climate Impact Assessment", "Biodiversity Conservation",
            "Sustainable Urban Planning", "Climate-Resilient Infrastructure", "Waste Management", "Water Conservation", "Energy Efficiency Improvement",
            "Climate Data Analysis", "Early Warning Systems", "Ecosystem Restoration", "Sustainable Transportation", "Climate-Smart Agriculture",
            "Ocean Monitoring", "Atmospheric Sampling", "Satellite Observation", "Climate Policy Formulation", "Public Engagement Campaigns",
            "Greenhouse Gas Inventory", "Arctic Research", "Permafrost Monitoring", "Desertification Control", "Coral Reef Protection",
            "Crop Yield Forecasting", "Water Resource Management", "Disease Vector Control", "Migration Pattern Analysis", "Ecosystem Services Valuation",
            "Carbon Offset Projects", "Urban Planning for Heat Mitigation", "Albedo Enhancement Research", "Methane Capture", "Ozone Layer Monitoring",
            "Environmental Justice Advocacy", "Sustainable Development Goal Implementation", "Circular Economy Transition", "Green Infrastructure Planning", "Climate Finance Allocation",
            "Air Quality Monitoring", "Soil Conservation", "Glacier Monitoring", "Ocean Current Mapping", "Wildfire Management"
        ],
        "perspectives": [
            "Climate Scientist", "Policymaker", "Environmental Activist", "Renewable Energy Developer", "Sustainability Consultant",
            "Farmer", "Urban Planner", "Disaster Management Specialist", "Climate Economist", "Indigenous Representative",
            "Marine Biologist", "Energy Sector Analyst", "Climate Journalist", "Green Tech Entrepreneur", "Climate Educator",
            "International Negotiator", "Climate Risk Analyst", "Biodiversity Researcher", "Climate Justice Advocate", "Circular Economy Specialist",
            "Atmospheric Scientist", "Oceanographer", "Glaciologist", "Ecologist", "Meteorologist",
            "Environmental Lawyer", "Sustainable Finance Expert", "Carbon Market Analyst", "Climate Psychologist", "Geoengineering Researcher",
            "Water Resource Manager", "Public Health Specialist", "Climate Migration Expert", "Ecosystem Services Economist", "Renewable Energy Engineer",
            "Green Building Architect", "Waste Management Specialist", "Environmental Education Coordinator", "Indigenous Knowledge Expert", "Climate Policy Analyst",
            "Sustainable Agriculture Specialist", "Climate Adaptation Planner", "Disaster Risk Reduction Expert", "Climate Communication Specialist", "Environmental Ethicist",
            "Climate Tech Investor", "Sustainable Transportation Planner", "Climate Resilience Officer", "Carbon Capture Technologist", "Climate Data Scientist"
        ]
    },
    "ArtificialIntelligence": {
        "properties": [
            "Machine Learning", "Neural Networks", "Natural Language Processing", "Computer Vision", "Robotics",
            "Expert Systems", "Reinforcement Learning", "Explainable AI", "Ethical AI", "AI Governance",
            "Data Privacy", "AI Bias", "AI Safety", "Quantum AI", "Edge AI",
            "Federated Learning", "Transfer Learning", "Generative AI", "Autonomous Systems", "Human-AI Interaction",
            "Deep Learning", "Cognitive Computing", "Swarm Intelligence", "Evolutionary Computation", "Fuzzy Logic",
            "Knowledge Representation", "Automated Reasoning", "Speech Recognition", "Image Processing", "Predictive Analytics",
            "Anomaly Detection", "Recommendation Systems", "Sentiment Analysis", "Chatbots", "Virtual Assistants",
            "Automated Decision Making", "AI-Powered Simulation", "AI in Cybersecurity", "AI for Scientific Discovery", "AI in Healthcare",
            "AI in Finance", "AI in Education", "AI in Manufacturing", "AI in Agriculture", "AI in Transportation",
            "AI Ethics", "AI Regulation", "AI Transparency", "AI Accountability", "AI Fairness",
            "AI Robustness", "AI Scalability", "AI Energy Efficiency", "AI Hardware Acceleration", "AI Model Compression"
        ],
        "processes": [
            "Data Collection", "Data Preprocessing", "Model Training", "Model Evaluation", "Hyperparameter Tuning",
            "Feature Engineering", "Algorithm Selection", "Deployment", "Monitoring", "Maintenance",
            "Ethical Review", "Bias Detection", "Privacy Preservation", "Explainability Analysis", "Safety Testing",
            "User Interface Design", "Integration with Existing Systems", "Continuous Learning", "Version Control", "Documentation",
            "Data Augmentation", "Cross-Validation", "Ensemble Learning", "Transfer Learning", "Federated Learning",
            "Model Compression", "Hardware Acceleration", "Edge Deployment", "Cloud Deployment", "A/B Testing",
            "Error Analysis", "Performance Optimization", "Scalability Testing", "Security Auditing", "Compliance Checking",
            "Data Visualization", "Interpretability Analysis", "Fairness Assessment", "Robustness Testing", "Adversarial Testing",
            "Energy Efficiency Optimization", "Model Versioning", "Data Pipeline Management", "Model Serving", "Online Learning",
            "Reinforcement Learning Training", "Generative Model Training", "Unsupervised Learning", "Semi-Supervised Learning", "Active Learning"
        ],
        "perspectives": [
            "AI Researcher", "Data Scientist", "Machine Learning Engineer", "AI Ethicist", "AI Policy Maker",
            "Domain Expert", "End User", "AI Product Manager", "AI Safety Specialist", "AI Governance Expert",
            "AI Educator", "AI Entrepreneur", "AI Investor", "AI Critic", "AI Rights Advocate"
        ]
    },
    "QuantumComputing": {
        "properties": [
            "Superposition", "Entanglement", "Quantum Gates", "Qubits", "Quantum Algorithms",
            "Quantum Error Correction", "Quantum Supremacy", "Quantum Cryptography", "Quantum Sensing", "Quantum Simulation",
            "Quantum Annealing", "Quantum Machine Learning", "Quantum Internet", "Quantum Software", "Quantum Hardware"
        ],
        "processes": [
            "Qubit Initialization", "Quantum Circuit Design", "Quantum State Preparation", "Quantum Measurement", "Quantum Error Mitigation",
            "Quantum Algorithm Implementation", "Quantum Compiler Optimization", "Quantum Debugger", "Quantum Simulator", "Quantum-Classical Interfacing",
            "Quantum Hardware Calibration", "Quantum Network Protocol", "Quantum Key Distribution", "Quantum Teleportation", "Quantum Memory Management"
        ],
        "perspectives": [
            "Quantum Physicist", "Quantum Engineer", "Quantum Algorithm Designer", "Quantum Software Developer", "Quantum Hardware Specialist",
            "Quantum Cryptographer", "Quantum Information Theorist", "Quantum Error Correction Specialist", "Quantum Complexity Theorist", "Quantum Applications Researcher",
            "Quantum Policy Maker", "Quantum Educator", "Quantum Entrepreneur", "Quantum Investor", "Quantum Ethics Specialist"
        ]
    },
    "Pipette_Use_In_Wet_Lab": {
        "properties": [
            "Accuracy", "Precision", "Ergonomics", "Volume Range", "Tip Compatibility",
            "Ease of Calibration", "Durability", "Chemical Resistance", "Autoclavability", "User Comfort",
            "Single Channel", "Multi-Channel", "Electronic", "Manual", "Adjustable Volume",
            "Fixed Volume", "Lightweight", "Digital Display", "Maintenance Requirements", "Cost Efficiency",
            "Contamination Prevention", "User Safety", "Reproducibility", "Pipetting Speed", "Liquid Retention",
            "Tip Ejection Force", "Grip Comfort", "Balance", "Material Quality", "Warranty"
        ],
        "processes": [
            "Sample Preparation", "Serial Dilution", "Reagent Addition", "Cell Culture", "PCR Setup",
            "ELISA", "Western Blotting", "DNA Extraction", "RNA Extraction", "Protein Purification",
            "Liquid Handling", "Assay Development", "High-Throughput Screening", "Genotyping", "Cloning",
            "Transformation", "Transfection", "Library Preparation", "Sequencing", "Chromatography",
            "Mass Spectrometry", "Flow Cytometry", "Microscopy", "Immunostaining", "In Situ Hybridization",
            "Cell Sorting", "Cell Counting", "Cell Viability Assay", "Enzyme Assay", "Metabolite Analysis",
            "Titration", "Buffer Preparation", "Media Preparation", "Sterilization", "Quality Control",
            "Calibration", "Validation", "Standard Curve Preparation", "Sample Storage", "Sample Transport",
            "Sample Mixing", "Sample Aliquoting", "Sample Homogenization", "Sample Filtration", "Sample Centrifugation",
            "Sample Labeling", "Sample Thawing", "Sample Freezing", "Sample Incubation", "Sample Vortexing"
        ],
        "perspectives": [
            "Lab Technician", "Research Scientist", "Principal Investigator", "Lab Manager", "Quality Control Specialist",
            "Clinical Researcher", "Pharmaceutical Scientist", "Biotechnologist", "Microbiologist", "Molecular Biologist",
            "Geneticist", "Biochemist", "Cell Biologist", "Immunologist", "Pathologist",
            "Forensic Scientist", "Environmental Scientist", "Agricultural Scientist", "Food Scientist", "Veterinary Scientist",
            "Chemical Engineer", "Biomedical Engineer", "Regulatory Affairs Specialist", "Lab Equipment Sales Representative", "Technical Support Specialist",
            "Lab Assistant", "Postdoctoral Researcher", "Graduate Student", "Undergraduate Student", "Lab Coordinator",
            "Lab Safety Officer", "Lab Automation Specialist", "Lab IT Specialist", "Lab Procurement Officer", "Lab Maintenance Technician"
        ]
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