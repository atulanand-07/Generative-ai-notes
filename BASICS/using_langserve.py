import os
from fastapi import FastAPI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from langserve import add_routes

from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="qwen/qwen3-32b", groq_api_key=api_key)

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

parser = StrOutputParser()

##create chain
chain = prompt | model | parser



## App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")

## Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)


# Run the code and try:-
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs#/
# http://127.0.0.1:8000/chain/playground/