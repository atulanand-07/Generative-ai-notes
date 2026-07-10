import streamlit as st
from backend import ask_bot

st.set_page_config(page_title="Simple Chatbot")

st.title("🤖 Chatbot")

# Create UI history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Session ID for LangChain
if "session_id" not in st.session_state:
    st.session_state.session_id = "user1"

# Display old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call LangChain backend
    answer = ask_bot(
        user_input,
        st.session_state.session_id
    )

    # Store AI message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)