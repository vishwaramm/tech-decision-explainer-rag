Why this separation matters

ingestion/ → deterministic, testable, LLM-free

retrieval/ → swappable vector DBs

llm/ → vendor-agnostic abstraction

pipelines/ → explicit reasoning stages

models/ → contract-first development

sources/ → raw truth

processed/ → normalized truth

embeddings/ → derived state

Preconditions
you should have python 3.10+

run the following:
python3 --version
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux

pip install -r requirements.txt

# create .env file
cp .env.example .env

# edit .env file
OPENAI_API_KEY=sk-xxxxxxxx
OPENAI_MODEL_CHAT=gpt-4o-mini
OPENAI_MODEL_EMBED=text-embedding-3-large

# check if it works
python -c "from app.llm.client import embed_text; print(len(embed_text('hello')))"

# run the full pipeline
PYTHONPATH=. python scripts/run_query.py


