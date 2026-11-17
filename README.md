# Voice Assistant

A small Flask web application that sends questions to Google Gemini and translates responses into the selected language.

## Features

- Gemini-powered question answering
- Response translation with `googletrans`
- Simple browser interface
- Configuration through environment variables

## Setup

```bash
git clone https://github.com/rithick2006/Voice-assistent.git
cd Voice-assistent
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -r requirements.txt
cp .env.example .env
```

Set `GEMINI_API_KEY` in `.env`, then start the server:

```bash
flask --app app run
```

Open <http://127.0.0.1:5000> in a browser.

## Security

Never commit `.env` or API keys. The application reads `GEMINI_API_KEY` from the environment and returns a safe error when it is missing.

## Status

Portfolio prototype. Add authentication, rate limiting, automated tests, and a production WSGI server before public deployment.
