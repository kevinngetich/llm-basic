from openai import OpenAI
from app.config import settings

def post_query(messages: list):
    client = OpenAI(
        base_url = settings.openrouter_base_url,
        api_key = settings.openrouter_api_key,
    )

    completion = client.chat.completions.create(
        model = settings.openrouter_model,
        messages = messages
    )

    return completion.choices[0].message.content