from typing import List
from app.model.document import DocumentChunk
import uuid

DECISION_SECTIONS = [
    "Motivation",
    "Rationale",
    "Specification",
    "Rejected Ideas",
    "Alternatives"
]
# I chunk by semantic intent, not token count, to preserve reasoning continuity.”
def chunk_by_sections(
    text: str,
    source: str
) -> List[DocumentChunk]:
    chunks = []
    current_section = "UNKNOWN"
    buffer = []
    
    for line in text.splitlines():
        if any(s.lower() in line.lower() for s in DECISION_SECTIONS):
            if buffer:
                chunks.append(
                    DocumentChunk(
                        id=str(uuid.uuid4()),
                        source=source,
                        section=current_section,
                        text="\n".join(buffer),
                        metadata={}
                    )
                )
                buffer=[]
                current_section=line.strip()
            else:
                buffer.append(line)
                
    if buffer:
        chunks.append(
            DocumentChunk(
                id=str(uuid.uuid4),
                source=source,
                section=current_section,
                text="\n".join(buffer),
                metadata={}
            )
        )
    return chunks