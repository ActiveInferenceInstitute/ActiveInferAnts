import asyncio
import uuid
import json
import re
from typing import Dict, List, Any, Optional
from urllib.parse import urlparse

import requests
from cryptography.fernet import Fernet
from pyld import jsonld

from activitypub.activities import Create, Note, Follow, Like, Announce, Undo, Delete
from activitypub.actors import Actor, Person
from activitypub.manager import Manager
from activitypub.database import Database
from activitypub.collections import OrderedCollection
from activitypub.security import HTTPSignature
from activitypub.linked_data_signature import LinkedDataSignature

from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

class ActivityPubCogSec:
    def __init__(self, base_url: str, private_key_path: str, public_key_path: str):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/activity+json"
        }
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.db = Database("sqlite:///activitypub_cogsec.db")
        self.manager = Manager(self.db)
        self.http_signature = HTTPSignature(private_key_path=private_key_path)
        self.ld_signature = LinkedDataSignature(private_key_path=private_key_path)
        
        # Initialize NLP models
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        self.misinformation_detector = pipeline("text-classification", model="roberta-base-openai-detector")

    async def detect_misinformation(self, content: str) -> float:
        result = self.misinformation_detector(content)[0]
        return result['score'] if result['label'] == 'LABEL_1' else 1 - result['score']

    def analyze_sentiment(self, content: str) -> float:
        return self.sentiment_analyzer.polarity_scores(content)['compound']

    def encrypt_sensitive_data(self, data: str) -> str:
        return self.cipher_suite.encrypt(data.encode()).decode()

    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()

    async def validate_actor(self, actor_id: str) -> bool:
        try:
            actor = await self.manager.fetch_actor(actor_id)
            return isinstance(actor, Actor)
        except Exception:
            return False

    def create_cognitive_security_note(self, content: str, target_actor: str) -> Dict[str, Any]:
        note = Note(
            id=f"{self.base_url}/notes/{uuid.uuid4()}",
            attributedTo=self.base_url,
            content=content,
            to=[target_actor, "https://www.w3.org/ns/activitystreams#Public"],
            cc=[f"{self.base_url}/followers"],
            tag=[
                {
                    "type": "Mention",
                    "href": target_actor,
                    "name": f"@{urlparse(target_actor).path.split('/')[-1]}"
                }
            ],
            cognitiveSecurityMetadata={
                "misinformationProbability": asyncio.run(self.detect_misinformation(content)),
                "sentiment": self.analyze_sentiment(content),
                "encryptedAnalysis": self.encrypt_sensitive_data(json.dumps({
                    "detailedAnalysis": "Placeholder for detailed cognitive security analysis",
                    "confidenceScore": 0.85,
                    "sourceReliability": "medium"
                }))
            }
        )
        return note.to_dict()

    async def post_cognitive_security_note(self, note: Dict[str, Any]) -> bool:
        create_activity = Create(object=note)
        signed_activity = self.ld_signature.sign(create_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def monitor_incoming_activities(self) -> List[Dict[str, Any]]:
        inbox_activities = await self.manager.get_inbox()
        return [
            activity.to_dict() for activity in inbox_activities
            if await self.validate_actor(activity.actor)
            and await self.detect_misinformation(activity.object.content if hasattr(activity.object, 'content') else '') < 0.5
        ]

    def generate_cognitive_security_report(self, activities: List[Dict[str, Any]]) -> str:
        report = "Cognitive Security Report\n"
        report += "==========================\n\n"
        for activity in activities:
            content = activity.get("object", {}).get("content", "")
            report += f"Activity Type: {activity.get('type', 'Unknown')}\n"
            report += f"Actor: {activity.get('actor', 'Unknown')}\n"
            report += f"Content: {content}\n"
            report += f"Misinformation Probability: {asyncio.run(self.detect_misinformation(content)):.2f}\n"
            report += f"Sentiment: {self.analyze_sentiment(content):.2f}\n"
            report += f"Timestamp: {activity.get('published', 'Unknown')}\n"
            report += "---\n"
        return report

    def apply_content_policy(self, content: str) -> str:
        policy_violations = [
            (r'\b(hate|offensive|discriminatory)\b', '[REDACTED]'),
            (r'\b(violence|threat|harassment)\b', '[CONTENT WARNING]'),
            (r'\b(explicit|nsfw)\b', '[ADULT CONTENT]')
        ]
        for pattern, replacement in policy_violations:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        return content

    async def cognitive_security_pipeline(self, incoming_activity: Dict[str, Any]) -> Dict[str, Any]:
        actor = incoming_activity.get("actor", "")
        content = incoming_activity.get("object", {}).get("content", "")

        if not await self.validate_actor(actor):
            return {"error": "Invalid actor"}

        content = self.apply_content_policy(content)
        
        analysis = {
            "misinformationProbability": await self.detect_misinformation(content),
            "sentiment": self.analyze_sentiment(content),
            "contentAfterPolicy": content
        }

        if analysis["misinformationProbability"] > 0.7:
            warning_note = self.create_cognitive_security_note(
                f"Warning: High probability of misinformation detected in a post by {actor}",
                actor
            )
            await self.post_cognitive_security_note(warning_note)

        return {
            "originalActivity": incoming_activity,
            "cognitiveSecurityAnalysis": analysis
        }

    async def follow_actor(self, target_actor: str) -> bool:
        follow_activity = Follow(actor=self.base_url, object=target_actor)
        signed_activity = self.ld_signature.sign(follow_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def unfollow_actor(self, target_actor: str) -> bool:
        undo_activity = Undo(
            actor=self.base_url,
            object=Follow(actor=self.base_url, object=target_actor)
        )
        signed_activity = self.ld_signature.sign(undo_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def like_object(self, object_id: str) -> bool:
        like_activity = Like(actor=self.base_url, object=object_id)
        signed_activity = self.ld_signature.sign(like_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def unlike_object(self, object_id: str) -> bool:
        undo_activity = Undo(
            actor=self.base_url,
            object=Like(actor=self.base_url, object=object_id)
        )
        signed_activity = self.ld_signature.sign(undo_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def announce_object(self, object_id: str) -> bool:
        announce_activity = Announce(actor=self.base_url, object=object_id)
        signed_activity = self.ld_signature.sign(announce_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def unannounce_object(self, object_id: str) -> bool:
        undo_activity = Undo(
            actor=self.base_url,
            object=Announce(actor=self.base_url, object=object_id)
        )
        signed_activity = self.ld_signature.sign(undo_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def delete_object(self, object_id: str) -> bool:
        delete_activity = Delete(actor=self.base_url, object=object_id)
        signed_activity = self.ld_signature.sign(delete_activity.to_dict())
        try:
            await self.manager.post_to_outbox(signed_activity)
            return True
        except Exception:
            return False

    async def get_followers(self) -> OrderedCollection:
        return await self.manager.get_followers(self.base_url)

    async def get_following(self) -> OrderedCollection:
        return await self.manager.get_following(self.base_url)

    async def update_profile(self, name: Optional[str] = None, summary: Optional[str] = None) -> bool:
        person = Person(id=self.base_url)
        if name:
            person.name = name
        if summary:
            person.summary = summary
        try:
            await self.manager.update_actor(person)
            return True
        except Exception:
            return False

    async def fetch_remote_object(self, object_id: str) -> Dict[str, Any]:
        try:
            return await self.manager.fetch_remote_object(object_id)
        except Exception:
            return {}

    async def process_incoming_activity(self, activity: Dict[str, Any]) -> None:
        activity_type = activity.get("type")
        
        if activity_type == "Follow":
            # Auto-accept follows
            accept = Create(
                actor=self.base_url,
                object={
                    "type": "Accept",
                    "actor": self.base_url,
                    "object": activity
                }
            )
            signed_accept = self.ld_signature.sign(accept.to_dict())
            await self.manager.post_to_outbox(signed_accept)
        
        elif activity_type in ["Create", "Update", "Delete", "Like", "Announce"]:
            # Process the activity through the cognitive security pipeline
            await self.cognitive_security_pipeline(activity)

    async def federated_search(self, query: str) -> List[Dict[str, Any]]:
        # This is a placeholder for a federated search implementation
        # In a real-world scenario, this would involve querying multiple instances
        return []

# Usage examples:

async def main():
    # Initialize the ActivityPubCogSec instance
    cogsec = ActivityPubCogSec("https://example.com", "path/to/private_key.pem", "path/to/public_key.pem")

    # Example 1: Detect misinformation
    content = "This is a conspiracy theory about fake news!"
    misinformation_prob = await cogsec.detect_misinformation(content)
    print(f"Misinformation probability: {misinformation_prob:.2f}")

    # Example 2: Analyze sentiment
    content = "This is a great day for ActivityPub!"
    sentiment = cogsec.analyze_sentiment(content)
    print(f"Sentiment score: {sentiment:.2f}")

    # Example 3: Encrypt and decrypt sensitive data
    sensitive_data = "This is sensitive information"
    encrypted = cogsec.encrypt_sensitive_data(sensitive_data)
    decrypted = cogsec.decrypt_sensitive_data(encrypted)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

    # Example 4: Validate actor
    actor_id = "https://example.com/users/alice"
    is_valid = await cogsec.validate_actor(actor_id)
    print(f"Is actor valid: {is_valid}")

    # Example 5: Create and post a cognitive security note
    content = "Attention: Potential security risk detected."
    target_actor = "https://example.com/users/bob"
    note = cogsec.create_cognitive_security_note(content, target_actor)
    posted = await cogsec.post_cognitive_security_note(note)
    print(f"Note posted successfully: {posted}")

    # Example 6: Monitor incoming activities
    incoming_activities = await cogsec.monitor_incoming_activities()
    print(f"Number of valid incoming activities: {len(incoming_activities)}")

    # Example 7: Generate cognitive security report
    report = cogsec.generate_cognitive_security_report(incoming_activities)
    print(report)

    # Example 8: Apply content policy
    content_with_violations = "This post contains hate speech and threats of violence."
    filtered_content = cogsec.apply_content_policy(content_with_violations)
    print(f"Filtered content: {filtered_content}")

    # Example 9: Run cognitive security pipeline
    incoming_activity = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "type": "Create",
        "actor": "https://example.com/users/alice",
        "object": {
            "type": "Note",
            "content": "This is a suspicious post with potential misinformation."
        }
    }
    pipeline_result = await cogsec.cognitive_security_pipeline(incoming_activity)
    print(json.dumps(pipeline_result, indent=2))

    # Example 10: Follow and unfollow an actor
    target_actor = "https://example.com/users/charlie"
    followed = await cogsec.follow_actor(target_actor)
    print(f"Successfully followed {target_actor}: {followed}")
    unfollowed = await cogsec.unfollow_actor(target_actor)
    print(f"Successfully unfollowed {target_actor}: {unfollowed}")

    # Example 11: Like and unlike an object
    object_id = "https://example.com/notes/123"
    liked = await cogsec.like_object(object_id)
    print(f"Successfully liked {object_id}: {liked}")
    unliked = await cogsec.unlike_object(object_id)
    print(f"Successfully unliked {object_id}: {unliked}")

    # Example 12: Announce and unannounce an object
    announced = await cogsec.announce_object(object_id)
    print(f"Successfully announced {object_id}: {announced}")
    unannounced = await cogsec.unannounce_object(object_id)
    print(f"Successfully unannounced {object_id}: {unannounced}")

    # Example 13: Delete an object
    deleted = await cogsec.delete_object(object_id)
    # Example 13: Get followers
    followers = await cogsec.get_followers()
    print(f"Number of followers: {len(followers.items)}")

    # Example 14: Get following
    following = await cogsec.get_following()
    print(f"Number of accounts following: {len(following.items)}")

    # Example 15: Update profile
    updated = await cogsec.update_profile(name="CogSec Bot", summary="I help maintain cognitive security in the fediverse.")
    print(f"Profile updated successfully: {updated}")

if __name__ == "__main__":
    asyncio.run(main())
