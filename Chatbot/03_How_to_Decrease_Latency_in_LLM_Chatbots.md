# How to Decrease Latency in an LLM Chatbot

Latency in an LLM chatbot comes from several places:

1.  Prompt construction
2.  Network transfer
3.  Model inference
4.  Response generation

The biggest contributor in most conversational chatbots is the **amount
of text sent to the model**.

------------------------------------------------------------------------

## 1. Reduce Chat History ⭐⭐⭐⭐⭐ (Most Effective)

Instead of sending the entire conversation every time, send only the
most recent messages.

**Instead of:**

``` text
Message 1
Message 2
...
Message 100
```

**Send:**

``` text
Last 10–20 messages
```

### Benefits

-   Smaller prompt
-   Lower latency
-   Lower token usage
-   Faster inference

------------------------------------------------------------------------

## 2. Summarize Older Conversations ⭐⭐⭐⭐⭐

When conversations become long, summarize older messages instead of
keeping every message.

**Instead of:**

``` text
100 messages
```

**Use:**

``` text
Summary:
- User is building a LangChain chatbot.
- User prefers Hugging Face models.
- User asked about conversational memory.

Recent Messages:
...
```

### Benefits

-   Keeps important information
-   Greatly reduces context size
-   Improves response speed

------------------------------------------------------------------------

## 3. Use RAG Instead of Huge Chat History ⭐⭐⭐⭐

Store previous conversations in a vector database.

When the user asks a question:

``` text
Stored Chats
      ↓
Vector Database
      ↓
Retrieve Top 3–5 Relevant Chunks
      ↓
Send Only Those to the LLM
```

### Benefits

-   Very small prompts
-   Better scalability
-   Efficient long-term memory

------------------------------------------------------------------------

## 4. Use a Faster Model ⭐⭐⭐⭐

Some models are optimized for speed.

Examples: - Llama 3.1 8B - Qwen 3 8B - Gemini Flash - GPT-4.1 mini

Large reasoning models usually take longer to generate responses.

------------------------------------------------------------------------

## 5. Reduce `max_new_tokens`

If your application only needs short responses, don't allow thousands of
output tokens.

Instead of:

``` python
max_new_tokens = 4096
```

Use something like:

``` python
max_new_tokens = 256
```

### Benefits

-   Shorter generation time
-   Lower cost

------------------------------------------------------------------------

## 6. Stream Responses ⭐⭐⭐⭐

Instead of waiting for the full answer:

``` text
10 seconds...
Entire response appears
```

Stream tokens as they are generated:

``` text
H
He
Hel
Hello...
```

### Benefits

-   Better user experience
-   Faster perceived latency

------------------------------------------------------------------------

## 7. Use Better Hardware or a Faster Provider ⭐⭐⭐⭐

The same model can perform very differently depending on where it is
hosted.

Examples: - Dedicated GPU endpoint - Serverless endpoint - Local GPU -
CPU

Dedicated GPU endpoints usually provide much lower latency.

------------------------------------------------------------------------

## 8. Reduce Retrieved RAG Documents

Instead of retrieving many documents:

``` text
Top 20 documents
```

Retrieve only:

``` text
Top 3–5 documents
```

### Benefits

-   Smaller prompts
-   Faster inference
-   Better focus

------------------------------------------------------------------------

## 9. Cache Repeated Responses

Frequently asked questions can be answered from a cache instead of
calling the LLM.

Example:

    "What is Python?"

If already cached, return the cached response immediately.

### Benefits

-   Near-instant responses
-   Reduced API usage
-   Lower cost

------------------------------------------------------------------------

## 10. Optimize Your System Prompt

Avoid unnecessarily long system prompts.

Instead of:

``` text
(500-word system prompt)
```

Use:

``` text
You are a helpful AI assistant.
```

### Benefits

-   Smaller context
-   Faster processing

------------------------------------------------------------------------

## 11. Parallelize Independent Tasks

If your application performs multiple independent operations, run them
simultaneously.

``` text
User Question
      │
      ├── Retrieve Documents
      ├── Database Lookup
      └── Fetch User Profile
           (parallel)
      │
      ▼
Combine Results
      ▼
LLM
```

### Benefits

-   Reduces preprocessing time
-   Improves overall latency

------------------------------------------------------------------------

# Best Practices for Your Current Chatbot

Your current pipeline is:

``` text
User
  ↓
Entire Chat History
  ↓
Prompt
  ↓
DeepSeek-V4-Pro
  ↓
Answer
```

As the conversation grows, latency increases because more history is
sent with every request.

## Recommended Improvements

1.  Keep only the last 10--20 conversation turns.
2.  Summarize older conversations.
3.  Stream responses to improve perceived speed.
4.  Use a faster model when possible.
5.  Retrieve only relevant information using RAG.
6.  Keep prompts concise.
7.  Cache repeated responses.
8.  Parallelize independent preprocessing tasks.

------------------------------------------------------------------------

## Priority Order

| Priority | Technique | Impact |
|:--------:|-----------|--------|
| ⭐⭐⭐⭐⭐ | Reduce chat history | Very High |
| ⭐⭐⭐⭐⭐ | Summarize conversations | Very High |
| ⭐⭐⭐⭐ | Stream responses | High |
| ⭐⭐⭐⭐ | Use a faster model | High |
| ⭐⭐⭐⭐ | Use RAG | High |
| ⭐⭐⭐ | Reduce retrieved documents | Medium |
| ⭐⭐⭐ | Optimize prompts | Medium |
| ⭐⭐⭐ | Cache responses | Medium |
| ⭐⭐ | Better hardware/provider | Depends on deployment |
| ⭐⭐ | Parallelize preprocessing | Depends on workflow |

------------------------------------------------------------------------

## Key Takeaway

For most production chatbots, the biggest latency improvements come
from:

1.  Sending less context.
2.  Summarizing old conversations.
3.  Retrieving only relevant information with RAG.
4.  Streaming responses.
5.  Choosing an appropriately fast model.

These techniques keep latency low while maintaining response quality.
