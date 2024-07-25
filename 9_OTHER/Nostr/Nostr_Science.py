import json
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict, field
from enum import Enum, auto
import time
from abc import ABC, abstractmethod
import asyncio
from nostr.event import Event
from nostr.key import PrivateKey, PublicKey
from nostr.relay_manager import RelayManager
from nostr.filter import Filter, Filters
from nostr.message_type import ClientMessageType
from datetime import datetime, timezone
import hashlib

class ContentType(Enum):
    RESEARCH_PAPER = auto()
    EXPERIMENT_PROTOCOL = auto()
    DATASET = auto()
    PEER_REVIEW = auto()
    EDUCATIONAL_RESOURCE = auto()
    RESEARCH_PROPOSAL = auto()
    CONFERENCE_PRESENTATION = auto()
    JOURNAL_PUBLICATION = auto()
    GRANT_APPLICATION = auto()
    PATENT_APPLICATION = auto()

@dataclass
class NostrEvent:
    id: str
    pubkey: str
    created_at: int
    kind: int
    tags: List[List[str]]
    content: str
    sig: str

    def to_json(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class ScientificContent:
    type: ContentType
    title: str
    abstract: str
    content: str
    authors: List[str]
    keywords: List[str]
    doi: Optional[str] = None
    publication_date: Optional[str] = None
    version: str = "1.0"
    license: str = "CC BY 4.0"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> Dict[str, Any]:
        return asdict(self)

class NostrScience:
    def __init__(self, relay_manager: RelayManager, private_key: str):
        self.relay_manager = relay_manager
        self.private_key = PrivateKey(bytes.fromhex(private_key))
        self.public_key = self.private_key.public_key

    async def create_and_publish_event(self, kind: int, tags: List[List[str]], content: Union[str, Dict[str, Any]]) -> Event:
        if isinstance(content, dict):
            content = json.dumps(content)
        
        created_at = int(time.time())
        event = Event(
            public_key=self.public_key.hex(),
            created_at=created_at,
            kind=kind,
            tags=tags,
            content=content
        )
        event.sign(self.private_key.hex())
        
        await self.relay_manager.publish_event(event)
        return event

    async def publish_scientific_content(self, content: ScientificContent, additional_tags: List[List[str]] = None) -> Event:
        tags = [
            ["t", content.type.name.lower()],
            ["title", content.title],
        ] + [["keyword", kw] for kw in content.keywords]
        
        if additional_tags:
            tags.extend(additional_tags)
        
        event_content = content.to_json()
        return await self.create_and_publish_event(1, tags, event_content)

    async def publish_research_paper(self, paper: ScientificContent) -> Event:
        paper.type = ContentType.RESEARCH_PAPER
        return await self.publish_scientific_content(paper)

    async def publish_experiment_protocol(self, protocol: ScientificContent) -> Event:
        protocol.type = ContentType.EXPERIMENT_PROTOCOL
        return await self.publish_scientific_content(protocol)

    async def publish_dataset(self, dataset: ScientificContent, data_url: str) -> Event:
        dataset.type = ContentType.DATASET
        additional_tags = [["data_url", data_url]]
        return await self.publish_scientific_content(dataset, additional_tags)

    async def publish_peer_review(self, review: ScientificContent, paper_id: str) -> Event:
        review.type = ContentType.PEER_REVIEW
        additional_tags = [["e", paper_id]]
        return await self.publish_scientific_content(review, additional_tags)

    async def publish_educational_resource(self, resource: ScientificContent, subject: str, level: str) -> Event:
        resource.type = ContentType.EDUCATIONAL_RESOURCE
        additional_tags = [["subject", subject], ["level", level]]
        return await self.publish_scientific_content(resource, additional_tags)

    async def publish_research_proposal(self, proposal: ScientificContent, funding_amount: float) -> Event:
        proposal.type = ContentType.RESEARCH_PROPOSAL
        additional_tags = [["funding_amount", str(funding_amount)]]
        return await self.publish_scientific_content(proposal, additional_tags)

    async def publish_conference_presentation(self, presentation: ScientificContent, conference_name: str, presentation_date: str) -> Event:
        presentation.type = ContentType.CONFERENCE_PRESENTATION
        additional_tags = [["conference", conference_name], ["date", presentation_date]]
        return await self.publish_scientific_content(presentation, additional_tags)

    async def publish_journal_publication(self, publication: ScientificContent, journal_name: str, issue: str, pages: str) -> Event:
        publication.type = ContentType.JOURNAL_PUBLICATION
        additional_tags = [["journal", journal_name], ["issue", issue], ["pages", pages]]
        return await self.publish_scientific_content(publication, additional_tags)

    async def publish_grant_application(self, application: ScientificContent, funding_agency: str, grant_amount: float) -> Event:
        application.type = ContentType.GRANT_APPLICATION
        additional_tags = [["funding_agency", funding_agency], ["grant_amount", str(grant_amount)]]
        return await self.publish_scientific_content(application, additional_tags)

    async def publish_patent_application(self, patent: ScientificContent, application_number: str, filing_date: str) -> Event:
        patent.type = ContentType.PATENT_APPLICATION
        additional_tags = [["application_number", application_number], ["filing_date", filing_date]]
        return await self.publish_scientific_content(patent, additional_tags)

    async def get_scientific_content(self, content_type: ContentType, additional_filters: Dict[str, List[str]] = None) -> List[Event]:
        tags = {'t': [content_type.name.lower()]}
        if additional_filters:
            tags.update(additional_filters)
        filters = Filters([Filter(kinds=[1], tags=tags)])
        return await self.subscribe_to_events(filters)

    async def subscribe_to_events(self, filters: Filters) -> List[Event]:
        events = []
        subscription_id = self.relay_manager.add_subscription(filters)
        
        async def event_handler(event: Event):
            events.append(event)

        self.relay_manager.add_event_handler(event_handler)
        
        while True:
            event_msg = await self.relay_manager.receive_message()
            if event_msg.type == ClientMessageType.EOSE:
                break

        self.relay_manager.remove_event_handler(event_handler)
        self.relay_manager.close_subscription(subscription_id)
        return events

    @staticmethod
    def generate_doi(event: Event) -> str:
        """Generate a DOI-like identifier based on the event."""
        prefix = "10.5555"  # Example DOI prefix
        suffix = hashlib.sha256(event.id.encode()).hexdigest()[:8]
        return f"{prefix}/{suffix}"

    @staticmethod
    def validate_scientific_content(content: ScientificContent) -> bool:
        """Validate the scientific content."""
        required_fields = ['title', 'abstract', 'content', 'authors', 'keywords']
        return all(getattr(content, field) for field in required_fields)

# Example usage:
async def main():
    relay_urls = ["wss://relay.damus.io", "wss://relay.nostr.info", "wss://nostr-pub.wellorder.net"]
    relay_manager = RelayManager()
    for url in relay_urls:
        relay_manager.add_relay(url)
    await relay_manager.open_connections()
    
    private_key = PrivateKey().hex()
    nostr_science = NostrScience(relay_manager, private_key)

    # Publish a research paper
    paper_content = ScientificContent(
        type=ContentType.RESEARCH_PAPER,
        title="Novel Approach to Quantum Computing",
        abstract="This paper presents a groundbreaking method in quantum computing...",
        content="Full paper content here...",
        authors=["Alice Johnson", "Bob Smith"],
        keywords=["quantum computing", "algorithm", "qubit"],
        metadata={"institution": "Quantum University"}
    )
    paper_event = await nostr_science.publish_research_paper(paper_content)
    paper_content.doi = NostrScience.generate_doi(paper_event)
    
    # Update the event with the generated DOI
    updated_paper_event = await nostr_science.publish_research_paper(paper_content)

    # Publish an experiment protocol
    protocol_content = ScientificContent(
        type=ContentType.EXPERIMENT_PROTOCOL,
        title="Quantum Entanglement Experiment",
        abstract="A detailed protocol for demonstrating quantum entanglement",
        content="Step 1: Prepare the quantum system...",
        authors=["Charlie Brown"],
        keywords=["quantum entanglement", "experimental physics"],
        metadata={"equipment": ["Quantum Computer", "Laser", "Detector"]}
    )
    protocol_event = await nostr_science.publish_experiment_protocol(protocol_content)

    # Publish a dataset
    dataset_content = ScientificContent(
        type=ContentType.DATASET,
        title="Quantum Computation Results",
        abstract="This dataset contains the results of our quantum computing experiments",
        content="Data description and analysis...",
        authors=["David Wilson", "Eva Garcia"],
        keywords=["quantum data", "experimental results"],
        metadata={"data_format": "CSV", "sample_size": 1000}
    )
    dataset_event = await nostr_science.publish_dataset(dataset_content, "https://example.com/dataset.csv")

    # Publish a peer review
    review_content = ScientificContent(
        type=ContentType.PEER_REVIEW,
        title="Review of 'Novel Approach to Quantum Computing'",
        abstract="A critical analysis of the proposed quantum computing method",
        content="This paper presents an interesting approach, however...",
        authors=["Frank Lee"],
        keywords=["peer review", "quantum computing"],
        metadata={"recommendation": "Major Revision"}
    )
    review_event = await nostr_science.publish_peer_review(review_content, updated_paper_event.id)

    # Retrieve and print all research papers
    papers = await nostr_science.get_scientific_content(ContentType.RESEARCH_PAPER)
    print(f"Number of research papers: {len(papers)}")

    # Retrieve and print all peer reviews for a specific paper
    reviews = await nostr_science.get_scientific_content(ContentType.PEER_REVIEW, {"e": [updated_paper_event.id]})
    print(f"Number of peer reviews for the paper: {len(reviews)}")

    relay_manager.close_connections()

if __name__ == "__main__":
    asyncio.run(main())
