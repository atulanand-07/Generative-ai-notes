# Simple LangChain Chatbot with Streamlit

A beginner-friendly conversational AI chatbot built using **LangChain**,
**Hugging Face Inference API**, and **Streamlit**.

The project demonstrates how to build a chatbot with conversational
memory using `RunnableWithMessageHistory` and
`InMemoryChatMessageHistory`.

------------------------------------------------------------------------

## Features

-   Streamlit chat interface
-   Hugging Face hosted LLM (DeepSeek-V4-Pro)
-   LangChain Expression Language (LCEL)
-   Prompt templates using `ChatPromptTemplate`
-   Conversation memory with `RunnableWithMessageHistory`
-   Session-based chat history
-   Clean separation between frontend and backend

------------------------------------------------------------------------

## Project Structure

``` text
.
├── app.py          # Streamlit UI
├── backend.py      # LangChain chatbot logic
├── .env            # Hugging Face API token
└── README.md
```

------------------------------------------------------------------------

## Technologies Used

-   Python
-   Streamlit
-   LangChain
-   Hugging Face Inference API
-   python-dotenv

------------------------------------------------------------------------

## How It Works

### Frontend (`app.py`)

-   Creates the Streamlit chat interface.
-   Stores UI messages using `st.session_state`.
-   Maintains a session ID for each conversation.
-   Sends user questions to the backend.
-   Displays the model response.

### Backend (`backend.py`)

-   Loads the Hugging Face model.
-   Creates a chat prompt with:
    -   System message
    -   Chat history
    -   Current user message
-   Wraps the chain using `RunnableWithMessageHistory`.
-   Stores conversation history in `InMemoryChatMessageHistory`.
-   Returns the assistant response.

------------------------------------------------------------------------

## Conversation Flow

``` text
User
   │
   ▼
Streamlit UI
   │
   ▼
ask_bot(question, session_id)
   │
   ▼
RunnableWithMessageHistory
   │
   ├── Load previous history
   ├── Add current question
   └── Build prompt
   │
   ▼
DeepSeek-V4-Pro
   │
   ▼
Response
   │
   ▼
Store Human + AI messages
```

------------------------------------------------------------------------

## Memory Implementation

The chatbot uses:

-   `RunnableWithMessageHistory`
-   `InMemoryChatMessageHistory`

Each session ID has its own conversation history stored in memory.

Current implementation:

-   Stores the **entire conversation**
-   Automatically injects all previous messages into every prompt
-   History exists only while the application is running
-   History is lost when the application restarts

------------------------------------------------------------------------

## Current Limitation

This project is intentionally simple for learning purposes.

**Chat history is not currently managed or optimized.**

Every request sends the entire stored conversation back to the LLM. As
conversations become longer:

-   Prompt size increases
-   Latency increases
-   Token usage increases
-   Memory (RAM) usage grows
-   Eventually the application may hit the model/provider context limit

------------------------------------------------------------------------

## Possible Improvements

A production chatbot should manage conversation history using one or
more of the following techniques:

### 1. Sliding Window Memory

Keep only the most recent 10--20 conversation turns.

### 2. Conversation Summarization

Replace older messages with a concise summary while keeping recent
messages.

### 3. Retrieval-Augmented Memory (RAG)

Store long-term conversations in a vector database and retrieve only
relevant history.

### 4. Persistent Chat History

Replace `InMemoryChatMessageHistory` with a persistent backend such
as: - Redis - PostgreSQL - MongoDB - SQLite

### 5. Token-Based Trimming

Trim history based on token count instead of message count to stay
within the model's context window.

### 6. Hybrid Memory

Maintain: - Short-term memory (recent chat) - Long-term memory
(retrieved when needed)

### 7. Streaming Responses

Stream generated tokens for a better user experience.

------------------------------------------------------------------------

## Future Enhancements

-   Persistent user sessions
-   Authentication
-   Multiple conversations
-   Conversation summarization
-   RAG-based long-term memory
-   Streaming responses
-   File upload support
-   Tool calling / Agents
-   Chat history export

------------------------------------------------------------------------

## Learning Objective

This project focuses on understanding:

-   LangChain chat models
-   Prompt templates
-   Message history
-   Session management
-   Streamlit integration
-   Basic conversational AI architecture

It is intentionally kept simple before introducing production-grade
memory management techniques.
