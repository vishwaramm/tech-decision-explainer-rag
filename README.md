Why this separation matters

ingestion/ → deterministic, testable, LLM-free

retrieval/ → swappable vector DBs

llm/ → vendor-agnostic abstraction

pipelines/ → explicit reasoning stages

models/ → contract-first development

sources/ → raw truth

processed/ → normalized truth

embeddings/ → derived state

must have .env file:

OPENAI_API_KEY=
OPENAI_MODEL_CHAT=gpt-4o-mini
OPENAI_MODEL_EMBED=text-embedding-3-large
