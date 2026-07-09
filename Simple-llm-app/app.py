import os
from dotenv import load_dotenv

import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple-LLM-app"

# PROMPT
prompt = ChatPromptTemplate([
    ('system', 'You are a helpful ai assistant.'),
    ('human', 'Explain {topic} in simple terms.')
])

# STREAMLIT FRAMEWORK
st.title("Simple llm call using Ollama-models")
input_text = st.text_input("Ask Question")

# OLLAMA MODELS
model = ChatOllama(model="gemma4:31b-cloud")

# CHAIN
chain = prompt | model | StrOutputParser()


if input_text:
    st.write(chain.invoke({"topic" : input_text}))
