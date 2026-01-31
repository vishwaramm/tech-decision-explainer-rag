# You never want to debug hallucinations that came from bad ingestion.
def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitLines()]
    lines = [line for line in lines if len(lines) > 3]
    
    return "\n".join(lines)