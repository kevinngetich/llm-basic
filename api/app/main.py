from fastapi import FastAPI
from pydantic import BaseModel
from .ai import deepseek
from .ai import openrouter

app = FastAPI()

class AIQuery(BaseModel):
    messages: list

@app.get("/")
def index():
    return {"Hello": "POST on '/ai/deepseek/post_query'"}

@app.post("/ai/deepseek/post_query")
def query_deepseek(query: AIQuery):
    result = deepseek.post_query(query.messages)
    return result

@app.post("/ai/openrouter/deepseek/post_query")
def query_openrouter_deepseek(query: AIQuery):
    result = openrouter.post_query(query.messages)
    return result
