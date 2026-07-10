import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly AI assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ]
)

parser = StrOutputParser()
chain = prompt | llm | parser

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

print("Simple Chatbot")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = chatbot.invoke(
        {"question": question},
        config={
            "configurable": {
                "session_id": "user1"
            }
        }
    )

    print("Bot:", response)