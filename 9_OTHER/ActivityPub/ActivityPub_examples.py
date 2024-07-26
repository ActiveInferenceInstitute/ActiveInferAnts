import json
import uuid
import random
from datetime import datetime, timedelta
from typing import List, Dict
from ActivityPub_Science import DecentralizedScienceSystem
from Helpful_ActivityPub import ActivityPubHelper, Note, Create, Event, EventKind

# Initialize the DecentralizedScienceSystem and ActivityPubHelper
base_url = "https://example.com"
access_token = "your_access_token_here"
dss = DecentralizedScienceSystem(base_url, access_token)
ap_helper = ActivityPubHelper(base_url, access_token)

def create_researcher_and_publish_paper():
    # Create a researcher
    researcher = dss.create_researcher(
        username="alice_researcher",
        display_name="Dr. Alice Smith",
        bio="Quantum physicist specializing in entanglement",
        fields=["quantum_physics", "entanglement"]
    )
    researcher_id = researcher["id"]

    # Publish a paper
    paper = dss.publish_paper(
        researcher_id=researcher_id,
        title="Novel Approaches to Quantum Entanglement",
        abstract="This paper explores innovative techniques in quantum entanglement...",
        content="Full content of the paper...",
        keywords=["quantum", "entanglement", "physics"],
        doi="10.1234/example.doi"
    )
    paper_id = paper["object"]["id"]

    # Announce the paper publication
    announce_publication(researcher_id, paper_id)

    return researcher_id, paper_id

def announce_publication(researcher_id: str, paper_id: str):
    announcement = ap_helper.create_announce(
        actor=researcher_id,
        object=paper_id,
        to=["https://www.w3.org/ns/activitystreams#Public"],
        cc=[f"{researcher_id}/followers"]
    )
    ap_helper.post_to_outbox(researcher_id, announcement)

def review_and_cite_paper(reviewer_id: str, paper_id: str, citing_paper_id: str):
    # Review the paper
    review = dss.review_paper(
        reviewer_id=reviewer_id,
        paper_id=paper_id,
        review_text="This paper presents groundbreaking ideas in quantum entanglement...",
        rating=4.5
    )

    # Announce the review
    announce_review(reviewer_id, review["id"])

    # Cite the paper
    citation = dss.cite_paper(
        researcher_id=reviewer_id,
        citing_paper_id=citing_paper_id,
        cited_paper_id=paper_id,
        context="This work builds upon the novel approaches presented in..."
    )

    # Announce the citation
    announce_citation(reviewer_id, citation["id"])

    return review, citation

def announce_review(reviewer_id: str, review_id: str):
    announcement = ap_helper.create_announce(
        actor=reviewer_id,
        object=review_id,
        to=["https://www.w3.org/ns/activitystreams#Public"],
        cc=[f"{reviewer_id}/followers"]
    )
    ap_helper.post_to_outbox(reviewer_id, announcement)

def announce_citation(researcher_id: str, citation_id: str):
    announcement = ap_helper.create_announce(
        actor=researcher_id,
        object=citation_id,
        to=["https://www.w3.org/ns/activitystreams#Public"],
        cc=[f"{researcher_id}/followers"]
    )
    ap_helper.post_to_outbox(researcher_id, announcement)

class ScienceAnt:
    def __init__(self, name: str, domain: str):
        self.name = name
        self.domain = domain
        self.actor_id = f"https://{domain}/users/{name}"
        self.ap_client = ActivityPubHelper(f"https://{domain}", "access_token")
        self.dss = DecentralizedScienceSystem(f"https://{domain}", "access_token")

    def publish_paper(self, title: str, abstract: str, content: str, keywords: List[str]):
        paper = self.dss.publish_paper(
            researcher_id=self.actor_id,
            title=title,
            abstract=abstract,
            content=content,
            keywords=keywords,
            doi=f"10.{random.randint(1000, 9999)}/example.doi"
        )
        paper_id = paper["object"]["id"]
        self.announce_publication(paper_id)
        return paper_id

    def announce_publication(self, paper_id: str):
        announcement = self.ap_client.create_announce(
            actor=self.actor_id,
            object=paper_id,
            to=["https://www.w3.org/ns/activitystreams#Public"],
            cc=[f"{self.actor_id}/followers"]
        )
        self.ap_client.post_to_outbox(self.actor_id, announcement)
        print(f"{self.name} announced a new paper: {paper_id}")

    def review_paper(self, paper_id: str, review_text: str, rating: float):
        review = self.dss.review_paper(
            reviewer_id=self.actor_id,
            paper_id=paper_id,
            review_text=review_text,
            rating=rating
        )
        review_id = review["id"]
        self.announce_review(review_id)
        return review_id

    def announce_review(self, review_id: str):
        announcement = self.ap_client.create_announce(
            actor=self.actor_id,
            object=review_id,
            to=["https://www.w3.org/ns/activitystreams#Public"],
            cc=[f"{self.actor_id}/followers"]
        )
        self.ap_client.post_to_outbox(self.actor_id, announcement)
        print(f"{self.name} announced a new review: {review_id}")

def simulate_science_communication(ant1: ScienceAnt, ant2: ScienceAnt):
    # Ant1 publishes a paper
    paper_id = ant1.publish_paper(
        title="Quantum Entanglement in Ant Colonies",
        abstract="This paper explores the fascinating connection between quantum entanglement and ant colony behavior...",
        content="Full content of the paper...",
        keywords=["quantum", "entanglement", "ants", "swarm intelligence"]
    )

    # Ant2 reviews the paper
    ant2.review_paper(
        paper_id=paper_id,
        review_text="This paper presents an intriguing hypothesis linking quantum phenomena to ant behavior...",
        rating=4.0
    )

class NostrAnt:
    def __init__(self, name: str):
        self.name = name
        self.public_key = "dummy_public_key"
        self.private_key = "dummy_private_key"
        self.relay_manager = DummyRelayManager()

    def send_message(self, content: str):
        event = Event(
            kind=EventKind.TEXT_NOTE,
            content=content,
            tags=[],
            pub_key=self.public_key,
        )
        event.sign(self.private_key)
        self.relay_manager.publish_event(event)
        print(f"{self.name} (Nostr): {content}")

    def receive_messages(self):
        return self.relay_manager.get_events()

class ActivityPubAnt:
    def __init__(self, name: str, domain: str):
        self.name = name
        self.domain = domain
        self.actor = type('Actor', (), {'id': f"https://{domain}/users/{name}", 'followers': f"https://{domain}/users/{name}/followers"})()
        self.ap_client = ActivityPubHelper(f"https://{domain}", "access_token")

    def send_message(self, content: str):
        note = Note(
            id=f"https://{self.domain}/notes/{uuid.uuid4()}",
            content=content,
            attributedTo=self.actor.id,
            to=["https://www.w3.org/ns/activitystreams#Public"],
            cc=[self.actor.followers]
        )
        create_activity = Create(actor=self.actor.id, object=note)
        self.ap_client.post_to_outbox(create_activity)
        print(f"{self.name} (ActivityPub): {content}")

    def like(self, object_id: str):
        like_activity = self.ap_client.create_like(
            actor=self.actor.id,
            object=object_id,
            to=["https://www.w3.org/ns/activitystreams#Public"],
            cc=[self.actor.followers]
        )
        self.ap_client.post_to_outbox(self.actor.id, like_activity)
        print(f"{self.name} liked: {object_id}")

def simulate_communication(nostr_ant: NostrAnt, activitypub_ant: ActivityPubAnt, iterations: int):
    for i in range(iterations):
        print(f"\nIteration {i+1}:")
        
        # Nostr ant sends a message
        nostr_message = f"Hello from Nostr land! The temperature is {random.randint(0, 30)}°C."
        nostr_ant.send_message(nostr_message)

        # ActivityPub ant receives and processes the message
        received_nostr = nostr_ant.receive_messages()
        for msg in received_nostr:
            print(f"{activitypub_ant.name} received: {msg['content']} from {msg['pubkey']}")
            response = f"Greetings from ActivityPub world! I heard it's {msg['content'].split()[-1]} there."
            activitypub_ant.send_message(response)
            activitypub_ant.like(msg['id'])

def main():
    # Create a researcher and publish a paper
    researcher_id, paper_id = create_researcher_and_publish_paper()
    print(f"Researcher created: {researcher_id}")
    print(f"Paper published: {paper_id}")

    # Review and cite the paper
    reviewer_id = "https://example.com/users/bob_reviewer"
    citing_paper_id = "https://example.com/papers/citing_paper"
    review, citation = review_and_cite_paper(reviewer_id, paper_id, citing_paper_id)
    print(f"Review created: {review['id']}")
    print(f"Citation created: {citation['id']}")

    # Example using ScienceAnts
    science_ant1 = ScienceAnt("QuantumAnt", "quantumlab.com")
    science_ant2 = ScienceAnt("EntanglementAnt", "entanglement.org")
    simulate_science_communication(science_ant1, science_ant2)

    # Example using Nostr and ActivityPub Ants
    nostr_ant = NostrAnt("NostrAnt")
    activitypub_ant = ActivityPubAnt("ActivityPubAnt", "example.com")
    simulate_communication(nostr_ant, activitypub_ant, iterations=3)

if __name__ == "__main__":
    main()

# Dummy classes for demonstration purposes
class DummyRelayManager:
    def publish_event(self, event):
        pass

    def get_events(self):
        return [{'content': 'Dummy Nostr message', 'pubkey': 'dummy_pubkey', 'id': 'dummy_id'}]
