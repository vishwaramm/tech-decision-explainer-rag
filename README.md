This project is intentionally structured to isolate deterministic logic from probabilistic behavior and to keep reasoning auditable.

**Core principles:**

* Deterministic code should be testable without an LLM
* Probabilistic behavior should be isolated and constrained
* Data should move through clear, inspectable stages

### Directory Responsibilities

* **`ingestion/`**
  Deterministic document loading, cleaning, and chunking.
  No LLM usage. Fully testable.

* **`retrieval/`**
  Vector store abstraction and retrieval logic.
  Designed to allow swapping databases without touching pipelines.

* **`llm/`**
  Thin, vendor-agnostic wrappers around LLMs and embeddings.
  All probabilistic behavior is isolated here.

* **`pipelines/`**
  Explicit multi-pass reasoning stages (evidence extraction, analysis, gap detection).
  No hidden chains or implicit behavior.

* **`models/`**
  Pydantic schemas defining strict input/output contracts.
  Enforces structure, validation, and abstention.

* **`data/sources/`**
  Raw, unmodified source documents (ground truth).

* **`data/processed/`**
  Cleaned, normalized text derived from sources.

* **`data/embeddings/`**
  Derived vector state used for retrieval (not committed).

---

## Preconditions

* Python **3.10+**
* macOS or Linux (Windows works with equivalent commands)

Verify Python version:

```bash
python3 --version
```

---

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS / Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### 3. Create environment file

```bash
cp .env.example .env
```

Edit `.env` and set the following:

```text
OPENAI_API_KEY=sk-xxxxxxxx
OPENAI_MODEL_CHAT=gpt-4o-mini
OPENAI_MODEL_EMBED=text-embedding-3-large
```

> **Note:** Never commit `.env` files.

---

## Sanity Check

Before running the full pipeline, confirm that embeddings work:

```bash
python -c "from app.llm.client import embed_text; print(len(embed_text('hello')))"
```

Expected output:

* A number (e.g. `3072`)
* No exceptions

If this fails, fix configuration before proceeding.

---

## Run the Full Pipeline

From the repository root:

```bash
PYTHONPATH=. python scripts/run_query.py
```

This will:

1. Load a public technical design document
2. Clean and chunk it
3. Embed and store chunks
4. Retrieve relevant context
5. Run Pass-1 evidence extraction

Empty output is valid and expected when no explicit rationale is found.
