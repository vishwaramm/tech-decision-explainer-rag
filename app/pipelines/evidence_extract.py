import json
from typing import List
from app.llm.client import chat_completion
from app.llm.prompts import EVIDENCE_EXTRACTION_SYSTEM
from app.models.document import DocumentChunk
from app.models.decision import RationalEvidence

"""
    You deliberately:
    - Separate retrieval from reasoning
    - Force verbatim quotes
    - Avoid “summarize why” (hallucination magnet)
    - Validate against a schema
"""

def extract_evidence(
    query: str,
    chunks: List[DocumentChunk]
) -> List[RationalEvidence]:
    
    context = "\n\n".join(
        f"Section {c.section}\n{c.text}"
        for c in chunks
    )
    
    user_prompt = f"""
    Question:
    {query}
    
    Context:
    {context}
    
    Task:
    Extract all statements that explicitly explain WHY a decision was made.
    
    Return JSON in this format:
    [
        {{
            "category": "PERFORMANCE | SAFETY | COMPLEXITY | ERGONOMICS | OTHER",
            "quote": "...",
            "source": "{chunks[0].source}",
            "section": "..."
        }}
    ]
    """
    
    raw = chat_completion(
        system_prompt=EVIDENCE_EXTRACTION_SYSTEM,
        user_prompt=user_prompt,
        temperature=0.0
    )
    
    try:
        data = json.loads(raw)
        return [RationalEvidence(**item) for item in data]
    except Exception as e:
        raise ValueError(f"Invalid LLM Output: {raw}") from e