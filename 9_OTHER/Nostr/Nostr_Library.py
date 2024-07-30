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
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class NostrLibrary:
    def __init__(self, relays: List[str], private_key: Optional[str] = None):
        self.relay_manager = RelayManager()
        for relay in relays:
            self.relay_manager.add_relay(relay)
        self.relay_manager.open_connections()
        self.private_key = PrivateKey(private_key) if private_key else PrivateKey()
        self.public_key = self.private_key.public_key

    async def publish_event(self, kind: int, content: str, tags: List[List[str]] = None, pow_difficulty: int = 0) -> str:
        """
        Publish a Nostr event (NIP-01)
        
        :param kind: Event kind (integer)
        :param content: Event content (string)
        :param tags: Optional list of tags
        :param pow_difficulty: Optional proof-of-work difficulty (NIP-13)
        :return: Event ID (string)
        """
        event = Event(
            public_key=self.public_key.hex(),
            created_at=int(time.time()),
            kind=kind,
            tags=tags or [],
            content=content
        )
        event.sign(self.private_key.hex())
        
        if pow_difficulty > 0:
            event = create_pow_event(event, pow_difficulty)
        
        await self.relay_manager.publish_event(event)
        return event.id

    async def fetch_events(self, filters: Union[Filters, List[Filter]], timeout: float = 5.0) -> List[Event]:
        """
        Fetch events from relays (NIP-01)
        
        :param filters: Filters to apply
        :param timeout: Maximum time to wait for events
        :return: List of fetched events
        """
        if isinstance(filters, list):
            filters = Filters(filters)
        
        events = []
        async with self.relay_manager.subscribe(filters) as sub:
            async for event in sub:
                events.append(event)
                if time.time() - sub.started_at > timeout:
                    break
        return events

    async def fetch_user_profile(self, pubkey: str) -> Optional[Dict[str, Any]]:
        """
        Fetch a user's profile (NIP-01)
        
        :param pubkey: Public key of the user
        :return: User profile as a dictionary, or None if not found
        """
        filters = Filters([Filter(authors=[pubkey], kinds=[0], limit=1)])
        events = await self.fetch_events(filters)
        if events:
            return json.loads(events[0].content)
        return None

    async def update_user_profile(self, name: str, about: str, picture: str, additional_fields: Dict[str, str] = None) -> str:
        """
        Update user profile (NIP-01)
        
        :param name: User's name
        :param about: User's description
        :param picture: URL to user's profile picture
        :param additional_fields: Additional profile fields
        :return: Event ID of the profile update
        """
        content = {
            "name": name,
            "about": about,
            "picture": picture,
            **(additional_fields or {})
        }
        return await self.publish_event(kind=0, content=json.dumps(content))

    async def publish_text_note(self, content: str, reply_to: str = None, mentions: List[str] = None, tags: List[List[str]] = None) -> str:
        """
        Publish a text note (NIP-01)
        
        :param content: Note content
        :param reply_to: Optional ID of the note being replied to
        :param mentions: Optional list of mentioned public keys
        :param tags: Optional additional tags
        :return: Event ID of the published note
        """
        event_tags = []
        if reply_to:
            event_tags.append(['e', reply_to, '', 'reply'])
        if mentions:
            event_tags.extend([['p', mention] for mention in mentions])
        if tags:
            event_tags.extend(tags)
        return await self.publish_event(kind=1, content=content, tags=event_tags)

    async def fetch_user_notes(self, pubkey: str, limit: int = 20, since: int = None, until: int = None) -> List[Event]:
        """
        Fetch notes from a specific user (NIP-01)
        
        :param pubkey: Public key of the user
        :param limit: Maximum number of notes to fetch
        :param since: Fetch notes since this timestamp
        :param until: Fetch notes until this timestamp
        :return: List of fetched notes
        """
        filters = Filters([Filter(authors=[pubkey], kinds=[1], limit=limit, since=since, until=until)])
        return await self.fetch_events(filters)

    async def react_to_event(self, event_id: str, reaction: str = "+") -> str:
        """
        React to an event (NIP-25)
        
        :param event_id: ID of the event to react to
        :param reaction: Reaction content (default is "+")
        :return: Event ID of the reaction
        """
        return await self.publish_event(kind=7, content=reaction, tags=[['e', event_id]])

    async def create_channel(self, name: str, about: str, picture: str = None, additional_metadata: Dict[str, str] = None) -> str:
        """
        Create a new channel (NIP-28)
        
        :param name: Channel name
        :param about: Channel description
        :param picture: Optional URL to channel picture
        :param additional_metadata: Optional additional metadata
        :return: Event ID of the channel creation event
        """
        content = {
            "name": name,
            "about": about,
            "picture": picture,
            **(additional_metadata or {})
        }
        return await self.publish_event(kind=40, content=json.dumps(content))

    async def publish_channel_message(self, channel_id: str, content: str, reply_to: str = None) -> str:
        """
        Publish a message to a channel (NIP-28)
        
        :param channel_id: ID of the channel
        :param content: Message content
        :param reply_to: Optional ID of the message being replied to
        :return: Event ID of the published message
        """
        tags = [
            ["e", channel_id, "", "root"],
            ["p", self.public_key.hex()]
        ]
        if reply_to:
            tags.append(["e", reply_to, "", "reply"])
        return await self.publish_event(kind=42, content=content, tags=tags)

    async def fetch_channel_messages(self, channel_id: str, limit: int = 20, since: int = None, until: int = None) -> List[Event]:
        """
        Fetch messages from a channel (NIP-28)
        
        :param channel_id: ID of the channel
        :param limit: Maximum number of messages to fetch
        :param since: Fetch messages since this timestamp
        :param until: Fetch messages until this timestamp
        :return: List of fetched messages
        """
        filters = Filters([Filter(kinds=[42], tags={'e': [channel_id]}, limit=limit, since=since, until=until)])
        return await self.fetch_events(filters)

    async def create_direct_message(self, recipient_pubkey: str, content: str) -> str:
        """
        Create an encrypted direct message (NIP-04)
        
        :param recipient_pubkey: Public key of the recipient
        :param content: Message content
        :return: Event ID of the direct message
        """
        shared_secret = self._compute_shared_secret(recipient_pubkey)
        encrypted_content = self._encrypt_message(shared_secret, content)
        return await self.publish_event(kind=4, content=encrypted_content, tags=[['p', recipient_pubkey]])

    async def fetch_direct_messages(self, pubkey: str = None, limit: int = 20) -> List[Event]:
        """
        Fetch encrypted direct messages (NIP-04)
        
        :param pubkey: Optional public key to filter messages
        :param limit: Maximum number of messages to fetch
        :return: List of fetched encrypted messages
        """
        filters = Filters([Filter(kinds=[4], authors=[pubkey or self.public_key.hex()], limit=limit)])
        return await self.fetch_events(filters)

    async def create_long_form_content(self, title: str, content: str, summary: str = None, image: str = None, published_at: int = None) -> str:
        """
        Create long-form content (NIP-23)
        
        :param title: Content title
        :param content: Main content body
        :param summary: Optional content summary
        :param image: Optional image URL
        :param published_at: Optional publication timestamp
        :return: Event ID of the long-form content
        """
        tags = [
            ['title', title],
            ['summary', summary] if summary else None,
            ['image', image] if image else None,
            ['published_at', str(published_at or int(time.time()))]
        ]
        tags = [tag for tag in tags if tag is not None]
        return await self.publish_event(kind=30023, content=content, tags=tags)

    async def fetch_long_form_content(self, pubkey: str = None, limit: int = 20) -> List[Event]:
        """
        Fetch long-form content (NIP-23)
        
        :param pubkey: Optional public key to filter content
        :param limit: Maximum number of content items to fetch
        :return: List of fetched long-form content events
        """
        filters = Filters([Filter(kinds=[30023], authors=[pubkey or self.public_key.hex()], limit=limit)])
        return await self.fetch_events(filters)

    async def create_zap_request(self, event_id: str, amount: int, content: str = "") -> str:
        """
        Create a zap request (NIP-57)
        
        :param event_id: ID of the event to zap
        :param amount: Amount of sats to zap
        :param content: Optional zap comment
        :return: Event ID of the zap request
        """
        zap_request = Event(
            kind=9734,
            pubkey=self.public_key.hex(),
            created_at=int(time.time()),
            content=content,
            tags=[
                ['e', event_id],
                ['amount', str(amount)]
            ]
        )
        zap_request.sign(self.private_key.hex())
        await self.relay_manager.publish_event(zap_request)
        return zap_request.id

    async def fetch_zap_requests(self, event_id: str = None, pubkey: str = None, limit: int = 20) -> List[Event]:
        """
        Fetch zap requests (NIP-57)
        
        :param event_id: Optional event ID to filter zaps
        :param pubkey: Optional public key to filter zaps
        :param limit: Maximum number of zap requests to fetch
        :return: List of fetched zap request events
        """
        filters = []
        if event_id:
            filters.append(Filter(kinds=[9734], tags={'e': [event_id]}, limit=limit))
        if pubkey:
            filters.append(Filter(kinds=[9734], tags={'p': [pubkey]}, limit=limit))
        return await self.fetch_events(Filters(filters))

    async def create_delegation(self, delegatee_pubkey: str, conditions: str, expiration: int) -> str:
        """
        Create a delegation (NIP-26)
        
        :param delegatee_pubkey: Public key of the delegatee
        :param conditions: Delegation conditions
        :param expiration: Expiration timestamp
        :return: Event ID of the delegation
        """
        delegation_token = f"nostr:delegation:{self.public_key.hex()}:{conditions}:{expiration}"
        signature = self.private_key.sign(delegation_token.encode())
        
        delegation_event = Event(
            kind=1040,
            pubkey=self.public_key.hex(),
            created_at=int(time.time()),
            content="",
            tags=[
                ['d', 'delegation'],
                ['p', delegatee_pubkey],
                ['conditions', conditions],
                ['expiration', str(expiration)],
                ['sig', signature.hex()]
            ]
        )
        delegation_event.sign(self.private_key.hex())
        await self.relay_manager.publish_event(delegation_event)
        return delegation_event.id

    def _compute_shared_secret(self, recipient_pubkey: str) -> bytes:
        """Compute shared secret for NIP-04 encryption"""
        private_key = ec.derive_private_key(int(self.private_key.hex(), 16), ec.SECP256K1(), default_backend())
        public_key = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256K1(), bytes.fromhex(recipient_pubkey))
        shared_key = private_key.exchange(ec.ECDH(), public_key)
        return HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'',
            backend=default_backend()
        ).derive(shared_key)

    def _encrypt_message(self, shared_secret: bytes, message: str) -> str:
        """Encrypt message for NIP-04"""
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(shared_secret), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_message = message.encode() + b'\0' * (16 - (len(message) % 16))
        ciphertext = encryptor.update(padded_message) + encryptor.finalize()
        return base64.b64encode(iv + ciphertext).decode()

    def close_connections(self):
        """Close all relay connections"""
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
