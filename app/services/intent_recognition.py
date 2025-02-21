import openai
from ..core.config import settings


# OPENAI
openai.api_key = settings.OPENAI_API_KEY
model = settings.AI_MODEL

async def recognize_intent(text: str)->str:
    prompt=f"What is the intent of this user input: '{text}'? Return only the intent name."
    response = openai.chat.completions.create(
        model=model,
        messages =[{"role":"system","content":prompt}]
    )

    return response["choices"][0]["message"]["content"]