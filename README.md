# AI Q&A Bot

A simple AI-powered chatbot built with Streamlit and OpenAI API.

## Features

- Interactive chat interface
- Conversation history
- Clean and simple UI
- Easy to deploy

## Prerequisites

- Python 3.9 or higher
- OpenAI API key

## Installation

1. Clone the repository

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
```
Then edit `.env` and add your OpenAI API key.

## Getting OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new secret key
5. Copy the key and paste it in your `.env` file

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at http://localhost:8501

## Project Structure

```
ai-qa-bot/
├── .env                    # API keys (not committed)
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── app.py                  # Main application
└── docs/                   # Documentation
    ├── REQUIREMENTS.md
    ├── TECHNICAL_SPECS.md
    └── STANDARDS.md
```

## Documentation

See the `docs/` folder for detailed documentation:
- Requirements Document
- Technical Specifications
- Coding Standards

## Technologies Used

- Python 3.9+
- Streamlit - Web UI framework
- OpenAI API - AI language model
- python-dotenv - Environment variable management

## Troubleshooting

**"Invalid API key" error:**
- Check that your `.env` file exists and contains a valid OpenAI API key
- Make sure there are no extra spaces in the key

**"Module not found" error:**
- Run `pip install -r requirements.txt` again
- Make sure your virtual environment is activated

## License

MIT License