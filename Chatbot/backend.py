import os
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = HuggingFaceEndpoint(model="deepseek-ai/DeepSeek-V4-Pro")
model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly AI assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ]
)

chain = prompt | model

store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

def ask_bot(question, session_id):
    response = chatbot.invoke(
        {"question": question},
        config={
            "configurable": {
                "session_id": session_id
            }
        }
    )

    return response.content