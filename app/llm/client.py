import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# I isolate all probabilistic behavior behind a thin interface so pipelines stay testable.
client = OpenAI()

EMBEDDING_MODEL = api_key=os.getenv("OPENAI_MODEL_EMBED")
CHAT_MODEL = api_key=os.getenv("OPENAI_MODEL_CHAT")

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
    