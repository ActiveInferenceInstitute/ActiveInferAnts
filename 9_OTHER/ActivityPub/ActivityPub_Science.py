import requests
import json
from typing import Dict, List, Optional, Union
from datetime import datetime
from Helpful_ActivityPub import ActivityPubHelper

class DecentralizedScienceSystem:
    def __init__(self, base_url: str, access_token: str):
        self.ap_helper = ActivityPubHelper(base_url, access_token)

    def create_researcher(self, username: str, display_name: str, bio: str, fields: Optional[List[str]] = None) -> Dict:
        """Create a new researcher actor in the ActivityPub network."""
        researcher_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Person",
            "id": f"{self.ap_helper.base_url}/users/{username}",
            "preferredUsername": username,
            "name": display_name,
            "summary": bio,
            "tag": [{"type": "Hashtag", "name": f"#{field}"} for field in (fields or [])],
            "publicKey": {
                "id": f"{self.ap_helper.base_url}/users/{username}#main-key",
                "owner": f"{self.ap_helper.base_url}/users/{username}",
                "publicKeyPem": "..."  # Generate and add actual public key
            },
            "inbox": f"{self.ap_helper.base_url}/users/{username}/inbox",
            "outbox": f"{self.ap_helper.base_url}/users/{username}/outbox",
            "followers": f"{self.ap_helper.base_url}/users/{username}/followers",
            "following": f"{self.ap_helper.base_url}/users/{username}/following",
            "sci:researchInterest": fields,
            "sci:affiliation": None  # To be filled by the researcher
        }
        return self.ap_helper.create_actor(username, display_name, bio, additional_data=researcher_data)

    def publish_paper(self, researcher_id: str, title: str, abstract: str, content: str, keywords: List[str], 
                      doi: Optional[str] = None, references: Optional[List[str]] = None) -> Dict:
        """Publish a scientific paper as an Article in the ActivityPub network."""
        paper_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Create",
            "actor": researcher_id,
            "object": {
                "type": "Article",
                "attributedTo": researcher_id,
                "name": title,
                "summary": abstract,
                "content": content,
                "tag": [{"type": "Hashtag", "name": f"#{keyword}"} for keyword in keywords],
                "sci:doi": doi,
                "sci:citation": references or [],
                "published": datetime.utcnow().isoformat() + "Z",
                "url": f"{self.ap_helper.base_url}/papers/{doi.replace('/', '-') if doi else ''}",
                "cc": ["https://www.w3.org/ns/activitystreams#Public"],
                "sci:peerReviewed": False,
                "sci:license": "https://creativecommons.org/licenses/by/4.0/"
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(paper_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def peer_review(self, reviewer_id: str, paper_id: str, review_content: str, rating: Optional[int] = None) -> Dict:
        """Submit a peer review for a paper."""
        review_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Create",
            "actor": reviewer_id,
            "object": {
                "type": "Review",
                "inReplyTo": paper_id,
                "content": review_content,
                "tag": [{"type": "Hashtag", "name": "#PeerReview"}],
                "sci:reviewRating": {
                    "type": "Rating",
                    "ratingValue": rating,
                    "bestRating": 5,
                    "worstRating": 1
                } if rating is not None else None,
                "published": datetime.utcnow().isoformat() + "Z",
                "url": f"{self.ap_helper.base_url}/reviews/{paper_id.split('/')[-1]}-{reviewer_id.split('/')[-1]}"
            },
            "to": [paper_id, "https://www.w3.org/ns/activitystreams#Public"]
        }
        return self.ap_helper.create_note(reviewer_id, json.dumps(review_data), [paper_id])

    def cite_paper(self, researcher_id: str, citing_paper_id: str, cited_paper_id: str, context: Optional[str] = None) -> Dict:
        """Create a citation relationship between two papers."""
        citation_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Announce",
            "actor": researcher_id,
            "object": cited_paper_id,
            "target": citing_paper_id,
            "summary": "This paper cites the following work",
            "content": context,
            "published": datetime.utcnow().isoformat() + "Z",
            "to": ["https://www.w3.org/ns/activitystreams#Public"],
            "sci:citation": {
                "type": "Citation",
                "citingWork": citing_paper_id,
                "citedWork": cited_paper_id
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(citation_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def collaborate(self, researcher1_id: str, researcher2_id: str, project_name: Optional[str] = None) -> Dict:
        """Establish a collaboration between two researchers."""
        collaboration_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Offer",
            "actor": researcher1_id,
            "object": {
                "type": "sci:ResearchProject",
                "name": f"Collaboration on {project_name}" if project_name else "Research Collaboration",
                "summary": f"Collaboration established between {researcher1_id} and {researcher2_id}",
                "sci:projectName": project_name
            },
            "target": researcher2_id,
            "published": datetime.utcnow().isoformat() + "Z",
            "to": [researcher2_id, "https://www.w3.org/ns/activitystreams#Public"]
        }
        return self.ap_helper.create_note(researcher1_id, json.dumps(collaboration_data), [researcher2_id, "https://www.w3.org/ns/activitystreams#Public"])

    def search_papers(self, query: str, limit: int = 20, filters: Optional[Dict] = None) -> List[Dict]:
        """Search for scientific papers in the network."""
        search_data = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": "Search",
            "query": query,
            "limit": limit,
            "filters": filters or {}
        }
        return self.ap_helper.search(json.dumps(search_data), type="Article", limit=limit, additional_params=filters)

    def get_researcher_publications(self, researcher_id: str, limit: int = 20, 
                                    start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict]:
        """Fetch publications of a specific researcher."""
        params = {
            "type": "Create",
            "actor": researcher_id,
            "object.type": "Article",
            "limit": limit,
            "published.gte": start_date,
            "published.lte": end_date
        }
        return self.ap_helper.get_outbox(researcher_id, params=params)

    def get_paper_reviews(self, paper_id: str) -> List[Dict]:
        """Fetch reviews for a specific paper."""
        paper_data = self.ap_helper.get_note(paper_id)
        return paper_data.get("replies", {}).get("items", [])

    def endorse_paper(self, researcher_id: str, paper_id: str, endorsement_text: Optional[str] = None) -> Dict:
        """Endorse a scientific paper."""
        endorse_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Like",
            "actor": researcher_id,
            "object": paper_id,
            "content": endorsement_text,
            "published": datetime.utcnow().isoformat() + "Z",
            "to": ["https://www.w3.org/ns/activitystreams#Public"],
            "sci:endorsement": {
                "type": "EndorseAction",
                "agent": researcher_id,
                "object": paper_id
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(endorse_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def retract_paper(self, researcher_id: str, paper_id: str, reason: str) -> Dict:
        """Retract a published paper."""
        retract_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Undo",
            "actor": researcher_id,
            "object": {
                "type": "Create",
                "object": paper_id
            },
            "summary": "Paper retraction",
            "content": reason,
            "published": datetime.utcnow().isoformat() + "Z",
            "to": ["https://www.w3.org/ns/activitystreams#Public"],
            "sci:retractionNotice": {
                "type": "RetractionNotice",
                "about": paper_id,
                "description": reason
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(retract_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def create_dataset(self, researcher_id: str, title: str, description: str, url: str, license: str) -> Dict:
        """Create a new dataset entry."""
        dataset_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Create",
            "actor": researcher_id,
            "object": {
                "type": "sci:Dataset",
                "attributedTo": researcher_id,
                "name": title,
                "content": description,
                "url": url,
                "license": license,
                "published": datetime.utcnow().isoformat() + "Z",
                "to": ["https://www.w3.org/ns/activitystreams#Public"],
                "sci:distribution": {
                    "type": "DataDownload",
                    "contentUrl": url,
                    "encodingFormat": "application/zip"
                }
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(dataset_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def organize_conference(self, organizer_id: str, title: str, description: str, date: str, location: str) -> Dict:
        """Organize a scientific conference."""
        conference_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Create",
            "actor": organizer_id,
            "object": {
                "type": "Event",
                "name": title,
                "content": description,
                "startTime": date,
                "location": {
                    "type": "Place",
                    "name": location
                },
                "published": datetime.utcnow().isoformat() + "Z",
                "to": ["https://www.w3.org/ns/activitystreams#Public"],
                "sci:about": "Scientific Conference",
                "sci:organizer": organizer_id
            }
        }
        return self.ap_helper.create_note(organizer_id, json.dumps(conference_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def submit_grant_proposal(self, researcher_id: str, title: str, abstract: str, amount: float, funder: str) -> Dict:
        """Submit a grant proposal."""
        proposal_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Create",
            "actor": researcher_id,
            "object": {
                "type": "sci:Grant",
                "name": title,
                "summary": abstract,
                "sci:amount": {
                    "type": "MonetaryAmount",
                    "value": amount,
                    "currency": "USD"
                },
                "sci:funder": {
                    "type": "Organization",
                    "name": funder
                },
                "tag": [{"type": "Hashtag", "name": "#GrantProposal"}],
                "published": datetime.utcnow().isoformat() + "Z",
                "to": ["https://www.w3.org/ns/activitystreams#Public"]
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(proposal_data), ["https://www.w3.org/ns/activitystreams#Public"])

    def create_lab_notebook_entry(self, researcher_id: str, title: str, content: str, experiment_id: Optional[str] = None) -> Dict:
        """Create a lab notebook entry."""
        entry_data = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
                {"sci": "http://schema.org/"}
            ],
            "type": "Create",
            "actor": researcher_id,
            "object": {
                "type": "sci:LabNotebookEntry",
                "name": title,
                "content": content,
                "sci:experimentId": experiment_id,
                "tag": [{"type": "Hashtag", "name": "#LabNotebook"}],
                "published": "2023-06-15T22:45:00Z",  # Add actual entry creation date
                "to": ["https://www.w3.org/ns/activitystreams#Public"]
            }
        }
        return self.ap_helper.create_note(researcher_id, json.dumps(entry_data), ["https://www.w3.org/ns/activitystreams#Public"])

# Example usage:
if __name__ == "__main__":
    base_url = "https://example.com/api"
    access_token = "your_access_token_here"
    dss = DecentralizedScienceSystem(base_url, access_token)

    # Create a researcher
    researcher = dss.create_researcher("johndoe", "John Doe", "Quantum physicist", ["Physics", "Quantum Mechanics"])
    researcher_id = researcher["id"]

    # Publish a paper
    paper = dss.publish_paper(
        researcher_id,
        "Quantum Entanglement in Neural Networks",
        "This paper explores the intersection of quantum mechanics and machine learning.",
        "Full paper content here...",
        ["quantum", "machine learning", "neural networks"],
        doi="10.1234/example.doi",
        references=["https://example.com/reference1", "https://example.com/reference2"]
    )
    paper_id = paper["id"]

    # Submit a peer review
    review = dss.peer_review(
        researcher_id,
        paper_id,
        "This paper presents an innovative approach to combining quantum mechanics and neural networks.",
        rating=4
    )

    # Cite a paper
    citation = dss.cite_paper(
        researcher_id,
        "https://example.com/citing-paper-id",
        paper_id,
        "This work builds upon the quantum neural network model proposed by Doe et al."
    )

    # Collaborate with another researcher
    collaboration = dss.collaborate(researcher_id, "https://example.com/researcher2-id", "Quantum-Enhanced ML")

    # Search for papers
    search_results = dss.search_papers("quantum neural networks", limit=5)

    # Get researcher's publications
    publications = dss.get_researcher_publications(researcher_id, limit=10, start_date="2023-01-01")

    # Get paper reviews
    reviews = dss.get_paper_reviews(paper_id)

    # Endorse a paper
    endorsement = dss.endorse_paper(researcher_id, paper_id, "Groundbreaking work in quantum machine learning!")

    # Retract a paper
    retraction = dss.retract_paper(researcher_id, paper_id, "Significant error found in methodology")

    # Create a dataset
    dataset = dss.create_dataset(
        researcher_id,
        "Quantum Neural Network Training Data",
        "A dataset of quantum states used for training quantum neural networks",
        "https://example.com/dataset",
        "CC-BY-4.0"
    )

    # Organize a conference
    conference = dss.organize_conference(
        researcher_id,
        "International Quantum Machine Learning Conference",
        "A conference dedicated to the latest advancements in quantum machine learning",
        "2024-06-15",
        "Virtual"
    )

    # Submit a grant proposal
    proposal = dss.submit_grant_proposal(
        researcher_id,
        "Quantum-Enhanced Neural Networks for Drug Discovery",
        "This project aims to leverage quantum computing to enhance neural networks for accelerated drug discovery.",
        amount=500000.00,
        funder="National Science Foundation"
    )

    # Create a lab notebook entry
    lab_entry = dss.create_lab_notebook_entry(
        researcher_id,
        "Quantum Neural Network Experiment #1",
        "Today, we initialized our quantum neural network with 5 qubits...",
        experiment_id="QNN-001"
    )

    print("All operations completed successfully!")
