import asyncio
import json
from typing import List, Dict, Optional, Union
from nostr.event import Event
from nostr.key import PrivateKey
from nostr.filter import Filter, Filters
from nostr.message_type import ClientMessageType
import time
from Helpful_Nostr import create_event, publish_event, subscribe_to_events, setup_relay_manager, create_filter
from dataclasses import dataclass, asdict
from enum import Enum, auto

class ThreatType(Enum):
    PHISHING = auto()
    MALWARE = auto()
    DDOS = auto()
    SOCIAL_ENGINEERING = auto()
    OTHER = auto()

class ModerationAction(Enum):
    HIDE = "hide"
    FLAG = "flag"
    REMOVE = "remove"

@dataclass
class ThreatReport:
    threat_type: ThreatType
    description: str
    severity: int
    indicators: List[str]

@dataclass
class TrustScore:
    score: float
    reason: str

@dataclass
class ContentModeration:
    action: ModerationAction
    reason: str

@dataclass
class ReputationUpdate:
    reputation_change: float
    reason: str

@dataclass
class NetworkAnalysis:
    analysis_type: str
    results: Dict
    timestamp: int

class NostrCogSec:
    def __init__(self, relays: List[str]):
        self.relay_manager = setup_relay_manager(relays)
        self.private_key = PrivateKey()
        self.public_key = self.private_key.public_key.hex()

    async def publish_event(self, kind: int, content: Union[str, Dict], tags: List[List[str]] = None) -> str:
        if isinstance(content, dict):
            content = json.dumps(content)
        event = create_event(
            private_key=self.private_key.hex(),
            kind=kind,
            content=content,
            tags=tags or []
        )
        await publish_event(self.relay_manager, event)
        return event.id

    async def fetch_events(self, filters: Filters) -> List[Event]:
        return await subscribe_to_events(self.relay_manager, filters)

    async def publish_threat_report(self, report: ThreatReport) -> str:
        content = asdict(report)
        content['type'] = 'threat_report'
        tags = [
            ["t", "threat_report"],
            ["severity", str(report.severity)],
            ["k", "cogsec"],
            ["k", "threat"]
        ]
        return await self.publish_event(kind=30078, content=content, tags=tags)

    async def fetch_threat_reports(self, severity: Optional[int] = None, limit: int = 20) -> List[Event]:
        filters = [create_filter(kinds=[30078], limit=limit, tags={'t': ['threat_report']})]
        if severity is not None:
            filters[0].tags['severity'] = [str(severity)]
        return await self.fetch_events(Filters(filters))

    async def publish_trust_score(self, target_pubkey: str, trust_score: TrustScore) -> str:
        content = asdict(trust_score)
        content['type'] = 'trust_score'
        tags = [
            ["p", target_pubkey],
            ["t", "trust_score"],
            ["k", "cogsec"],
            ["k", "trust"]
        ]
        return await self.publish_event(kind=30079, content=content, tags=tags)

    async def fetch_trust_scores(self, pubkey: str, limit: int = 20) -> List[Event]:
        filters = Filters([create_filter(kinds=[30079], tags={'p': [pubkey], 't': ['trust_score']}, limit=limit)])
        return await self.fetch_events(filters)

    async def publish_content_moderation(self, event_id: str, moderation: ContentModeration) -> str:
        content = asdict(moderation)
        content['type'] = 'content_moderation'
        tags = [
            ["e", event_id],
            ["t", "content_moderation"],
            ["k", "cogsec"],
            ["k", "moderation"]
        ]
        return await self.publish_event(kind=30080, content=content, tags=tags)

    async def fetch_content_moderations(self, event_id: str, limit: int = 20) -> List[Event]:
        filters = Filters([create_filter(kinds=[30080], tags={'e': [event_id], 't': ['content_moderation']}, limit=limit)])
        return await self.fetch_events(filters)

    async def publish_reputation_update(self, target_pubkey: str, update: ReputationUpdate) -> str:
        content = asdict(update)
        content['type'] = 'reputation_update'
        tags = [
            ["p", target_pubkey],
            ["t", "reputation_update"],
            ["k", "cogsec"],
            ["k", "reputation"]
        ]
        return await self.publish_event(kind=30081, content=content, tags=tags)

    async def fetch_reputation_updates(self, pubkey: str, limit: int = 20) -> List[Event]:
        filters = Filters([create_filter(kinds=[30081], tags={'p': [pubkey], 't': ['reputation_update']}, limit=limit)])
        return await self.fetch_events(filters)

    async def publish_network_analysis(self, analysis: NetworkAnalysis) -> str:
        content = asdict(analysis)
        content['type'] = 'network_analysis'
        tags = [
            ["t", "network_analysis"],
            ["analysis_type", analysis.analysis_type],
            ["k", "cogsec"],
            ["k", "network"]
        ]
        return await self.publish_event(kind=30082, content=content, tags=tags)

    async def fetch_network_analyses(self, analysis_type: Optional[str] = None, limit: int = 20) -> List[Event]:
        filters = [create_filter(kinds=[30082], tags={'t': ['network_analysis']}, limit=limit)]
        if analysis_type:
            filters[0].tags['analysis_type'] = [analysis_type]
        return await self.fetch_events(Filters(filters))

    async def verify_event_signature(self, event: Event) -> bool:
        return event.verify()

    def close_connections(self):
        self.relay_manager.close_connections()

async def main():
    cogsec = NostrCogSec(["wss://relay.damus.io", "wss://relay.nostr.info"])
    
    # Example usage
    threat_report = ThreatReport(
        threat_type=ThreatType.PHISHING,
        description="New phishing campaign targeting Nostr users",
        severity=8,
        indicators=["nostr:npub1abc123...", "https://malicious-site.com"]
    )
    threat_report_id = await cogsec.publish_threat_report(threat_report)
    print(f"Published threat report: {threat_report_id}")
    
    trust_score = TrustScore(
        score=0.85,
        reason="Consistent high-quality content and positive community interactions"
    )
    trust_score_id = await cogsec.publish_trust_score(
        "32e1827635450ebb3c5a7d12c1f8e7b2b514439ac10a67eef3d9fd9c5c68e245",
        trust_score
    )
    print(f"Published trust score: {trust_score_id}")
    
    moderation = ContentModeration(
        action=ModerationAction.HIDE,
        reason="Spam content"
    )
    moderation_id = await cogsec.publish_content_moderation(
        "1a2b3c4d5e6f7g8h9i0j...",
        moderation
    )
    print(f"Published content moderation: {moderation_id}")
    
    reputation_update = ReputationUpdate(
        reputation_change=0.05,
        reason="Helpful contribution to community discussion"
    )
    reputation_update_id = await cogsec.publish_reputation_update(
        "32e1827635450ebb3c5a7d12c1f8e7b2b514439ac10a67eef3d9fd9c5c68e245",
        reputation_update
    )
    print(f"Published reputation update: {reputation_update_id}")
    
    network_analysis = NetworkAnalysis(
        analysis_type="cluster_detection",
        results={"clusters": [["pubkey1", "pubkey2"], ["pubkey3", "pubkey4"]]},
        timestamp=int(time.time())
    )
    network_analysis_id = await cogsec.publish_network_analysis(network_analysis)
    print(f"Published network analysis: {network_analysis_id}")
    
    cogsec.close_connections()

if __name__ == "__main__":
    asyncio.run(main())
