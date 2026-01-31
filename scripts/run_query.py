from app.ingestion.loaders import load_pep
from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_by_sections
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriever
from app.llm.client import embed_text
from app.pipelines.evidence_extract import extract_evidence

PEP_URL = "https://peps.python.org/pep-0572/"

def main():
    raw = load_pep(PEP_URL)
    cleaned = clean_text(raw)
    chunks = chunk_by_sections(cleaned, "PEP-572")
    store = VectorStore("tech-decisions")
    embeddings = [embed_text(c) for c in chunks]
    store.add(chunks, embeddings)
    
    retriever = Retriever(store)
    query = "Why was the walrus operator introduced?"
    results = retriever.retrieve(query)
    
    retrieved_chunks = [chunks[i] for i in results["ids"][0]]
    
    evidence = extract_evidence(query, chunks=retrieved_chunks)
    
    for e in evidence:
        print(e)
        
    if __name__ == "__main__":
        main()