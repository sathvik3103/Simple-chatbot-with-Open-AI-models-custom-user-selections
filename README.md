# OpenAI Q&A Chatbot with Custom Selections

A Streamlit-based web application that allows users to interact with OpenAI's language models through a customizable interface.

## Features

- Interactive chat interface with OpenAI models
- Customizable model parameters
- Secure API key handling
- Model selection options
- Adjustable temperature and token settings

## Installation

```bash
pip install -r requirements.txt
```

## Required Dependencies

- streamlit
- openai
- langchain-openai
- python-dotenv

## Environment Setup

Create a `.env` file in the root directory with the following variables:

```plaintext
OPENAI_API_KEY=your_api_key_here
LANGCHAIN_API_KEY=your_langchain_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Configure the settings in the sidebar:
   - Enter your OpenAI API key
   - Select an OpenAI model
   - Adjust temperature (0.0-1.0)
   - Set maximum tokens (50-500)

3. Enter your question in the main interface and receive AI-generated responses

## Model Options

| Model | Description |
|-------|------------|
| gpt-4o | Standard GPT-4 model |
| gpt-4-turbo | Faster GPT-4 variant |
| gpt-4o-mini | Lightweight GPT-4 version |

## Project Structure

```plaintext
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## Configuration

The application uses LangChain for enhanced tracking and monitoring:
- LangSmith tracking enabled
- Project name: "Simple chatbot with custom selections using OpenAI"
- Customizable temperature and token settings
- Secure API key handling through environment variables

## Error Handling

- Validates API key presence
- Ensures user input before generating responses
- Provides clear feedback for missing inputs

Example output for reference:
![Example Output for reference](https://github.com/user-attachments/assets/c2d70073-6e40-4991-9add-674b85919e0e)



Langsmith Project Tracking:
![Langsmith project tracking](https://github.com/user-attachments/assets/8ea5e0e8-098a-4883-9fe7-424fd825df0b)


