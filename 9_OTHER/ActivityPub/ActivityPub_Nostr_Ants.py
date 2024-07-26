import json
import time
import random
from typing import List, Dict, Any
from datetime import datetime, timedelta
import uuid

# Nostr-related imports
import nostr
from nostr.key import PrivateKey
from nostr.relay_manager import RelayManager
from nostr.message_type import ClientMessageType
from nostr.event import Event, EventKind
from nostr.filter import Filter, Filters

# ActivityPub-related imports
from activitypub import ActivityPub
from activitypub.activities import Create, Note, Follow, Like, Announce, Delete, Update, Undo
from activitypub.actors import Person
from activitypub.database import Database
from activitypub.client import Client

class Ant:
    def __init__(self, name: str):
        self.name = name

class NostrAnt(Ant):
    def __init__(self, name: str):
        super().__init__(name)
        self.private_key = PrivateKey()
        self.public_key = self.private_key.public_key
        self.relay_manager = RelayManager()
        self.relay_manager.add_relay("wss://relay.damus.io")
        self.relay_manager.add_relay("wss://nostr-pub.wellorder.net")
        self.relay_manager.add_relay("wss://relay.nostr.info")
        self.relay_manager.open_connections()
        self.following = set()
        self.followers = set()

    def send_message(self, content: str):
        event = Event(
            kind=EventKind.TEXT_NOTE,
            content=content,
            tags=[],
            pub_key=self.public_key.hex(),
        )
        event.sign(self.private_key.hex())
        self.relay_manager.publish_event(event)
        print(f"{self.name} (Nostr): {content}")

    def receive_messages(self) -> List[Dict[str, Any]]:
        messages = []
        while self.relay_manager.message_pool.has_events():
            event_msg = self.relay_manager.message_pool.get_event()
            if event_msg.event.kind == EventKind.TEXT_NOTE:
                messages.append({
                    "content": event_msg.event.content,
                    "pubkey": event_msg.event.pub_key,
                    "created_at": event_msg.event.created_at,
                    "id": event_msg.event.id
                })
        return messages

    def follow(self, pubkey: str):
        event = Event(
            kind=EventKind.CONTACTS,
            content="",
            tags=[["p", pubkey]],
            pub_key=self.public_key.hex(),
        )
        event.sign(self.private_key.hex())
        self.relay_manager.publish_event(event)
        self.following.add(pubkey)
        print(f"{self.name} (Nostr) is now following {pubkey}")

    def like(self, event_id: str):
        event = Event(
            kind=EventKind.REACTION,
            content="+",
            tags=[["e", event_id]],
            pub_key=self.public_key.hex(),
        )
        event.sign(self.private_key.hex())
        self.relay_manager.publish_event(event)
        print(f"{self.name} (Nostr) liked event {event_id}")

    def repost(self, event_id: str):
        event = Event(
            kind=EventKind.REPOST,
            content="",
            tags=[["e", event_id]],
            pub_key=self.public_key.hex(),
        )
        event.sign(self.private_key.hex())
        self.relay_manager.publish_event(event)
        print(f"{self.name} (Nostr) reposted event {event_id}")

    def delete_event(self, event_id: str):
        event = Event(
            kind=EventKind.DELETION,
            content="",
            tags=[["e", event_id]],
            pub_key=self.public_key.hex(),
        )
        event.sign(self.private_key.hex())
        self.relay_manager.publish_event(event)
        print(f"{self.name} (Nostr) deleted event {event_id}")

    def update_profile(self, name: str, about: str):
        content = json.dumps({"name": name, "about": about})
        event = Event(
            kind=EventKind.SET_METADATA,
            content=content,
            tags=[],
            pub_key=self.public_key.hex(),
        )
        event.sign(self.private_key.hex())
        self.relay_manager.publish_event(event)
        print(f"{self.name} (Nostr) updated profile: {name}, {about}")

class ActivityPubAnt(Ant):
    def __init__(self, name: str, domain: str):
        super().__init__(name)
        self.domain = domain
        self.db = Database(f"sqlite:///{name}_activitypub.db")
        self.ap_client = ActivityPub(
            username=name,
            domain=domain,
            private_key_pem=f"keys/{name}_private_key.pem",
            public_key_pem=f"keys/{name}_public_key.pem",
            database=self.db
        )
        self.actor = Person(
            id=f"https://{domain}/users/{name}",
            preferredUsername=name,
            name=name,
            summary="I'm an ActivityPub ant!",
            inbox=f"https://{domain}/users/{name}/inbox",
            outbox=f"https://{domain}/users/{name}/outbox",
            followers=f"https://{domain}/users/{name}/followers",
            following=f"https://{domain}/users/{name}/following"
        )
        self.inbox: List[Dict[str, Any]] = []
        self.client = Client(self.actor)

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

    def receive_messages(self) -> List[Dict[str, Any]]:
        messages = []
        for activity in self.inbox:
            if activity["type"] == "Create" and activity["object"]["type"] == "Note":
                messages.append({
                    "content": activity["object"]["content"],
                    "actor": activity["actor"],
                    "id": activity["object"]["id"],
                    "published": activity["object"]["published"]
                })
        self.inbox.clear()
        return messages

    def follow(self, target_actor: str):
        follow_activity = Follow(actor=self.actor.id, object=target_actor)
        self.ap_client.post_to_outbox(follow_activity)
        print(f"{self.name} (ActivityPub) is now following {target_actor}")

    def unfollow(self, target_actor: str):
        undo_activity = Undo(
            actor=self.actor.id,
            object=Follow(actor=self.actor.id, object=target_actor)
        )
        self.ap_client.post_to_outbox(undo_activity)
        print(f"{self.name} (ActivityPub) has unfollowed {target_actor}")

    def like(self, object_id: str):
        like_activity = Like(actor=self.actor.id, object=object_id)
        self.ap_client.post_to_outbox(like_activity)
        print(f"{self.name} (ActivityPub) liked {object_id}")

    def announce(self, object_id: str):
        announce_activity = Announce(
            actor=self.actor.id,
            object=object_id,
            to=["https://www.w3.org/ns/activitystreams#Public"],
            cc=[self.actor.followers]
        )
        self.ap_client.post_to_outbox(announce_activity)
        print(f"{self.name} (ActivityPub) announced {object_id}")

    def delete_object(self, object_id: str):
        delete_activity = Delete(actor=self.actor.id, object=object_id)
        self.ap_client.post_to_outbox(delete_activity)
        print(f"{self.name} (ActivityPub) deleted {object_id}")

    def update_profile(self, name: str, summary: str):
        self.actor.name = name
        self.actor.summary = summary
        update_activity = Update(actor=self.actor.id, object=self.actor)
        self.ap_client.post_to_outbox(update_activity)
        print(f"{self.name} (ActivityPub) updated profile: {name}, {summary}")

    def fetch_actor(self, actor_id: str) -> Dict[str, Any]:
        return self.client.fetch_resource(actor_id)

    def fetch_object(self, object_id: str) -> Dict[str, Any]:
        return self.client.fetch_resource(object_id)

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

        # ActivityPub ant sends a message
        ap_message = f"The weather in ActivityPub land is {random.choice(['sunny', 'rainy', 'cloudy'])}."
        activitypub_ant.send_message(ap_message)

        # Nostr ant receives and processes the message
        activitypub_ant.inbox.append({
            "type": "Create",
            "actor": activitypub_ant.actor.id,
            "object": {
                "type": "Note",
                "content": ap_message,
                "id": f"https://{activitypub_ant.domain}/notes/{uuid.uuid4()}",
                "published": datetime.utcnow().isoformat() + "Z"
            }
        })
        received_ap = activitypub_ant.receive_messages()
        for msg in received_ap:
            print(f"{nostr_ant.name} received: {msg['content']} from {msg['actor']}")
            response = f"Interesting weather update! Here in Nostr, we're experiencing {random.choice(['high', 'low'])} humidity."
            nostr_ant.send_message(response)
            nostr_ant.like(msg['id'])

        # Additional interactions
        if i % 2 == 0:
            nostr_ant.update_profile(f"NostrAnt_{i}", f"I'm a Nostr ant, iteration {i}")
            activitypub_ant.update_profile(f"ActivityPubAnt_{i}", f"I'm an ActivityPub ant, iteration {i}")
        
        if i % 3 == 0:
            nostr_ant.follow(activitypub_ant.actor.id)
            activitypub_ant.follow(nostr_ant.public_key.hex())
        
        if i % 5 == 0:
            activitypub_ant.announce(f"https://{activitypub_ant.domain}/notes/{uuid.uuid4()}")

        time.sleep(2)  # Pause between iterations

if __name__ == "__main__":
    nostr_ant = NostrAnt("NostrAnt")
    activitypub_ant = ActivityPubAnt("ActivityPubAnt", "example.com")
    simulate_communication(nostr_ant, activitypub_ant, iterations=10)
