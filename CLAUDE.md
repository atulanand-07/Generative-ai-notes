# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains notes and examples for working with Generative AI technologies, particularly focusing on LangChain and various LLM providers. It includes:

- Experimental notebooks demonstrating LLM usage
- A simple Streamlit LLM application
- Requirements for various LLM integrations

## Key Directories

- `Simple-llm-app/` - Contains a Streamlit-based LLM application
- `tests.ipynb` - Jupyter notebook demonstrating LLM usage with Ollama

## Key Files

- `requirements.txt` - Lists all Python dependencies for LLM integrations
- `.env` - Environment variables file (likely contains API keys)
- `Simple-llm-app/app.py` - Streamlit application for LLM interactions

## Dependencies

The project uses the following key libraries:
- `langchain` and `langchain-core` - Core LangChain framework
- `langchain-ollama` - Integration with Ollama LLMs
- `langchain-google-genai` - Integration with Google's Gemini models
- `langchain-huggingface` - Integration with Hugging Face models
- `google-generativeai` - Direct Google Gemini access
- `transformers` and `huggingface-hub` - Hugging Face transformers
- `streamlit` - For building the web interface
- `python-dotenv` - For environment variable management
- `numpy` - Numerical computations
- `ipykernel` - For Jupyter notebook support

## Development Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Streamlit App
```bash
streamlit run Simple-llm-app/app.py
```

### Run Tests/Notebooks
```bash
jupyter notebook tests.ipynb
# or
jupyter lab tests.ipynb
```

### Environment Setup
1. Copy `.env.example` to `.env` (if it exists) or create a new `.env` file
2. Add required API keys:
   - For Ollama: Ensure Ollama is running locally with desired models
   - For Google Gemini: Add `GOOGLE_API_KEY`
   - For Hugging Face: Add `HUGGINGFACEHUB_API_TOKEN`

## Key Features

### Simple LLM App (`Simple-llm-app/app.py`)
- Streamlit-based interface for interacting with LLMs
- Supports multiple LLM providers via LangChain
- Configurable model selection
- Basic chat interface

### Tests Notebook (`tests.ipynb`)
- Demonstrates basic usage of ChatOllama with Gemma model
- Shows how to set up prompts, models, and output parsers
- Example of simple question-answering with LLMs

## Common Development Tasks

### Adding New LLM Providers
1. Add the required package to `requirements.txt`
2. Install dependencies: `pip install -r requirements.txt`
3. Import the appropriate LangChain integration
4. Update the model selection in the Streamlit app if applicable

### Running Experiments
1. Create a new Jupyter notebook or modify `tests.ipynb`
2. Import desired LangChain components
3. Follow patterns shown in existing examples
4. Ensure required API keys are in `.env`

### Deploying the Streamlit App
1. Ensure all dependencies are installed
2. Set required environment variables
3. Run: `streamlit run Simple-llm-app/app.py`
4. Access via browser at http://localhost:8501

## Best Practices

1. **Environment Management**: Use the `.env` file for API keys and never commit it to version control
2. **Dependency Management**: Keep `requirements.txt` updated when adding new packages
3. **Experimentation**: Use Jupyter notebooks for trying new approaches before integrating into the main app
4. **Model Selection**: When experimenting with different LLMs, consider resource requirements (especially for local models)
5. **Error Handling**: LLM APIs can fail; implement appropriate error handling in applications

## Troubleshooting

### Common Issues
- **ModuleNotFoundError**: Run `pip install -r requirements.txt` to install missing dependencies
- **API Key Errors**: Check that required API keys are set in `.env` file
- **Ollama Connection Issues**: Ensure Ollama service is running (`ollama serve`) and desired model is pulled (`ollama pull <model>`)
- **Streamlit Port Conflicts**: Change port with `streamlit run --server.port=8501 app.py`

### Getting Help
- LangChain documentation: https://python.langchain.com/
- Streamlit documentation: https://docs.streamlit.io/
- Specific provider documentation linked in requirements.txt