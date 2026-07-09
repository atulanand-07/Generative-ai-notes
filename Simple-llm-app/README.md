# Simple LLM App

A simple Streamlit application for interacting with Large Language Models (LLMs) using LangChain.

## Overview

This application provides a simple web interface for querying various LLMs through LangChain. Currently configured to work with Ollama models, but can be easily adapted to work with other LLM providers supported by LangChain.

## Features

- Streamlit-based web interface
- Integration with LangChain for LLM interactions
- Configurable prompt templates
- Support for Ollama models (configurable for other providers)
- Simple question-answer interface

## Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd Simple-llm-app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r ../../requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory (one level up from this folder) with your API keys:
   ```
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_PROJECT=Simple-LLM-app
   ```
   
   For Ollama, make sure you have Ollama installed and running locally with the desired model:
   ```bash
   ollama pull gemma4:31b-cloud
   ```

## Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Use the interface**:
   - Enter your question in the text input field
   - The app will send your question to the configured LLM
   - View the response displayed below the input

## Configuration

### Model Configuration
In `app.py`, you can change the model being used:
```python
model = ChatOllama(model="gemma4:31b-cloud")
```
Replace `"gemma4:31b-cloud"` with any model available in your Ollama installation or switch to a different LangChain LLM provider.

### Prompt Customization
The prompt template can be modified in `app.py`:
```python
prompt = ChatPromptTemplate([
    ('system', 'You are a helpful ai assistant.'),
    ('human', 'Explain {topic} in simple terms.')
])
```

## Requirements

See the root `requirements.txt` file for all dependencies. Key packages include:
- `streamlit` - Web application framework
- `langchain` - Framework for LLM applications
- `langchain-ollama` - Ollama integration for LangChain
- `python-dotenv` - Environment variable management

## How It Works

1. User enters a question in the Streamlit text input
2. The input is formatted according to the prompt template
3. The formatted prompt is sent to the LLM via LangChain
4. The LLM response is parsed and displayed in the Streamlit interface

## Customization Ideas

- Add model selection dropdown in the UI
- Implement chat history
- Add parameters controls (temperature, max tokens, etc.)
- Support for multiple LLM providers
- Add file upload capabilities for context-aware queries

## Troubleshooting

- **Model not found**: Ensure you have pulled the model in Ollama (`ollama pull <model-name>`)
- **Connection errors**: Make sure Ollama is running (`ollama serve`)
- **API key issues**: Verify your `.env` file is correctly set up in the project root
- **Streamlit port conflicts**: Use `streamlit run app.py --server.port=<port-number>` to specify a different port

## License

This project is part of the Generative-ai-notes repository. Please see the root repository for licensing information.