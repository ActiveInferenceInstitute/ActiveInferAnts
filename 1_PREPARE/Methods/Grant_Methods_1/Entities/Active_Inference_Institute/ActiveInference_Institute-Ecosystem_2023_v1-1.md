The Active Inference Institute and Active Inference Ecosystem 
August 19th, 2023 ~ Version #001.1
Active Inference Institute 1*, Ander Aguirre 1,2, John Boik 1, Libor Burian 1, Matthew Brown 1,3, RJ Cordes 1, Scott David 1,4, David S. Douglass 1, Pablo Fernandez-Maquieira 1,5, Daniel Ari Friedman 1,6, Holly Grimm 1, Avel Guénin–Carlut 1,7,8,9, Maria Luiza Iennaco 1,10, V. Bleu Knight 1, Alexandra Mikhailova 1,6, Ali Rahmjoo 1, Adeel Razi 1,11,12,13, Jakub Smékal 1, Ronen Tamari 1,14,15, Dean Tickles 1, Alex Vyatkin 1
* All authors contributed in different ways to the work, and are listed here alphabetically by last name. Contact: Blanket@ActiveInference.Institute
ORCID: AII: 0009-0008-7721-7407, AA: 0000-0002-6337-8292, JB: 0000-0003-1289-7997, LB: 0009-0007-6181-340X , MB: 0000-0002-7552-0989, RJC: 0000-0002-9913-7159, SD: 0000-0003-0679-3286 , DSD: 0000-0001-7894-8019, PF-M, DAF: 0000-0001-6232-9096, HG: 0009-0001-6181-2569, AGC: 0000-0001-8239-7264, MLV: 0000-0002-5407-4852, VBK:0000-0002-9894-1989, AM: 0000-0002-8699-7125, ARahmjoo: 0000-0002-3244-7419, ARazi: 0000-0002-0779-9439, JS: 0000-0003-4989-4968, RT: 0000-0002-6049-591X, DT 0000-0003-2213-0773, AV: 0000-0003-1306-4620
Affiliations
    1. Active Inference Institute
    2. Ohio State University
    3. ThoughtForge Inc.
    4. Information Risk and Synthetic Intelligence Research Initiative (IRSIRI), University of Washington - Applied Physics Laboratory.
    5. NFT-Crap
    6. University of California, Davis
    7. Verses Lab
    8. University of Sussex
    9. Kairos Research
    10. University of São Paulo
    11. Turner Institute for Brain and Mental Health, Monash University, Australia
    12. Wellcome Centre for Human NeuroImaging, University College London
    13. CIFAR Azrieli Global Scholars program, CIFAR, Toronto, Canada
    14. Hebrew University of Jerusalem
    15. Common SenseMakers
Table of Contents
Table of Contents	2
Abstract	3
Preamble	4
The Active Inference Institute	5
Our Vision	7
Our Values and Principles	7
Priorities and Challenge Areas	8
The Way Ahead	9
History of The Institute	10
Possibilities	12
Challenges	13
Next Steps	14
Institute Organization Model	15
Institute Governance and Leadership	15
Members	15
Board of Directors	15
Scientific Advisory Board	15
Officers	15
Institute Units (Support, Projects, and Programs)	16
Administrative Unit	16
EduActive Unit	16
ReInference unit	17
Volunteer Program	19
Internship Program	19
Community Growth and Development	20
Ecosystem Structure	20
Community Structure	21
Participants (Members and Learners)	21
Users (Adopters and Beneficiaries)	21
Research Partners (External Research Organizations and Working Groups)	22
Educational Partners (Universities and Educators)	22
Funders (Donors, Supporters, and Funding Agencies)	22
Information Management and Tech Stack	22
Coda (Modeling, Project, and Knowledge Management Platform)	23
YouTube (Live Streaming and Video Hosting)	23
Discord (Forum and Instant Messaging)	23
Google Workspace (Document Management, Document Production, and Email)	24
Twitter (now “X”) (Public Announcements and Releases)	24
Communications Plan	24
Internal Communications Plan	24
External Communications Plan	25
Target Audiences	25
Approach	25
Organizational Communication	26
Target Audiences	26
Approach	26
Ecosystem Support, Infrastructure, and Administration	27
Informational Commons	27
Infrastructure and Administration	27
Quality, Performance, and Growth Evaluation	28
Participant scale	28
Institute scale	28
Ecosystem scale	29
Discussion and Future Directions	30
Appendix	32
Open source services of The Institute for the Ecosystem	32
Educational services	32
Research services	32
Standards activities	33
Facilitation activities	33
Governance activities	34
Works Cited	35

Abstract
This document briefly surveys the current state of the Active Inference Institute and Active Inference Ecosystem, and outlines our future directions. It will be versioned as a living representation (both cyclic and updating) of ecosystems both general and local, describing the past, present, and future actions of the Active Inference Institute. 



Preamble
Active Inference is an integrated physics-based approach to modeling cognition and behavior as the active minimization of prediction error [1–3]. More exactly, it describes in mathematical terms the tendency of complex adaptive systems to self-organize as to maintain low-surprise states (formally, through minimization of the statistical quantity of Variational Free Energy). Active Inference treats this tendency as the basic process, enabling the modeling of perception and behavior in various kinds of cognitive agents, including humans [4–6]. The generality and action orientation of Active Inference makes it a natural bridge between descriptive approaches to cognition (e.g., biology) and prescriptive approaches to implementation of artificial intelligence (e.g., machine learning) and design (e.g., user experience, communication). Active Inference therefore enables a principled account of composition and decomposition, construction and de-construction, in complex adaptive systems. This generality provides a unified conceptual and pragmatic approach towards establishing a foundation for modeling, designing, and implementing various systems across scales, disciplines, and settings. 
While Active Inference was developed as a theoretical and descriptive analytical framework for application in biological systems, it is showing early promise in guiding the integration and management of heterogeneous information systems (viewed as intelligent agents) across a variety of domains. The transdisciplinary nature and flexibility of Active Inference makes the framework ideal for practical, theoretical, and interoperable work across myriad use-cases, including (i) cognitive neuroscience and philosophy [1,2,7–27] (ii) artificial intelligence (AI) and AI explainability [2,4,9,28–34] (iii) robotics [35,36] (iv) human health and clinical psychiatry [37–49], (v) developmental psychology [5,35,46,50–54] (vi) social sciences and economics [6,52,55–61], (vii) mathematical physics [59,62–70], (viii) physics of life [15,69–75] (ix) consciousness studies and phenomenology [41,48,76–81] (x) evolution, ecology, and development [3,42,69,82,83] (xi) cyber and cognitive security [84], (xii) mapping and modeling of information ecosystems [6,85–87], (xiii) ontology modeling and maintenance [85,88], (xiv) rhetorical analysis [89], (xv) logistics and business intelligence [90,91], (xvi) theoretical and applied biology and ecology [3,69,92,93], (xvii) project management and team science [94–96], (xvii) collective behavior [42,97,98], (xix) trust, aesthetics, and wellbeing [99,100], (xx) military science [101,102], and (xxi) climate science [103,104]. 
Further development and formalization of Active Inference research has the potential to facilitate various socially valuable outcomes and directly address many domain-specific “research to practice” gaps [96,105,106]. As such, Active Inference already exists both as a physics-based scientific methodology, and as an nascent Open Source Ecosystem that is forming an interoperability layer for an emerging network of people, tools, methodologies, and practices. 
The Active Inference Institute
As of August 2023, The Active Inference Institute is a registered non-profit organization, tasked with identifying, establishing, and managing the sustainable implementation of: 
	(i) administrative and governance functions to give components of the Active Inference Ecosystem coherent forms and reliable channels of communications, 
	(ii) publishing, and licensing protocols that establish open and fair use and effective dissemination of community products within and beyond the Ecosystem, 
	(iii) services at the scale of individual humans and the community at large so that stability is protected while risk and uncertainty are minimized within the Ecosystem, and 
	(iv) organization and operation of cyber and cognitive security systems that ensure productivity, inclusivity, accessibility, and safety in discourse and collaboration,
Figure 1 shows the structure of the Institute and engagements with the Ecosystem.

Figure 1. Active Inference Institute & the Active Inference Ecosystem.
To date, The Institute has hosted or facilitated the development of hundreds of open-source licensed products which serve various functions in the Ecosystem including Awareness, Education, Commons, Support, and Governance (Figure 2, see Appendix for details on livestreams, courses, research papers, games, tools, etc.). 
Despite its minimal budget with volunteer-only staff, The Institute’s level of community engagement and productive outputs compare favorably with some well-resourced research think tanks and centers of excellence. At the same time, the rapid growth of the Active Inference community, brings attention towards building pathways to sustainability for both The Institute as an organization and the open source Ecosystem as a whole.

Figure 2. Open Source Products of The Institute (left side) support various Functions in the Active Inference Ecosystem (right side). 
Our Vision
The Active Inference Institute (“The Institute” from here on) serves as a scaffold for stabilizing and connecting myriad fields around a central tradition and approach called “Active Inference.” The Institute aims to make the Active Inference framework and the Ecosystem we serve more accessible, applicable, rigorous, and integrated. We facilitate theoretical and applied engagement with Active Inference, promoting awareness of the field within the lay, academic, public-sector, and professional communities. We envision a future in which the term “Active Inference” is used as widely as “Machine Learning”, as a result of its demonstrated utility and impact in a variety of domains.
Our Values and Principles
We are committed to fostering a culture of excellence, collaboration, and innovation. Our values and principles serve as the guiding principles that shape our work and define our organization's character. 
Active Inference and Exploration. At The Institute, we embrace the principle of Active Inference and exploration as a fundamental driving force. We actively cultivate a culture of curiosity and continuous learning. Through engaging in diverse research endeavors and actively exploring our environment, we enrich our understanding and drive impactful collaborative research.
Integrity & Inclusivity. We strive to uphold and promote honesty, accountability, professionalism, as well as responsible conduct in research, education, and facilitation among members of The Institute, Ecosystem, and communities we serve. We foster diversity, respect, and inclusion through community engagement. We treat differences in perspective and understanding as a wellspring of valuable creative and productive potential, driving breakthroughs and strengthening collaborative research outcomes.
Dynamic Internal Modeling: At The Institute, we utilize a cutting-edge modeling-based approach to support shared informational niches for different scales, spanning the Ecosystem, Institute, Organizational Units, and Projects. We continuously develop and refine hierarchical models, drawing on sensory information, exploiting data, and gathering feedback. Our dynamic self-modeling enables efficient resource allocation.
Anticipatory Behavior: The Institute's commitment to anticipatory behavior equips us to excel in uncertain environments. Leveraging our internal models, we generate predictions at various scales and time horizons, empowering us to take initiative and adapt our policies accordingly. This forward-thinking approach enables us to plan strategically and make informed decisions, thus remaining at the forefront of our fields.
Continuous Development: Embodying the ideas of open-endedness and techno-evolution, we wholeheartedly embrace the principle of continuous development at The Institute. Recognizing the dynamic nature of our environment and the constant advancements in science and technology, we continually evolve our internal models and approaches. This perpetual learning and evolution enable us to remain adaptive and at the cutting edge of our fields, driving impactful research that contributes significantly to the scientific community.
Priorities and Challenge Areas
We address the following challenge areas at the Active Inference Institute, enabling the Ecosystem to make even broader impacts:
Education: Scientific Literacy and Workforce Development. Active Inference relies on mathematical formalisms and is loaded with abstract conceptual challenges that transcend disciplinary boundaries. By modeling educational processes such as pedagogy, competency evaluation, and professionalization in the Active Inference framework, The Institute catalyzes workforce development, seeks to stabilize the “research to practice” gap, and contributes to the broader project of participation in scientific ecosystems.
Research: Grounding the Cognitive Sciences in Physics. Research across the natural sciences suffers from a lack of theoretical integration and practical collaborations. The Active Inference framework provides a unifying first-principles account of vital features of biological systems, transcending disciplinary boundaries. At The Institute we promote this theoretical integration through various educational programs, supporting learners of all backgrounds.
Information Science and Diverse Intelligences. Modern information environments are faster and more complex than ever. At The Institute we apply Active Inference to understanding, monitoring, evaluating, refining, and developing artificial and synthetic (e.g., human-machine interface, organizational, crowd) intelligence systems. This work is enacted by projects currently related to information science, ontology, data quality control, artificial intelligence explainability, and knowledge engineering. 
User Experience, Accessibility, and Sociotechnical Design. It remains an open challenge how to enable sustainable engagement in digital systems. At The Institute we map cognitive frameworks to design, user experience, ergonomics, and requirements engineering, to offer new methods and tools to a wider community of professionals and scholars. 
Cyber and Cognitive Security. Individuals and organizations today are confronted with a rapidly-evolving landscape of threats to digital and cognitive security. At The Institute we work to unify cognitive frameworks with existing cyber security and emerging cognitive security concepts and frameworks, to understand, measure, and address local and global information technology risks and impacts more effectively at multiple scales. 
Scaling the Active Inference Ecosystem. The nascency of the Active Inference Ecosystem enables us to take a proactive approach towards various areas of consideration. At The Institute we create synergy among the efforts applied to the above challenge areas, and emerging needs of the Active Inference Ecosystem. This approach creates an opportunity to learn by doing and to embrace convergence research, where implementations are developed in parallel with theory, supported by regular information sharing and collaboration among practitioners and researchers.
Applying Active Inference. Bringing the insights from empirical and theoretical Active Inference research into practice by designing new projects or communicating with existing projects that design and implement social system infrastructure, such as health infrastructure and cultural technologies that support human wellbeing [49]. Supporting projects in the Ecosystem that design and implement solutions to various problems we face, such as climate change or overall polycrisis [85,107–110].
The Way Ahead
To deliver on these challenge areas and to ensure the continued facilitation of the Active Inference Ecosystem in coming years, The Institute will pursue the following initiatives:
Administrative and Financial Support. Finding and allocating the necessary seed resources to establish dedicated administrative support for The Institute and the necessary infrastructure (e.g., accounting, legal, digital affordances, materials), to request and receive donor and sponsor support, and to offer and dispense micro-grants and financial support to researchers and collaborators. 
Publishing and Licensing Support. Developing publishing affordances and publishing facilitation systems to assist contributors in identifying and applying correct licensing, reducing time-to-impact for research and educational artifacts, and enhancing access to knowledge of other Ecosystem participants. 
Facilitation, Research, and Project Support. Providing both direct and tool-based support and coordination to emergent professional and research teams to extend their impact and reduce uncertainty in interorganizational collaboration; for example, by providing access to common digital storage and workspace, research and modeling tools, common information sharing and licensing models, and grant and project management systems.
Human Resources Development. Instantiating the necessary human resources and learning management systems to support The Institute’s volunteers and staff in fostering productivity, inclusivity, connectivity, and safety in discourse and collaboration. 
Community Engagement. Creating and, where applicable, automating feedback mechanisms for ensuring that the community remains productively engaged. Delivering quality content updates, moderating community discourse to ensure compliance with our culture and values, and responding to community feedback.
Community User Experience, Ergonomics, and Design Systems. Connecting Active Inference to the user experience, ergonomics, and design communities to both better identify and understand relevant best practices and to apply these within the Ecosystem and The Institute. Establishing design patterns for consistent communications, feedback mechanisms, and semiotics, and improving the onboarding and working experience for new and existing users of Active Inference and derivative tools, methodologies, and materials.
Communications and Public Relations Planning. Collaborating with communications professionals and establishing a communications plan and necessary supporting tools to allow for the regular, professional, and tailored communications necessary for a community of this size and diversity, with an eye toward supporting rapid growth of new partners and users, and responding to and integrating community feedback.


History of The Institute
The Active Inference Institute’s origin lies in a co-founder team meeting around a common interest: the Active Inference framework. This resulted in productive collaboration and the publication “Active Inference & Behavior Engineering for Teams” in September 2020 [94]. Following the publication, discussions turned towards exploring approaches that could catalyze the accessibility, rigor, and applicability of Active Inference, and how to merge the developing framework with Systems Engineering and Open Science. Out of these discussions an “Active Inference Lab” (or ActInfLab) was formed and began operations in 2021. Over the coming months, dozens of individuals from around the world would come to engage with ActInfLab through various projects such as educational livestreams, open source publishing, collaborative research projects, focused learning groups, and early-stage development of the Active Inference Ontology. From the first quarter of operations, the ActInfLab hosted Quarterly Roundtable livestreams for communicating quarterly expectations and results to the community [111], a tradition that The Institute continues to this day. 
Beginning in 2022, a cohort-based Scientific Advisory Board (SAB) was established to connect the ActInfLab to cutting-edge theoretical work as well as various domain-specific applications. As interest in both the ActInfLab’s activities and Active Inference itself began to grow, ActInfLab soon emerged as a key facilitating organization in what was then a primarily academic community working on the underlying theory and potential implications for Active Inference. In 2022, ActInfLab made the developmental leap to become the Active Inference Institute, a non-profit formed in Delaware, USA (as of writing, we are seeking recognition as a 501c3 tax-exempt organization by the US Internal Revenue Service), with the intention of making its facilitatory role in the community sustainable, and scalable. 
Active Inference, over this time, has been attracting increased attention as a quantitative and cognitive framework capable of acting as a common bridge, or Rosetta Stone, among various domains, and is rapidly gathering support across fields (Figure 3), which is reflected in The Institute’s increasingly diverse membership (Figure 4) and a literature review we conducted at the end of 2022 [112]. The transdisciplinary nature and flexibility of Active Inference make it an ideal candidate for practical, theoretical, and interoperable integration across myriad disciplines, sectors, and use-cases. The application of Active Inference framings across these various domains promises to foster new research frontiers and socially-impactful solutions in a variety of interdisciplinary settings. 

Figure 3. Proportion of citations per 100,000 on NCBI PubMed for “Active Inference” (blue line) from 2006 till July 31, 2023. In the last complete year (2022), there were 103 citations for “Active Inference” of 1,772,674 publications total. 


Figure 4. Keyword scrape from affiliations within The Institute’s roster of people who have appeared or been invited to join for a livestream. Only 29.15% of the list had affiliations to scrape, and this list does not cover most participants in textbook groups and courses, thus it represents a preliminary and partial sample that underestimates the diversity of interests and backgrounds.
Possibilities
Along with other modern technical fields, Active Inference faces and addresses challenges of broad relevance such as (i) remote education, workforce development, and competency evaluation, (ii) user experience, ergonomics, and accessibility in a modern global context, (iii) open source ecosystem, utility, reliability, and safety, (iv) participation in research and practice-oriented activities (v) cyber- and cognitive-security, (vi) theoretical and practical aspects of artificial intelligence explainability and safety, (vii) social and economic policy integration and management. 
Integrations featuring Active Inference are increasingly being found across public and private sectors. In such settings, usage of the framework supports information and technique sharing, contributes to common tools and artifacts, and enables documentation of best practices, protocols, and procedures. These applications are enabled through common education around Active Inference themes, concepts, skills, practices, and tools.
As such, there is potential for The Institute to facilitate both the study (theory and research) and professionalization (practice and implementation) of Active Inference within and across myriad sectors and disciplines, and to grow the incipient Active Inference Ecosystem and awareness of Active Inference by facing such challenges proactively and in a fashion aligned with our vision, values, and principles..
The core reason why Active Inference is being adopted so rapidly is that it provides a neutral, action-oriented ontology which describes a great array of complex adaptive systems, up to and including human social cognition [85,88]. The Active Inference framework can be used to describe systems at different nested scales. The applicability of Active Inference to multi-scale complex adaptive systems is a source of great explanatory power, and it is also a challenge for the framework’s coherence. Scholars from different disciplines or fields may read Active Inference concepts or constructs differently, and unknowingly build an error into their research ecology which is then propagated forward, thereby hampering progress in the field at large. To our knowledge, the Active Inference Institute is the first scaled attempt at directly tackling that risk by offering Active Inference education to learners of all backgrounds, and by working to specify an ontology that is both particular to Active Inference and broadly accessible. 

Challenges
Rapid growth comes with new challenges and greater requirements for sustainability. The following challenges were identified as among the most important to address for the Active Inference Institute in order to support further flourishing of the Active Inference Ecosystem:
Onboarding and Adoption. Learning and applying Active Inference, and onboarding into the Ecosystem, can be challenging for a variety of reasons. Active Inference involves abstract concepts, mathematical formalisms, and specific terminology, making it challenging for newcomers to actively engage with the framework. Given Active Inference’s transdisciplinary nature, learning resources must be tailored to sit at the edges of Active Inference and a variety of other fields (such as community-produced immersive learning experiences [113]).
Usability of Community Tools and Resources. In addition to conceptual challenges faced when onboarding into Active Inference, there is a learning process to become familiar with community tools and ways of working (such as knowledge or project management software [94,96]), potentially causing user experience frictions in practical aspects of community onboarding. The Institute offers resources and support features to facilitate usability of community tools and resources (see Appendix), and plans to improve on such services in the future. The Institute will establish user-experience auditing and common design patterns to ensure a satisfactory, calm, and reliable user experience, as well as the smooth delivery of bug reports and feedback.
Sustainability and Scalability of Support Functions. Support functions that would add value to The Institute and the Ecosystem at large include publishing and licensing support, grant and project management tools, and learning management systems. Making support functions available and scalable is a priority.
Communications. The Institute currently manages communications across multiple platforms and channels with a variety of audiences and potential stakeholders in a semi-automated fashion according to our internal and external communication plans (see below). Scaling and fully automating our communication efforts will require financial and human support.
Administrative and Financial Support. In order to address many of the challenges described here, The Institute will need dedicated administrative support and standardization of protocols and procedures related to record keeping, management of partnerships, human resources, financial compliance, and other operational aspects.

Next Steps
With these challenges in mind, The Institute seeks financial and operational support to scale our impact in the coming years and pursue sustainability. In this document, we (i) formalize our organizational model (see Section titled “Institute Organization Model”), (ii) provide a community development and communications plan with consideration for measurement and evaluation (see Section titled “Community Growth and Development Model”), and, (iii) put forth the following initiatives to address the challenge areas here, with an eye toward receiving support to sustain ongoing activities (Appendix) and deploy new programs in the coming years.
Administrative and Financial Support. We will develop a sustainable funding strategy that involves a combination of grants, donations, sponsorships, and partnerships to support The Institute. We will look to various grant programs to acquire the necessary resources to jumpstart systemization of many administrative and support functions. We will establish the infrastructure (e.g., accounting, legal, compliance, security) to request, receive, and provide financial support.
Publishing and Licensing Support. Decisions regarding licensing, publishing venue can be complex, and can greatly delay time-to-impact of some work products, and prevent others from ever coming to fruition. We will continue to develop publishing affordances and publishing facilitation systems to assist contributors in applying open-source licensing, thus leveraging the visibility of their work and reducing time-to-impact for research and educational artifacts.
Facilitation, Research, and Project Support. Interorganizational and interdisciplinary collaboration is rewarding but potentially hazardous due to differences in ontology and working norms. We will systemize facilitation tools (e.g., project management tools, grant facilitation tools), to reduce conflict and uncertainty in emergent professional and research teams. Further, we intend to streamline other support functions, such as accessibility to common digital storage and workspaces, and research modeling tools.
Human Resources and Community Development. In a community of this size, there is a need for dedicated human resources and community management roles, as well as systemization of educational offerings for ease of access. We will prioritize instantiating the necessary human resources, community, and learning management systems to support The Institute’s volunteers and staff in fostering productivity, inclusivity, integrity, and safety in discourse and collaboration.
Community User Experience, Ergonomics, and Design Systems. We will leverage the expertise of user experience and ergonomics experts to audit and improve the user experience within the Active Inference community. Design patterns for consistent user experience and feedback will be prioritized, with an emphasis on improving the onboarding and working experience for users of Active Inference and foundational tools, methodologies, and materials.
Communications and Public Relations Planning. In order to sustain the community, The Institute needs to interface with a variety of communities and stakeholders. In addition to establishing administrative functions for the maintenance and development of partnerships and funding support, we also plan to work with communications professionals to refine and streamline our existing communications plan (see Communications Plan below). This will allow us to scale our regular, professional, and tailored communications as the size and diversity of the Active Inference Ecosystem increase. 
Institute Organization Model
Institute Governance and Leadership
Members
The legal founding members of The Institute are Alexander Vyatkin, Virginia Knight, Ivan Metelkin, Daniel Friedman, and Karl Friston.
Board of Directors
The inaugural cohort of the Board of Directors has been in operation since the end of 2022 [114]. The Board of Directors is composed of individuals with expertise in Active Inference, governance, fundraising, and various other domains. They meet quarterly and are responsible for setting the organization's strategic goals, providing oversight, and ensuring compliance. The current Board of Directors in 2023 is: Rafael Kaufmann, John Clippinger, Daniel Friedman, Dean Tickles, Bleu Knight, and Mike Smith.
Scientific Advisory Board
The Scientific Advisory Board comprises external experts in Active Inference and related research areas who provide guidance, review grant proposals, and offer advice on scientific integrity [115]. The first Scientific Advisory Board was active during 2022, and currently we are engaged with the second cohort in 2023: Bradly Alicea, John Boik, Matt Brown, Scott David, Shady El Damaty, Jeff Emmett, Chris Fields, Karl Friston, Holly Grimm, Sarah Hamburg, Victor Kariuki, Anatoly Levenchuk, Maxwell J. D. Ramstead, Adeel Razi, and Michael Zargham.
Officers
The first set of Officers was installed at the end of 2022 with the following positions: 
Daniel Friedman (President and Treasurer)
As President, responsible for overall leadership, direction, and activities of the organization. As Treasurer, responsible for managing the financial activities of The Institute. 
Alexander Vyatkin (Vice President)
Supports the objective of the President and assumes these responsibilities when necessary. Focused on defining and implementing effective ways of working for The Institute/Units/Project scales, integrating state of the art methods, practices, and technologies into operations. In charge of organizational design, ensuring continuous evolvement of services and organizational functions. 
Bleu Knight (Secretary)
Oversees logistical and operational projects. Supervises organizational processes such as official meetings and votes. Oversees efforts geared toward financial and HR compliance.
Institute Units (Support, Projects, and Programs)
Administrative Unit
The Institute Administrative Unit will be established upon receiving the necessary funding to support operations. Members of the Administrative Unit will be paid subcontractors and employed staff, assisting with and performing administrative and support tasks within The Institute and the wider Ecosystem, such as recordkeeping, graphic design, data input, formatting, copywriting, grant proposal submission, preparation and compliance, and other various administrative and support activities. They will also contribute to the development of core infrastructure to provide such support and automate or systematize and standardize tasks, and become the organizational umbrella for financial, human resources, internship, volunteer, security, community moderation and management, and related activities and organizational components. These tasks are currently assumed by The Institute’s officers, who will continue to provide oversight as the unit develops formally.
EduActive Unit
The Institute’s Education Unit facilitates (i) textbook groups, (ii) course development, (iii) production, editing, and review of educational materials, and (iv) review, feedback, and integration of external educational materials. 
See Table A1 for a description of projects in the Education Unit.
Example Outputs:
    • Video Live Streams
    • Active Inference Journal
    • Courses and Educational Groups
    • Events
    • Standards and Qualifications
    • Educational Games
Ongoing Initiatives:
    • Educational Materials and Documentation. Developing and disseminating educational materials, methodology and tool documentation and tutorials, contributing to competency, capability, and common language within the community.
    • Courses. Developing educational courses and course management software to streamline hosting, development, and requests for content from the community.
    • Livestreams and Events. Releasing Livestreams regularly. Planning and coordinating symposia and other events for education and continuing professional development.
    • Active Inference Ontology. Integrating Active Inference with formal ontologies (such as the axiom-driven Suggested Upper Merged Ontology [60]). Among the affordances to be expected from deeply axiomatizing Active Inference within a global formal ontology are detecting and correcting gaps, identifying development opportunities for domain-specific engagements, and facilitating use in translation and educational work across human and computer languages
    • Qualification system. Developing an Active Inference qualification system that centers and standardizes referenceable levels of skills and knowledge in order to help individuals adapt and thrive in various professional and personal contexts. A scientific foundation will ensure that the system is based on the latest research and insights, enabling it to maintain effectiveness and relevance. Such systems might also be integrated (and normatively cross referenced) with existing professional and credentialing systems (e.g. in psychology, academia, law, medicine, engineering). 
ReInference unit
The Institute’s ReInference unit facilitates (i) the forming of fit-for-function interdisciplinary research teams, (ii) the development and execution of research proposals and projects aligned with the mission of The Institute and challenges faced by The Institute and Ecosystem at large. The ReInference unit is committed to hosting and sharing all relevant data, findings, publications, tools, and derivative artifacts under open-source or similarly accessible licensing agreements wherever practicable and appropriate. 
See Table A2 for a description of projects in the ReInference unit.
Example Outputs:
    • Research Papers
    • Literature Review and Meta-Analysis
    • Software and Tools
    • Distributed Facilitation
    • Standards Development and Contribution
Ongoing Initiatives:
    • Computational and Storage Resources. Streamlining access to computational resources and tools for research and educational purposes.
    • Project Facilitation Tools & Support. Pending funding, providing both direct and tool-based project management and facilitation support to emergent professional and research teams to extend their impact.
    • Volunteers and Internship programs. Providing multiple and diverse opportunities to individuals willing to commit to role-based contribution, tailored to their circumstances where possible, to offer opportunities for hands-on learning and experience.
    • Publishing & Licensing Support. Continuing to develop publishing affordances (such as the Active Inference Journal) and publishing facilitation systems to assist contributors in identifying and applying correct licensing, reducing time-to-impact on research and educational artifacts, and getting access to more knowledgeable others.
    • Scaffold domain- and system-specific connections through liaisons. Facilitating interdomain liaison relationships. For example at the intersection of Active Inference with Robotics, the ongoing work by JF Cloutier [116] at The Institute applies the principles of Active Inference to implement unsupervised, symbolic machine learning in autonomous robots. 
    • Explore new forms of peer review. Providing tools and protocols for distributed collective sensemaking that can be applied towards situated scientific practices, by incorporating them in novel publishing, evaluation and curation workflows [85,117]. The Active Inference Journal can serve as a test-bench for initial prototyping efforts, improving its function of archiving, indexing, translating, curating, and disseminating, and implementing a peer review system for certain kinds of publications. 
    • Applications to sensemaking. Expanding and extending ontology and sensemaking frameworks. The Active Entity Ontology for Science (AEOS) [85] can be extended to cover sensemaking more broadly, by specifying active and informational entities and the relevant interactions between them. The Suggested Upper Merged Ontology (SUMO) [118] [62] seems to offer the best combination of broad coverage and theoretical rigor as an open-source upper-level ontology framework.
    • Cognitive modeling of organizations. Supporting organizational modeling. The Active Inference ontology can then serve as a scaffold for building multi-agent simulations of collective sensemaking in cadCAD and Active Blockference [119], as well as the basis for specification of protocols to guide the development of digital sensemaking tools and networks [120]. Hybrid societal organizations, whether academic, corporate, or other, can leverage these simulations to anticipate potential disruptions or challenges in their communication networks. 
Volunteer Program
As a community-driven open science organization, there are multiple opportunities for contribution. All backgrounds, time zones, time availability, and levels of familiarity with Active Inference are welcome and encouraged. Volunteers are active learners who want to contribute to ongoing projects at The Institute. Volunteers have the opportunity to engage in and lead a wide array of projects without any constraints on their type or quantity. These projects encompass a range of activities such as study groups, livestreams, marketing initiatives, publications, symposiums, and applied research. 
Internship Program
The Active Inference Institute Internship Program is a 1-6 month program (tailored to individual circumstances), in which accepted applicants participate in Learning Groups, Projects, and other functions within The Institute, developing team and project skills and familiarity with Active Inference. Interns receive a 1:1 mentor who catalyzes their work through a shared document and periodic check-ins. Upon successful completion, Interns receive acknowledgement and certification and, where appropriate, letters of recommendation for their next endeavors.

Community Growth and Development
Here, we present the community growth and development model (Figure 2), built on the following 5 core components:
    i. Awareness. Promoting and fostering awareness and use of Active Inference, and developing partnerships with well-aligned organizations and communities.
    ii. Education. Developing and disseminating educational materials, contributing to competency, capability, and common language within the community.
    iii. Common Forum. Offering and maintaining an inclusive and accessible common forum for discussing, sharing, and hosting relevant work and opportunities, finding collaborators, and networking (i.e., an informational commons).
    iv. Support. Providing support for emergent teams and projects which align with The Institute’s mission, in the interest of innovation and impact
    v. Governance. Maintaining stable governance for cultivating and sustaining partnerships, technical infrastructure, and sponsors.
Ecosystem Structure
The Institute cultivates an active and engaged ecosystem around the scientific modeling framework of Active Inference. This vibrant Ecosystem and community drives innovation on the research front and makes significant strides in providing accessible education. The Institute ensures that efforts are well-aligned, impact-focused, relevant, and meaningful in advancing research and education for the betterment of society by forming partnerships and by engaging with and growing the Active Inference community. Our community development model emphasizes facilitation over management, and distributed as opposed to command-and-control strategies. More importantly, our model moves beyond the provision of networking and discussion space to support emergent, collaborative work. 
As opposed to a linear “funnel” growth model, The Institute will implement a cyclical model of organic growth pursued through the incubation among participants of (i) self-efficacy, or a sense of personal capability, (ii) a sense of support and safety, and (iii) a sense of investment and impact in participants, as a basis for forming a sense of community and providing the foundation for development of relationships within the community through positive, repeated contact [121]. The support of these senses leads to productive, emergent collaboration, which in turn leads to emergent community narrative, norms, roles, and “scripts” [94,122]. Participants are reinforced in their feelings of capability as a part of a team, assured that they will be provided with support in a reasonably safe environment, and that results will have a lasting, positive impact on their community. Resulting research and educational artifacts and documentation constitute shareable content which can then be used to bring awareness about Active Inference and The Institute to non-community members. 
Where a “funnel growth” model focuses on awareness alone as a basis for developing a user-base, our model’s focus on education, knowledge sharing and presentation of work, and support for teams allows for non-community members of all backgrounds and interests to engage with and contribute to the community, thus affirming membership through a sense of shared investment, impact, and competency. Further, where online learning communities anticipate members terminating participation following completion of coursework (or after achieving feelings of self-efficacy in the material), our model’s provision of support and opportunities for sharing of work with professionals and academics provides incentives for continued engagement and participation to those who feel they have already become reasonably familiar with all available educational material.
Below, background is provided on the (i) structure of the community (i.e., user segmentation), (ii) our information storage and dissemination technology (“tech”) stack, (iii) our communications plan, (iv) the education, support, and infrastructure and governance functions we provide and/or intend to provide as a part of this model, and (v) our intended approach toward evaluating quality control and growth.
Community Structure
Participants (Members and Learners)
Participants include members of the Active Inference Ecosystem, or those who engage with and contribute to The Institute and its facilitated artifacts, activities, and communications. Potential participants include students, educators, researchers, and professionals who may benefit either from awareness of Active Inference and its implications, developing related competencies and having opportunities to network and collaborate with individuals who do, or from opportunities to collaborate and share work and insights which would be valuable to the Active Inference Ecosystem. 
Users (Adopters and Beneficiaries)
The Institute’s productive outputs include software, tools, and methodologies, including the facilitation of Active Inference itself as an open source product. As such, the community using Active Inference and related open source products requires documentation, clear messaging regarding updates, and guidelines on fair and best practices. By considering such beneficiaries of Active Inference as “users,” The Institute may leverage existing best practices from other domains, such as user experience, requirements engineering, and software engineering. Potential users include professionals, researchers, educators, and engineers.
Research Partners (External Research Organizations and Working Groups)
The Institute’s ReInference unit collaborates with external research partners, universities, institutions, and subject matter experts. These partnerships involve joint research projects, data sharing, and knowledge exchange to enhance the depth and breadth of research efforts. Collaborations with research partners create an opportunity to enrich The Institute's research capabilities and resource access, thereby accelerating the generation of new knowledge and helping us to address complex research questions, validate findings, and extend the reach of our research impact. Potential research partners include organizations working on or faced with problems that may be solved by Active Inference, and organizations which are working on or have solutions to problems which The Institute and the community are facing. 
Educational Partners (Universities and Educators)
The Institute’s EduActive Unit collaborates with educational partners to influence, instantiate, share, and get access to educational programs, teacher training, and learning resources. By partnering with educational institutions, The Institute extends its educational reach and impact and fosters effective delivery and dissemination of its educational content. Potential educational partners include universities, tutors, educational institutions, and educators.
Funders (Donors, Supporters, and Funding Agencies)
The Institute requires financial support in order to keep pace with community needs, maintain information infrastructure, and assist researchers in finding their own financial support for relevant research initiatives. Potential donors and funders include generous community members and beneficiaries, government funding agencies, private philanthropic donors, and sponsors of events, programs, and initiatives.
Information Management and Tech Stack
The Institute hosts and disseminates information using Coda, YouTube, Discord, and Google Suites. This stack of platforms streamlines specific levels of access to shared resources, and enhances overall productivity within the organization. We aim to ensure that participants are aware of the platforms being used and understand their purposes and functionalities. We regularly evaluate, communicate, and reinforce best practices for information storage, access, and organization. We implement security measures, such as strong passwords, 2-factor authentication, and appropriate access permission in order to protect sensitive information. We back up important data regularly to prevent loss due to technical issues or accidental deletion. We conduct periodic reviews and audits of the information storage systems to identify areas for improvement and optimization. The specific use of each platform is described below.
Coda (Modeling, Project, and Knowledge Management Platform)
Coda is the primary platform for knowledge and project management at The Institute, Ecosystem, community, and individual scale. It organizes all information and content related to each project (or sub-project). Coda is version-controlled and access-restricted, ensuring that all of our data is protected against accidental deletion and inappropriate user access. We use Coda for storing and organizing important documents, such as policies, procedures, project plans, and meeting notes. We follow best practices for Coda, including: (1) creating dedicated Coda “documents”, or work areas, for different departments or projects to ensure easy access and organization of relevant information, (2) implementing a clear folder and file structure within Coda to maintain document organization and version control, (3) archiving unnecessary and irrelevant pages, files, and folders, and (4) granting appropriate access permissions to users, allowing them to view, edit, or comment on documents as required. If The Institute receives the necessary resources, Coda will be upgraded to an Enterprise License and consultants will assist in development of templates and low-code applications for streamlining support, records and knowledge management, and project management functions. Further, an Enterprise License will allow for a variety of new mechanisms for user-access control and permissioning, and for tracking of work activity and community engagement with hosted content.
YouTube (Live Streaming and Video Hosting)
YouTube is the primary platform for storing audiovisual content created for and by The Institute. Our designated YouTube Channel holds distinct playlists for courses, live streams, symposia, and other content that we host. We share and embed links within internal and external communication channels to provide easy access to relevant content. The content on YouTube is also backed up in a personal cloud storage service as well as in offline hard drives. 
Discord (Forum and Instant Messaging)
Discord is our primary platform for engaging with the Active Inference Ecosystem and broader community. We use Discord for real-time communication, informal discussions, and team collaboration. Dedicated channels are used within Discord to categorize discussions based on topics or projects. Participants are encouraged to share relevant files, documents, or links within Discord channels, fostering easy access to shared resources. We regularly monitor and moderate Discord channels to maintain professionalism, and eagerly look to improve our protocols and guidelines here and elsewhere. 
Google Workspace (Document Management, Document Production, and Email)
Google Workspace is composed of email, cloud storage, calendar, and collaborative artifact editing tools for presentation slide-decks, documents, spreadsheets, and diagrams, among other related web-based applications. These tools are tightly integrated, allowing for seamless collaboration, file sharing, and real-time editing among participants, making them ideal for distributed teams and organizations with remote workers. Google Workspace automatically saves document versions, making it easy to track changes and revert to previous versions if needed. This version control feature ensures that all participants have access to the latest document updates and can track changes over time. Google's robust security infrastructure includes two-factor authentication, data loss prevention, and enterprise-grade security features. 
Twitter (now “X”) (Public Announcements and Releases)
Twitter (recently rebranded as “X”), serves as the primary tool for public announcements and releases, and for directing attention of the wider public to events within the Ecosystem and community.
Communications Plan
Our communications plan is broken into three segments, (i) Internal Communications, (ii) External Communications, and (iii) Organizational Communications. 
Internal Communications Plan
Institute staff, volunteers, interns, officers, and board members communicate with one another and with members of the community as follows:
    • Email serves as the primary means of communication for internal announcements, updates, sharing important documents, and any other professional communications where record keeping is of interest. 
    • Regular Synchronous Officer Meetings are held to keep communication lines open, address questions, and discuss progress on projects. The Scientific Advisory Board meets optionally, twice a month, in an open discussion format. The Board of Directors meets quarterly to respond to the quarterly roundtable update and address any other issues or concerns.
    • Shared Calendars are used to schedule meetings, appointments, and events, ensuring everyone is aware of each other's availability.
    • The Institute-operated Discord Server is the primary location for asynchronous discussion and synchronous project meetings. Currently there are around 900 people in the server, and we strive to keep it an accessible entry point for learning and applying Active Inference. 
External Communications Plan
The Institute communicates with Active Inference Ecosystem and public as follows:
Target Audiences
    • Professionals and Academics: Individuals with an interest in cognitive science, machine learning, philosophy, physics, linguistics, computer science, and related areas.
    • Potential Partners: Government agencies, funding organizations, academic institutions, and other research-focused organizations.
    • Active Inference Community: Researchers, academics and professionals who use and reference Active Inference and related approaches in their daily work. 
    • Broader Scientific Community: Researchers, academics, and professionals in compatible fields.
Approach
    • Livestreams (between one and several public streams per week).
    • Content Announcements
Twitter, Discord, and Email
        ◦ Completed projects and recent publications.
        ◦ Collaboration and other project opportunities.
        ◦ New releases of educational materials and tools.
    • Scheduled Updates and Announcements
Twitter, Discord, and Email
        ◦ Weekly Announcements of Livestreams, educational activities, and overall projects and participation information.
        ◦ Monthly Communications providing updates on results of the last month’s with information for different scales of AII.
        ◦ Quarterly Summaries of roundtable discussions regarding quarterly results, and expectations and preferences for next quarter. 
Organizational Communication
The Institute communicates with potential partners, sponsors, and relevant constituencies as follows:
Target Audiences
    • General Public: Individuals who may have a personal interest in cognitive science, machine learning, philosophy, physics, linguistics, computer science, and related areas.
    • Research and Educational: Universities and academic institutions.
    • Trade Associations and Think Tanks. Organizations which perform research about future industry trends, in addition to other communities of practice.
    • Corporate: Companies with employees who would benefit from knowing Active Inference related approaches to business organization and operations. 
    • Government: Government agencies and funding vehicles.
    • Private Donors: Individuals who understand the value and potential impact of this community of practice and its subject matter, and would be willing to help support it.
Approach
The goal of our organizational communications plan is to provide the foundation for sustainable and accessible funding, and to work toward making Active Inference a household term, used as widely as “Machine Learning”, reflecting its demonstrable utility and impact in implementation.
Pending support, The Institute plans to engage with public relations and communications experts to work toward these goals. The path toward both objectives begins with making "Active Inference" a commonly known and used term within Government, Corporate, Research, and Educational organizations. As such, an ideal next step toward this goal is the professionalization of Active Inference core competencies and techniques and related competency and qualification standards. 
Ecosystem Support, Infrastructure, and Administration
The Institute contributes to participants' (i) self-efficacy, (ii) safety, and (iii) impact, through the aims of our broader vision and strategy. Beyond the Education and Research work described above, the Institute plays Ecosystem support roles such as: 
Informational Commons
Common Forum. Hosting online forums, discussion groups, and social communications channels where learners, researchers, and practitioners can connect, ask questions, and share insights. Fostering a community that helps individuals overcome challenges, exchange ideas, and receive support from peers and experts. 
Opportunities to Share and Present Work. Provide myriad opportunities to share and present relevant interdisciplinary work on Active Inference, offering enhanced opportunities for unique collaborations and new knowledge discovery catalyzed by Active Inference and the consequent amplified leveraging of expertise and practices across disciplines, domains, and paradigms.
Infrastructure and Administration
Partnerships. Managing and growing relationships with potential educational and research partners. 
Sponsor and Donor Funding. Managing relationships with potential donors and sponsors, and, pending funding, developing the necessary infrastructure (e.g., accounting, legal, digital affordances, materials) to request and receive donor and sponsor support, and to offer and dispense micro-grants and financial support to researchers.
Funding Discovery & Acquisition Support. Providing a variety of support mechanisms for participants to search for and submit to grant and funding opportunities, as well as assist them in forming partnerships (e.g., with other researchers, companies, and universities). 
Infrastructure. Maintaining and developing information systems to support The Institute’s activities, iteratively improving usability and efficacy. Pending funding, working with requirements engineering and user experience professionals to overhaul existing systems.
Professionalization. Developing a curriculum of training programs for Officers and Directors of commercial entities and officials of governmental and civil society organizations to enhance their understanding of sentient behavior (as described by Active Inference) and its implications for organizational interactions in the areas of Business, Operations, Legal, Technical, and Social [102]. 
Quality, Performance, and Growth Evaluation
The Institute intends to evaluate quality, performance, and growth within community development at three scales, listed below, based on best practices within the open source community [123,124] and adapted for our low-code and no-code use-cases. See the section titled “Next Steps” for more information on expectations of future expansion and refinement of evaluation methodology.
Participant scale
Evaluation at the level of individuals, with consideration for a plurality of individual priors (i.e., diversity in perspective, experience, culture, language, preferences, discipline, and level of expertise) and a focus on accessibility and onboarding. Objectives include quality of participant and user experience, plurality of educational mediums and formats (i.e., accessibility), networking and collaboration opportunities, and professional development. Pending grant or donor funding, The Institute will work with user experience, communications, and requirements engineering professionals to improve current and establish new feedback mechanisms and implement best practices for aforementioned evaluations. The following tools serve as a basis for evaluation:
    • Individual feedback forms and surveys
    • Participation (e.g., number of projects completed and contributed to)
    • Continuing Professional Development (e.g., courses completed, certifications) 
Institute scale 
Evaluation at the level of The Institute will consider various areas such as sustainability of personal and collective efforts, support reliability, and user experience quality, and Institute quality control and improvement. Objectives include increasing collaboration opportunities, ensuring consistency and rapid handling of inconsistency in documentation, and supporting and facilitating projects. Specific metrics of quality, performance, and growth at The Institute scale may include: 
    • Number of participants and commits in open source projects
    • Number of responses to our Volunteer and Internship forms
    • Number of newsletter signups
    • Statistics on projects facilitated by The Institute (e.g., total completed, ongoing, and dissolved)
    • Offered and completed Internships
    • Frequency of discovery and resolution of inconsistencies in research, documentation, tools.
    • Frequency of discovery and resolution of gaps in implementation (i.e., frequently questioned answers and frequently asked questions)
    • Number of facilitators, stewards, and volunteers and related turnover and activity
    • Aggregation of individual feedback forms and surveys
Ecosystem scale 
Evaluation at the level of the Ecosystem and community scale with consideration for impact and relationship management, and a focus on impact. Objectives include minimizing turnover rate in educational courses, increasing the number of participants, and maintaining and adding partnerships. Metrics of quality, performance, and growth at the community scale may include: 
    • Frequency and number of edits and engagements with Coda pages (pending funding, see sections titled “Information Management and Tech Stack” and “Next Steps”)
    • Number of participants in Discord General Channel
    • Number of participants contributing to facilitated projects
    • Turnover rate in engagement and participation (e.g., direct participant engagement with Institute releases and material, and annual involvement in collaborative activities)
    • Number of individuals enrolled in educational courses
    • Turnover and completion rate in educational courses
    • Turnover rate in partnerships (e.g., research and education partnership decisions to renew, maintain, or dissolve)
    • Social media analytics (e.g., views, watch time, audience diversity)

Discussion and Future Directions
The Active Inference Institute attracts and amplifies the self-organizing abilities of people, thereby potentiating a unique opportunity and a powerful and scalable platform from which to accomplish research and development goals. As members of the Ecosystem, we continue to evolve an understanding and “voice” clarifying who we are, and who we might become, as a collective. In the process of building both an organizational reputation and individual expectations, we are constantly reminded of and inspired by the fact that the object of our research and development work, Active Inference, itself anticipates analysis and integration well beyond systems that are “closed” in time or space (i.e. those constrained to evolve linearly with a beginning, middle, and end as structure). We are interested in modeling, designing, and working with “open” systems, and have sought to cultivate an Ecosystem and larger community that reflects the intrinsic openness and systemic “curiosity” of Active Inference. With additional resources to support the work described in this application, the benefits of these open systems and guidance on future interaction practices consistent with Active Inference can be readily made available across myriad domains.
The Institute’s work and community building efforts have always exemplified the benefits of “open” systems, consistent with the insights gleaned from Active Inference research itself. For example, when tracking open system behavior associated with the development and evolution of Active Inference, The Institute might have chosen to place an emphasis on “closing” (i.e. erecting constraints, applying limits, setting conditions, etc.) to simplify the challenge of modeling the space. However, rather than take a closed system (laboratory-centric) approach alone, which might have relegated Active Inference to an isolated academic disciplinary silo, we recognized the benefits that accrue from an “open” approach that invites self-organizers in the broader Active Inference Ecosystem to migrate (the “active” in Active Inference) into programs and participation that best suits their needs and prior experiences. Members of the Ecosystem will continue to encourage and support the opportunities to embrace variation-retained field studies for Active Inference…everywhere. 
In the Ecosystem, we recognize that people and entities are explorers, capable of self-organization, motivated and eager to discover, and change agents of Active Inference approaches in the truest sense. By applying and leveraging the collective expertise of our community in preparation, scouting, and wayfinding practices, The Institute aims to continue helping Ecosystem participants to move ideas off-the-bench and into complex real world situations where the interaction environment acts as the ultimate scrutinizer. The resilience, sustainability and responsiveness of biological systems described through Active Inference research suggests that the human and social systems benefits of applied Active Inference framings will enhance the positive impact on the organization and operation of humans, including but not limited to The Institute itself. 
To the people already involved in the Active Inference community, the “Ecosystem” isn’t just a hypothetical and aspirational future state. Instead, it is the actual current world of interactions among members of the Active Inference community that we inhabit at all times. Active Inference, The Institute and members of the Ecosystem are all focused on dynamically adapting the efficiencies of change management practices as we prepare, scout, and “way find” our way into the future with measurable degrees of understanding around confidences, probabilities and the underlying mechanics involved, rather than depending on static plans that are quickly rendered obsolete in times of rapid change. As The Institute and Ecosystem help build competence and confidence in more agents in forms of organization and operation that reflect and apply Active Inference concepts, we will grow the pool of potential first finds (discoveries and inventions) and high-reliability knowledge systems in our world. Cultivating those skills as part of who we are as individuals and in organizations, and sharing those skills with others who are eager to see the future, and to be the future, is more than just an attractor state to guide our actions. It is the core mission of The Institute, Ecosystem, and its participants. 
Act. Infer. Serve.

Appendix
Open source services of The Institute for the Ecosystem
This section reviews the work that The Institute has hosted or carried out between the beginning of 2021 and August 2023.
Educational services
Table A1 gives a summary of the educational work carried out from 2021 through the present. 
Educational Service
Information
Video Livestreams
More than 370 livestreams from 2020 through 2023 (presentations, discussions, workshops, textbook groups) on a wide variety of topics related to Active Inference.
Active Inference Journal
We publish curated transcriptions for livestreams, and make video captions/translations.
Textbook groups
Two completed cohorts of Active Inference Textbook groups, and two ongoing cohorts.
Courses
Chris Fields "Physics as Information Processing"
“Active Inference in the Social Sciences”
Textbook alpha testing
Working with Sanjeev Namjoshi during 2023 to support development of a textbook (expected public release in 2024).
Ontology for Education
Collect and define key terms in Active Inference in a formal ontology, with translations in more than 10 languages
Table A1. Educational offerings at The Institute.
Research services
Table A2 gives a summary of the research work carried out from 2021 through the present. 
Research Service
Information
Active Inference Ontology Development
Core, Supplemental, and Entailed terms, examples/counterexamples, connections, translations.
Software
Active Blockference consists of Active Inference generative models implemented in the complex systems modeling framework cadCAD.
Notation interoperability systems
Generalized Notation Notation works to provide a notational system that generalizes across settings of Active Inference modeling.
Research papers
Some relevant supported publications are listed here.
Literature meta-analysis and presentation
Knight et al. 2022 performed ontology-guided automatic and manual literature analysis on several hundred Active Inference paper, presenting the results as interactive public frontend
Table A2. Research offerings at The Institute.
Standards activities 
In 2023 The Institute proposed the first-ever qualification standard for Active Inference expertise. We continue to develop these standards for use in educational, research, and professional settings. 
Facilitation activities
Table A3 gives a summary of the mentorship, facilitation, and service activities carried out from 2021 until now. 
Service Activity
Information
Volunteer program
Volunteers contribute to Institute projects and engage in learning groups.
Internship program
The Internship program supports motivated individuals who are looking to make large contributions and make rapid gains in understanding.
Distributed facilitation
We engage the Ecosystem and support individuals to contribute their facilitation skills in the context of projects, courses, and learning groups.
Applied Active Inference Symposia
1st in 2021 with Karl Friston, 2nd in 2022 on Robotics, 3rd in 2023 on “Enacting Ecosystems of Shared Intelligence.”
Table A3. Facilitation activities at The Institute.
Governance activities
Table A4 gives a summary of the governance activities carried out from 2021 through the present. Future Institute and Ecosystem-scale governance programs are planned. 
Governance Activity
Information
Scientific Advisory Board
The Scientific Advisory Board is an informal body that provides The Institute with guidance.
Board of Directors
Board of Directors is the formal governance body of The Institute, currently in its first annual cohort of 6 people.
 Table A4. Governance activities at The Institute.


Works Cited
1. 	Friston K, FitzGerald T, Rigoli F, Schwartenbeck P, Pezzulo G. Active Inference: A Process Theory. Neural Comput. 2017;29: 1–49. doi:10.1162/NECO_a_00912
2. 	Parr T, Pezzulo G, Friston KJ. Active Inference: The Free Energy Principle in Mind, Brain, and Behavior. MIT Press; 2022. Available: https://mitpress.mit.edu/books/active-inference
3. 	Friston K, Friedman DA, Constant A, Knight VB, Fields C, Parr T, et al. A Variational Synthesis of Evolutionary and Developmental Dynamics. Entropy. 2023;25: 964. doi:10.3390/e25070964
4. 	Sajid N, Ball PJ, Parr T, Friston KJ. Active Inference: Demystified and Compared. Neural Comput. 2019. pp. 674–712. doi:10.1162/neco_a_01357
5. 	Constant A, Ramstead MJD, Veissière SPL, Friston K. Regimes of Expectations: An Active Inference Model of Social Conformity and Human Decision Making. Front Psychol. 2019;10: 679. doi:10.3389/fpsyg.2019.00679
6. 	Albarracin M, Demekas D, Ramstead MJD, Heins C. Epistemic Communities under Active Inference. Entropy. 2022;24. doi:10.3390/e24040476
7. 	Hipólito I, Ramstead MJD, Convertino L, Bhat A, Friston K, Parr T. Markov blankets in the brain. Neurosci Biobehav Rev. 2021;125: 88–97. doi:10.1016/j.neubiorev.2021.02.003
8. 	de Vries B, Friston KJ. A Factor Graph Description of Deep Temporal Active Inference. Front Comput Neurosci. 2017;11: 95. doi:10.3389/fncom.2017.00095
9. 	Friston KJ, Daunizeau J, Kiebel SJ. Reinforcement learning or active inference? PLoS One. 2009;4: e6421. doi:10.1371/journal.pone.0006421
10. 	Friston KJ, Fagerholm ED, Zarghami TS, Parr T, Hipólito I, Magrou L, et al. Parcels and particles: Markov blankets in the brain. Netw Neurosci. 2021;5: 211–251. doi:10.1162/netn_a_00175
11. 	Clark A. Whatever next? Predictive brains, situated agents, and the future of cognitive science. Behav Brain Sci. 2013;36: 181–204. doi:10.1017/S0140525X12000477
12. 	Badcock PB, Friston KJ, Ramstead MJD. The hierarchically mechanistic mind: A free-energy formulation of the human psyche. Phys Life Rev. 2019;31: 104–121. doi:10.1016/j.plrev.2018.10.002
13. 	Bruineberg J, Rietveld E. Self-organization, free energy minimization, and optimal grip on a field of affordances. Front Hum Neurosci. 2014;8: 599. doi:10.3389/fnhum.2014.00599
14. 	Bruineberg J, Froese T. Surfing uncertainty: prediction, action and the embodied mind. International Journal of Performance Arts and Digital Media. 2016;12: 215–217. doi:10.1080/14794713.2016.1257478
15. 	Yufik YM, Friston K. Life and Understanding: The Origins of “Understanding” in Self-Organizing Nervous Systems. Front Syst Neurosci. 2016;10. doi:10.3389/fnsys.2016.00098
16. 	Sengupta B, Friston K. Approximate Bayesian inference as a gauge theory. arXiv [q-bio.NC]. 2017. Available: http://arxiv.org/abs/1705.06614
17. 	Sengupta B, Tozzi A, Cooray GK, Douglas PK, Friston KJ. Towards a neuronal gauge theory. PLoS Biol. 2016;14: e1002400. doi:10.1371/journal.pbio.1002400
18. 	Ramstead MJ, Kirchhoff MD, Friston KJ. A tale of two densities: active inference is enactive inference. Adapt Behav. 2020;28: 225–239. doi:10.1007/s11229-016-1239-1
19. 	Ramstead MJD, Friston KJ, Hipólito I. Is the Free-Energy Principle a Formal Theory of Semantics? From Variational Density Dynamics to Neural and Phenotypic Representations. Entropy. 2020;22. doi:10.3390/e22080889
20. 	Safron A, Klimaj V, Hipólito I. On the Importance of Being Flexible: Dynamic Brain Networks and Their Potential Functional Significances. Front Syst Neurosci. 2021;15: 688424. doi:10.3389/fnsys.2021.688424
21. 	Hipólito I, Baltieri M, Friston K, Ramstead MJD. Embodied skillful performance: where the action is. Synthese. 2021;199: 4457–4481. doi:10.1007/s11229-020-02986-5
22. 	Hipólito I. Cognition Without Neural Representation: Dynamics of a Complex System. Front Psychol. 2021;12: 643276. doi:10.3389/fpsyg.2021.643276
23. 	Nave K, Deane G, Miller M, Clark A. Wilding the predictive brain. Wiley Interdiscip Rev Cogn Sci. 2020;11: e1542. doi:10.1002/wcs.1542
24. 	Seth AK, Critchley HD. Extending predictive processing to the body: emotion as interoceptive inference. The Behavioral and brain sciences. 2013. pp. 227–228. doi:10.1017/S0140525X12002270
25. 	Seth AK. Interoceptive inference, emotion, and the embodied self. Trends Cogn Sci. 2013;17: 565–573. doi:10.1016/j.tics.2013.09.007
26. 	Ramstead MJD, Kirchhoff MD, Constant A, Friston KJ. Multiscale integration: beyond internalism and externalism. Synthese. 2021;198: 41–70. doi:10.1007/s11229-019-02115-x
27. 	Constant A, Clark A, Friston KJ. Representation Wars: Enacting an Armistice Through Active Inference. Front Psychol. 2020;11: 598733. doi:10.3389/fpsyg.2020.598733
28. 	Friston KJ, Lin M, Frith CD, Pezzulo G, Hobson JA, Ondobaka S. Active Inference, Curiosity and Insight. Neural Comput. 2017;29: 2633–2683. doi:10.1162/neco_a_00999
29. 	Smith R, Schwartenbeck P, Parr T, Friston KJ. An Active Inference Approach to Modeling Structure Learning: Concept Learning as an Example Case. Front. Comput. Neurosci. 2020. p. 633677. doi:10.3389/fncom.2020.00041
30. 	Da Costa L, Parr T, Sajid N, Veselic S, Neacsu V, Friston K. Active inference on discrete state-spaces: A synthesis. J Math Psychol. 2020;99: 102447. doi:10.1016/j.jmp.2020.102447
31. 	Kinghorn P, Collis P, Buckley C. Understanding Tool Discovery and Tool Innovation Using Active Inference. 4th International Workshop on Active Inference. 2023. Available: https://openreview.net/forum?id=BKzmTzoQIr
32. 	Pezzulo G, Parr T, Cisek P, Clark A, Friston K. Generating meaning: Active inference and the scope and limits of passive AI. [cited 29 Jul 2023]. Available: https://psyarxiv.com/8xgzv/download?format=pdf
33. 	Albarracin M, Hipólito I, Tremblay SE, Fox JG, René G, Friston K, et al. Designing explainable artificial intelligence with active inference: A framework for transparent introspection and decision-making. arXiv [cs.AI]. 2023. Available: http://arxiv.org/abs/2306.04025
34. 	Paul A, Sajid N, Da Costa L, Razi A. On efficient computation in active inference. arXiv [cs.LG]. 2023. Available: http://arxiv.org/abs/2307.00504
35. 	Hipólito I, Winkle K, Lie M. Enactive artificial intelligence: subverting gender norms in human-robot interaction. Front Neurorobot. 2023;17: 1149303. doi:10.3389/fnbot.2023.1149303
36. 	Da Costa L, Lanillos P, Sajid N, Friston K, Khan S. How active inference could help revolutionise robotics. Entropy. 2022;24: 361. doi:10.3390/e24030361
37. 	Adams RA, Stephan KE, Brown HR, Frith CD, Friston KJ. The computational anatomy of psychosis. Front Psychiatry. 2013;4: 47. doi:10.3389/fpsyt.2013.00047
38. 	Schwartenbeck P, Friston K. Computational Phenotyping in Psychiatry: A Worked Example. eNeuro. 2016;3. doi:10.1523/ENEURO.0049-16.2016
39. 	Cullen M, Davey B, Friston KJ, Moran RJ. Active Inference in OpenAI Gym: A Paradigm for Computational Investigations Into Psychiatric Illness. Biol Psychiatry Cogn Neurosci Neuroimaging. 2018;3: 809–818. doi:10.1016/j.bpsc.2018.06.010
40. 	Smith R, Badcock P, Friston KJ. Recent advances in the application of predictive coding and active inference models within clinical neuroscience. Psychiatry Clin Neurosci. 2020. doi:10.1111/pcn.13138
41. 	Friston K. Computational psychiatry: from synapses to sentience. Mol Psychiatry. 2022. doi:10.1038/s41380-022-01743-z
42. 	Pio-Lopez L, Kuchling F, Tung A, Pezzulo G, Levin M. Active inference, morphogenesis, and computational psychiatry. Front Comput Neurosci. 2022;16: 988977. doi:10.3389/fncom.2022.988977
43. 	Badcock PB, Davey CG, Whittle S, Allen NB, Friston KJ. The Depressed Brain: An Evolutionary Systems Theory. Trends Cogn Sci. 2017;21: 182–194. doi:10.1016/j.tics.2017.01.005
44. 	McParlin Z, Cerritelli F, Rossettini G, Friston KJ, Esteves JE. Therapeutic Alliance as Active Inference: The Role of Therapeutic Touch and Biobehavioural Synchrony in Musculoskeletal Care. Front Behav Neurosci. 2022;16: 897247. doi:10.3389/fnbeh.2022.897247
45. 	Ciaunica A, Seth A, Limanowski J, Hesp C, Friston KJ. I overthink—Therefore I am not: An active inference account of altered sense of self and agency in depersonalisation disorder. Conscious Cogn. 2022;101: 103320. doi:10.1016/j.concog.2022.103320
46. 	Ciaunica A, Roepstorff A, Fotopoulou AK, Petreca B. Whatever Next and Close to My Self—The Transparent Senses and the “Second Skin”: Implications for the Case of Depersonalization. Front Psychol. 2021;12. doi:10.3389/fpsyg.2021.613587
47. 	Dumas G, Gozé T, Micoulaud-Franchi J-A. “Social physiology” for psychiatric semiology: How TTOM can initiate an interactive turn for computational psychiatry? The Behavioral and brain sciences. Cambridge University Press (CUP); 2020. p. e102. doi:10.1017/S0140525X19002735
48. 	Ramstead MJD, Wiese W, Miller M, Friston KJ. Deep neurophenomenology: An active inference account of some features of conscious experience and of their disturbance in major depressive disorder. 2020. Available: http://philsci-archive.pitt.edu/18377
49. 	Miller M, Kiverstein J, Rietveld E. The Predictive Dynamics of Happiness and Well-Being. Emot Rev. 2022;14: 15–30. doi:10.1177/17540739211063851
50. 	Hipólito I, van Es T. Enactive-Dynamic Social Cognition and Active Inference. Front Psychol. 2022;13. doi:10.3389/fpsyg.2022.855074
51. 	Gallagher S, Allen M. Active inference, enactivism and the hermeneutics of social cognition. Synthese. 2018;195: 2627–2648. doi:10.1007/s11229-016-1269-8
52. 	Veissière SPL, Constant A, Ramstead MJD, Friston KJ, Kirmayer LJ. Thinking through other minds: A variational approach to cognition and culture. Behav Brain Sci. 2019;43: e90. doi:10.1017/S0140525X19001213
53. 	Ramstead MJD, Veissière SPL, Kirmayer LJ. Cultural Affordances: Scaffolding Local Worlds Through Shared Intentionality and Regimes of Attention. Front Psychol. 2016;7: 1090. doi:10.3389/fpsyg.2016.01090
54. 	Ciaunica A, Constant A, Preissl H, Fotopoulou K. The first prior: From co-embodiment to co-homeostasis in early life. Conscious Cogn. 2021;91: 103117. doi:10.1016/j.concog.2021.103117
55. 	Manrique HM, Walker MJ. To copy or not to copy? That is the question! From chimpanzees to the foundation of human technological culture. Phys Life Rev. 2023;45: 6–24. doi:10.1016/j.plrev.2023.02.005
56. 	Guénin--Carlut A. Cognitive agency in sociocultural evolution. 2022. doi:10.31219/osf.io/x7yr4
57. 	Guénin--Carlut A. Thinking like a State - Embodied intelligence in the deep history of our collective minds. 2021. doi:10.31219/osf.io/dxnzt
58. 	Albarracin M, Poirier P. Enacting Gender: An Enactive-Ecological Account of Gender and Its Fluidity. Front Psychol. 2022;13: 772287. doi:10.3389/fpsyg.2022.772287
59. 	Albarracin M, Constant A, Friston KJ, Ramstead MJD. A Variational Approach to Scripts. Front Psychol. 2021;12: 585493. doi:10.3389/fpsyg.2021.585493
60. 	Hipólito I, Hesp C. On religious practices as multi-scale active inference. Wittgenstein and the Cognitive Science of Religion: Interpreting Human Nature and the Mind. 2023; 179. Available: https://www.torrossa.com/gs/resourceProxy?an=5494029&publisher=FZ0661#page=192
61. 	Vasil J, Badcock PB, Constant A, Friston K, Ramstead MJD. A World Unto Itself: Human Communication as Active Inference. Front Psychol. 2020;11: 417. doi:10.3389/fpsyg.2020.00417
62. 	Ramstead MJD, Sakthivadivel DAR, Heins C, Koudahl M, Millidge B, Da Costa L, et al. On Bayesian mechanics: a physics of and by beliefs. Interface Focus. 2023;13: 20220029. doi:10.1098/rsfs.2022.0029
63. 	Sakthivadivel DAR. A Worked Example of the Bayesian Mechanics of Classical Objects. arXiv [physics.class-ph]. 2022. Available: http://arxiv.org/abs/2206.12996
64. 	Fields C, Friston K, Glazebrook JF, Levin M. A free energy principle for generic quantum systems. arXiv [quant-ph]. 2021. Available: http://arxiv.org/abs/2112.15242
65. 	Ramstead MJD, Sakthivadivel DAR, Friston KJ. On the Map-Territory Fallacy Fallacy. arXiv [physics.hist-ph]. 2022. Available: http://arxiv.org/abs/2208.06924
66. 	Da Costa L, Friston K, Heins C, Pavliotis GA. Bayesian mechanics for stationary processes. Proc Math Phys Eng Sci. 2021;477: 20210518. doi:10.1098/rspa.2021.0518
67. 	Parr T, Da Costa L, Friston K. Markov blankets, information geometry and stochastic thermodynamics. Philos Trans A Math Phys Eng Sci. 2020;378: 20190159. doi:10.1098/rsta.2019.0159
68. 	Friston K. A free energy principle for a particular physics. arXiv [q-bio.NC]. 2019. Available: http://arxiv.org/abs/1906.10184
69. 	Ramstead MJD, Constant A, Badcock PB, Friston KJ. Variational ecology and the physics of sentient systems. Phys Life Rev. 2019. doi:10.1016/j.plrev.2018.12.002
70. 	Ramstead MJD, Badcock PB, Friston KJ. Answering Schrödinger’s question: A free-energy formulation. Phys Life Rev. 2018;24: 1–16. doi:10.1016/j.plrev.2017.09.001
71. 	Kirchhoff M, Parr T, Palacios E, Friston K, Kiverstein J. The Markov blankets of life: autonomy, active inference and the free energy principle. J R Soc Interface. 2018;15: 20170792. doi:10.1098/rsif.2017.0792
72. 	Palacios ER, Razi A, Parr T, Kirchhoff M, Friston K. Biological Self-organisation and Markov blankets. bioRxiv. 2017. p. 227181. doi:10.1101/227181
73. 	Kirchhoff MD, Froese T. Where There is Life There is Mind: In Support of a Strong Life-Mind Continuity Thesis. Entropy. 2017;19: 169. doi:10.3390/e19040169
74. 	Palacios ER, Razi A, Parr T, Kirchhoff M, Friston K. On Markov blankets and hierarchical self-organisation. J Theor Biol. 2020;486: 110089. doi:10.1016/j.jtbi.2019.110089
75. 	Friston K. Life as we know it. J R Soc Interface. 2013;10: 20130475. doi:10.1098/rsif.2013.0475
76. 	Ramstead MJD, Seth AK, Hesp C, Sandved-Smith L, Mago J, Lifshitz M, et al. From Generative Models to Generative Passages: A Computational Approach to (Neuro) Phenomenology. Rev Philos Psychol. 2022;13: 829–857. doi:10.1007/s13164-021-00604-y
77. 	Ramstead MJD, Albarracin M, Kiefer A, Williford K, Safron A, Fields C, et al. Steps towards a minimal unifying model of consciousness: An integration of models of consciousness based on the free energy principle. [cited 29 Jul 2023]. Available: https://files.osf.io/v1/resources/6eqxh/providers/osfstorage/64a7222ccdab33002ede4bbb?action=download&direct&version=1
78. 	Ramstead MJD, Albarracin M, Kiefer A, Klein B, Fields C, Friston K, et al. The inner screen model of consciousness: applying the free energy principle directly to the study of conscious experience. arXiv [q-bio.NC]. 2023. Available: http://arxiv.org/abs/2305.02205
79. 	Friston KJ, Wiese W, Hobson JA. Sentience and the Origins of Consciousness: From Cartesian Duality to Markovian Monism. Entropy. 2020;22. doi:10.3390/e22050516
80. 	Friston K, Lutz A, Ramstead MJD. Towards a computational phenomenology of mental action: modelling meta-awareness and attentional control with deep parametric active inference. of consciousness. 2021. Available: https://academic.oup.com/nc/article-abstract/2021/1/niab018/6358635
81. 	Safron A. An integrated World Modeling Theory (IWMT) of consciousness: Combining integrated information and global neuronal workspace theories with the Free Energy Principle and Active Inference Framework; Toward solving the hard problem and characterizing agentic causation. Front Artif Intell. 2020;3: 30. doi:10.3389/frai.2020.00030
82. 	Constant A, Ramstead MJD, Veissière SPL, Campbell JO, Friston KJ. A variational approach to niche construction. J R Soc Interface. 2018;15. doi:10.1098/rsif.2017.0685
83. 	Ramstead MJD, Hesp C, Tschantz A, Smith R, Constant A, Friston K. Neural and phenotypic representation under the free-energy principle. Neurosci Biobehav Rev. 2021;120: 109–122. doi:10.1016/j.neubiorev.2020.11.024
84. 	David S, Cordes RJ, Friedman DA, editors. Structuring the Information Commons: Open Standards and Cognitive Security. Cognitive Security Education & Research Forum (COGSEC); 2022. Available: https://www.cogsec.org/cat-22
85. 	Friedman D, Applegate-Swanson S, Choudhury A, Cordes RJ, El Damaty S, Guénin—Carlut A, et al. An Active Inference Ontology for Decentralized Science: from Situated Sensemaking to the Epistemic Commons. 2022. doi:10.5281/zenodo.6320575
86. 	Groz R, Oriat C, Vega G, Simao A, Foster M, Walkinshaw N. Active Inference of Extended Finite State Models of Software Systems. In: Coste F, Ouardi F, Rabusseau G, editors. Proceedings of 16th edition of the International Conference on Grammatical Inference. PMLR; 10--13 Jul 2023. pp. 265–269. Available: https://proceedings.mlr.press/v217/groz23a.html
87. 	Murray-Smith R, Stein S, Williamson JH. Active Inference in Human--Computer Interaction. 4th International Workshop on Active Inference. 2023. Available: https://openreview.net/forum?id=BuhUs1yGu1
88. 	Active Inference Institute. Active Inference Ontology. 2022 [cited 12 Dec 2022]. doi:10.5281/zenodo.7972289
89. 	Mascarenhas M, Cordes RJ, Knight B, Murphy S, Friedman DA. Tracking Public Sensemaking through Rhetorical Annotation of Image Memes. 2022. doi:10.5281/zenodo.6904427
90. 	Fox S. Active Inference: Applicability to Different Types of Social Organization Explained through Reference to Industrial Engineering and Quality Management. Entropy. 2021;23: 198. doi:10.3390/e23020198
91. 	Khezri B. Governing Continuous Transformation: Re-framing the Strategy-Governance Conversation. Springer International Publishing; 2022. doi:10.1007/978-3-030-95473-4
92. 	Fields C, Levin M. Scale-Free Biology: Integrating Evolutionary and Developmental Thinking. Bioessays. 2020;42: e1900228. doi:10.1002/bies.201900228
93. 	Friedman D, Tschantz A, Ramstead MJD, Friston K, Constant A. Active inferants: The basis for an active inference framework for ant colony behavior. Front Behav Neurosci. 2021;15: 126. doi:10.3389/fnbeh.2021.647732
94. 	Vyatkin A, Metelkin I, Mikhailova A, Cordes RJ, Friedman DA. Active Inference & Behavior Engineering for Teams. 2020. doi:10.5281/zenodo.4021163
95. 	Tison R, Poirier P. Communication as Socially Extended Active Inference: An Ecological Approach to Communicative Behavior. Ecol Psychol. 2021;33: 197–235. doi:10.1080/10407413.2021.1965480
96. 	Fox S. Accessing Active Inference Theory through Its Implicit and Deliberative Practice in Human Organizations. Entropy. 2021;23: 1521. doi:10.3390/e23111521
97. 	Kaufmann R, Gupta P, Taylor J. An Active Inference Model of Collective Intelligence. Entropy. 2021;23. doi:10.3390/e23070830
98. 	Heins C, Klein B, Demekas D, Aguilera M, Buckley CL. Spin Glass Systems as Collective Active Inference. Active Inference. Springer Nature Switzerland; 2023. pp. 75–98. doi:10.1007/978-3-031-28719-0_6
99. 	Mikhailova A, Friedman DA. Partner Pen Play in Parallel (PPPiP): A New PPPiParadigm for Relationship Improvement. Arts Health. 2018;7: 39. doi:10.3390/arts7030039
100. 	Miller M, Albarracin M, Pitliya RJ, Kiefer A, Mago J, Gorman C, et al. Resilience and active inference. Front Psychol. 2022;13: 1059117. doi:10.3389/fpsyg.2022.1059117
101. 	Cordes RJ, Friedman DA. The Facilitator’s Catechism. 2020. doi:10.5281/zenodo.4062541
102. 	David S, Cordes RJ, Friedman DA. Active Inference in Modeling Conflict. 2021. doi:10.5281/zenodo.5750935
103. 	Rubin S, Parr T, Da Costa L, Friston K. Future climates: Markov blankets and active inference in the biosphere. J R Soc Interface. 2020;17: 20200503. doi:10.1098/rsif.2020.0503
104. 	Rubin S, Da Costa L, Friston K. Earth system resilience through planetary active inference. 2021. pp. EGU21–15347. doi:10.5194/egusphere-egu21-15347
105. 	Mallonee S, Fowler C, Istre GR. Bridging the gap between research and practice: a continuing challenge. Inj Prev. 2006;12: 357–359. doi:10.1136/ip.2006.014159
106. 	Munro CL, Savel RH. Narrowing the 17-Year Research to Practice Gap. Am J Crit Care. 2016;25: 194–196. doi:10.4037/ajcc2016449
107. 	Boik JC. Science-Driven Societal Transformation, Part I: Worldview. Sustain Sci Pract Policy. 2020;12: 6881. doi:10.3390/su12176881
108. 	Boik JC. Science-Driven Societal Transformation, Part II: Motivation and Strategy. Sustain Sci Pract Policy. 2020;12: 8047. doi:10.3390/su12198047
109. 	Friston KJ, Ramstead MJD, Kiefer AB, Tschantz A, Buckley CL, Albarracin M, et al. Designing Ecosystems of Intelligence from First Principles. arXiv [cs.AI]. 2022. Available: http://arxiv.org/abs/2212.01354
110. 	Kaufmann R. The Gaia Attractor. A planetary AI copilot network to overcome the Metacrisis. In: Medium [Internet]. 17 Apr 2023 [cited 11 Aug 2023]. Available: https://rkauf.medium.com/the-gaia-attractor-41e5af33f3b7
111. 	Active Inference Institute. Active Inference Institute ~ Livestreams. 30 Nov 2021 [cited 24 Jul 2023]. Available: https://coda.io/@active-inference-institute/livestreams
112. 	Knight VB, Cordes RJ, Friedman D. The Free Energy Principle & Active Inference: a Systematic Literature Analysis. 2022. doi:10.5281/zenodo.7449368
113. 	The Adventure of Curiosity. [cited 6 Aug 2023]. Available: https://oncyber.io/the_adventure_of_curiosity
114. 	Active Inference Institute. Board of Directors. [cited 24 Jul 2023]. Available: https://www.activeinference.org/about/board-of-directors
115. 	Active Inference Institute. Scientific Advisory Board. [cited 24 Jul 2023]. Available: https://www.activeinference.org/about/scientific-advisory-board
116. 	Cloutier J-F. Towards a symbolic implementation of Active Inference for Lego robots. 2022. doi:10.5281/zenodo.6862626
117. 	Tamari R, Friedman D. Open Access science needs Open Science Sensemaking (OSSm): open infrastructure for sharing scientific sensemaking data. https://osf.io › preprints › metaarxivhttps://osf.io › preprints › metaarxivhttps://osf.io › preprints › metaarxiv › downloadhttps://osf.io › preprints › metaarxiv › download. 2023. doi:10.31222/osf.io/9nb3u
118. 	Niles I, Pease A. Towards a standard upper ontology. Proceedings of the international conference on Formal Ontology in Information Systems - Volume 2001. New York, NY, USA: Association for Computing Machinery; 2001. pp. 2–9. doi:10.1145/505168.505170
119. 	Smékal J, Choudhury A, Singh AK, Damaty SE, Friedman DA. Active Blockference: cadCAD with Active Inference for Cognitive Systems Modeling. Active Inference. Springer Nature Switzerland; 2023. pp. 143–150. doi:10.1007/978-3-031-28719-0_10
120. 	Tamari R, Friedman D, Fischer W, Hebert L, Shahaf D. From Users to (Sense)Makers: On the Pivotal Role of Stigmergic Social Annotation in the Quest for Collective Sensemaking. Proceedings of the 33rd ACM Conference on Hypertext and Social Media. New York, NY, USA: Association for Computing Machinery; 2022. pp. 236–239. doi:10.1145/3511095.3536361
121. 	McMillan DW, Chavis DM. Sense of community: A definition and theory. J Community Psychol. 1986;14: 6–23. doi:10.1002/1520-6629(198601)14:1<6::aid-jcop2290140103>3.0.co;2-i
122. 	Albarracin M, Constant A, Friston K, Ramstead M. A variational approach to scripts. 2020. Available: https://psyarxiv.com/67zy4/download
123. 	Open Source Security Foundation. Concise Guide for Evaluating Open Source Software. 2023. Available: https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Concise-Guide-for-Evaluating-Open-Source-Software.md
124. 	Aniszczyk C, Abernathy C, Beda J, Yehuda G, Novotny S. Measuring Your Open Source Program’s Success. Linux Foundation; Available: https://www.linuxfoundation.org/resources/open-source-guides/measuring-your-open-source-program-success


