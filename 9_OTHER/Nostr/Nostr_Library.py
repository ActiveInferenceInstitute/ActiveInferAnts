import asyncio
import json
import time
from typing import List, Dict, Optional, Any, Union
from nostr.event import Event
from nostr.key import PrivateKey, PublicKey
from nostr.relay_manager import RelayManager
from nostr.filter import Filter, Filters
from nostr.message_type import ClientMessageType
from nostr.pow import create_pow_event
from nostr.delegation import create_delegation_event

class NostrLibrary:
    def __init__(self, relays: List[str], private_key: Optional[str] = None):
        self.relay_manager = RelayManager()
        for relay in relays:
            self.relay_manager.add_relay(relay)
        self.relay_manager.open_connections()
        self.private_key = PrivateKey(private_key) if private_key else PrivateKey()
        self.public_key = self.private_key.public_key

    async def publish_event(self, kind: int, content: str, tags: List[List[str]] = None, pow_difficulty: int = 0) -> str:
        event = create_event(
            private_key=self.private_key.hex(),
            kind=kind,
            content=content,
            tags=tags or []
        )
        if pow_difficulty > 0:
            event = create_pow_event(event, pow_difficulty)
        await publish_event(self.relay_manager, event)
        return event.id

    async def fetch_events(self, filters: Union[Filters, List[Filter]], timeout: float = 5.0) -> List[Event]:
        if isinstance(filters, list):
            filters = Filters(filters)
        return await subscribe_to_events(self.relay_manager, filters, timeout=timeout)

    async def fetch_user_profile(self, pubkey: str) -> Optional[Dict[str, Any]]:
        filters = Filters([Filter(authors=[pubkey], kinds=[0], limit=1)])
        events = await self.fetch_events(filters)
        if events:
            return json.loads(events[0].content)
        return None

    async def update_user_profile(self, name: str, about: str, picture: str, additional_fields: Dict[str, str] = None) -> str:
        content = {
            "name": name,
            "about": about,
            "picture": picture,
            **(additional_fields or {})
        }
        return await self.publish_event(kind=0, content=json.dumps(content))

    async def publish_text_note(self, content: str, reply_to: str = None, mentions: List[str] = None, tags: List[List[str]] = None) -> str:
        event_tags = []
        if reply_to:
            event_tags.append(['e', reply_to, '', 'reply'])
        if mentions:
            event_tags.extend([['p', mention] for mention in mentions])
        if tags:
            event_tags.extend(tags)
        return await self.publish_event(kind=1, content=content, tags=event_tags)

    async def fetch_user_notes(self, pubkey: str, limit: int = 20, since: int = None, until: int = None) -> List[Event]:
        filters = Filters([Filter(authors=[pubkey], kinds=[1], limit=limit, since=since, until=until)])
        return await self.fetch_events(filters)

    async def react_to_event(self, event_id: str, reaction: str = "+") -> str:
        return await self.publish_event(kind=7, content=reaction, tags=[['e', event_id]])

    async def create_channel(self, name: str, about: str, picture: str = None, additional_metadata: Dict[str, str] = None) -> str:
        content = {
            "name": name,
            "about": about,
            "picture": picture,
            **(additional_metadata or {})
        }
        return await self.publish_event(kind=40, content=json.dumps(content))

    async def publish_channel_message(self, channel_id: str, content: str, reply_to: str = None) -> str:
        tags = [
            ["e", channel_id, "", "root"],
            ["p", self.public_key.hex()]
        ]
        if reply_to:
            tags.append(["e", reply_to, "", "reply"])
        return await self.publish_event(kind=42, content=content, tags=tags)

    async def fetch_channel_messages(self, channel_id: str, limit: int = 20, since: int = None, until: int = None) -> List[Event]:
        filters = Filters([Filter(kinds=[42], tags={'e': [channel_id]}, limit=limit, since=since, until=until)])
        return await self.fetch_events(filters)

    async def create_direct_message(self, recipient_pubkey: str, content: str) -> str:
        encrypted_content = encrypt_message(self.private_key.hex(), recipient_pubkey, content)
        return await self.publish_event(kind=4, content=encrypted_content, tags=[['p', recipient_pubkey]])

    async def fetch_direct_messages(self, pubkey: str = None, limit: int = 20) -> List[Event]:
        filters = Filters([Filter(kinds=[4], authors=[pubkey or self.public_key.hex()], limit=limit)])
        return await self.fetch_events(filters)

    async def create_long_form_content(self, title: str, content: str, summary: str = None, image: str = None, published_at: int = None) -> str:
        tags = [
            ['title', title],
            ['summary', summary] if summary else None,
            ['image', image] if image else None,
            ['published_at', str(published_at or int(time.time()))]
        ]
        tags = [tag for tag in tags if tag is not None]
        return await self.publish_event(kind=30023, content=content, tags=tags)

    async def fetch_long_form_content(self, pubkey: str = None, limit: int = 20) -> List[Event]:
        filters = Filters([Filter(kinds=[30023], authors=[pubkey or self.public_key.hex()], limit=limit)])
        return await self.fetch_events(filters)

    async def create_zap_request(self, event_id: str, amount: int, content: str = "") -> str:
        zap_request = create_zap_request(self.private_key.hex(), self.public_key.hex(), amount, content)
        zap_request.tags.append(['e', event_id])
        await publish_event(self.relay_manager, zap_request)
        return zap_request.id

    async def fetch_zap_requests(self, event_id: str = None, pubkey: str = None, limit: int = 20) -> List[Event]:
        filters = []
        if event_id:
            filters.append(Filter(kinds=[9734], tags={'e': [event_id]}, limit=limit))
        if pubkey:
            filters.append(Filter(kinds=[9734], tags={'p': [pubkey]}, limit=limit))
        return await self.fetch_events(Filters(filters))

    async def create_delegation(self, delegatee_pubkey: str, conditions: str, expiration: int) -> str:
        delegation_event = create_delegation_event(self.private_key.hex(), delegatee_pubkey, conditions, expiration)
        await publish_event(self.relay_manager, delegation_event)
        return delegation_event.id

    def close_connections(self):
        self.relay_manager.close_connections()

async def main():
    library = NostrLibrary(["wss://relay.damus.io", "wss://relay.nostr.info"])
    
    try:
        # Example usage
        profile_id = await library.update_user_profile("Alice", "Nostr enthusiast", "https://example.com/alice.jpg", {"website": "https://alice.com"})
        print(f"Updated profile: {profile_id}")
        
        note_id = await library.publish_text_note("Hello, #nostr world!", mentions=["32e1827635450ebb3c5a7d12c1f8e7b2b514439ac10a67eef3d9fd9c5c68e245"])
        print(f"Published note: {note_id}")
        
        user_notes = await library.fetch_user_notes(library.public_key.hex())
        print(f"Fetched {len(user_notes)} user notes")
        
        channel_id = await library.create_channel("Nostr Dev", "A channel for Nostr developers")
        print(f"Created channel: {channel_id}")
        
        message_id = await library.publish_channel_message(channel_id, "Welcome to the Nostr Dev channel!")
        print(f"Published channel message: {message_id}")
        
        dm_id = await library.create_direct_message("32e1827635450ebb3c5a7d12c1f8e7b2b514439ac10a67eef3d9fd9c5c68e245", "Hey, check out this new Nostr library!")
        print(f"Sent direct message: {dm_id}")
        
        article_id = await library.create_long_form_content("Introduction to Nostr", "Nostr is a decentralized social network...", "A beginner's guide to Nostr")
        print(f"Published long-form content: {article_id}")
        
        zap_request_id = await library.create_zap_request(note_id, 1000, "Great post!")
        print(f"Created zap request: {zap_request_id}")
        
        delegation_id = await library.create_delegation("32e1827635450ebb3c5a7d12c1f8e7b2b514439ac10a67eef3d9fd9c5c68e245", "kind=1&created_at<1679292300", 1679292300)
        print(f"Created delegation: {delegation_id}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        library.close_connections()

if __name__ == "__main__":
    asyncio.run(main())
