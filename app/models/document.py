from pydantic import BaseModel
from typing import Dict

class DocumentChunk(BaseModel):
    id: str
    source: str
    section: str
    text: str
    metadata: Dict[str, str]