from dataclasses import dataclass
from datetime import datetime

@dataclass
class BidSnapshot:
    value: float
    raw_text: str
    located_by: str
    timestamp: datetime