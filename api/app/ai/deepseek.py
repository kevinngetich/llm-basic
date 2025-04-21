from openai import OpenAI
from app.config import settings

def post_query(messages: list):
    client = OpenAI(api_key=settings.deepseek_api_key, base_url=settings.deepseek_base_url)

    response = client.chat.completions.create(
        model = settings.deepseek_model,
        messages = messages,
        stream = False
    )

    return response.choices[0].message.content