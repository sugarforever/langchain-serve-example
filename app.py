#!/usr/bin/env python
from fastapi import FastAPI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)

system_message_prompt = SystemMessagePromptTemplate.from_template("""
    You are a helpful assistant that translates {input_language} to {output_language}.
""")
human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

add_routes(
    app,
    chat_prompt | ChatOpenAI(),
    path="/translate",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8888)