import os
from openai import OpenAI

# I isolate all probabilistic behavior behind a thin interface so pipelines stay testable.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDING_MODEL = "text-embedding-3-large"
CHAT_MODEL = "gpt-4o-mini"

def embed_text(text: str) -> list[float]:
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding

def chat_completion(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.0
) -> str:
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    
    return response.choices[0].message.content
    