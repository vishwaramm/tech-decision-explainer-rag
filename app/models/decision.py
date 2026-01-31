from pydantic import BaseModel
from typing import List, Literal

class RationalEvidence(BaseModel):
    category: Literal[
        "PERFORMANCE",
        "SAFETY",
        "COMPLEXITY",
        "ERGONOMICS",
        "OTHER"
    ]
    quote: str
    source: str
    section: str
    
class TechnicalDecision(BaseModel):
    decision: str
    rationale: List[RationalEvidence]
    alternatives_considered: List[str]
    known_tradeoffs: List[str]
    confidence: float