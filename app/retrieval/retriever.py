from app.retrieval.vector_store import VectorStore
from app.llm.client import embed_text

class Retriever:
    def __init__(self, store: VectorStore):
        self.store = store
        
    def retrieve(self, query: str):
        query_embedding = embed_text(query)
        return self.store.query(query_embedding)