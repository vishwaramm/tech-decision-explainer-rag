import chromab
from app.models.document import DocumentChunk

class VectorStore:
    def __init__(self, collection_name: str):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )
    
    def add(self, chunks: list[DocumentChunk], embeddings: list[list[float]]):
        self.collection.add(
            ids=[c.id for c in chunks],
            documents=[c.text for c in chunks],
            metadatas=[
                {"Source": c.source, "section": c.section}
                for c in chunks
            ],
            embeddings=embeddings
        )
    
    def query(self, embedding: list[float], k: int = 5):
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )