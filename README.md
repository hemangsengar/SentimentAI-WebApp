# SentimentAI-WebApp

A Flask-based web application for performing sentiment analysis using Google's Generative AI. The app provides a user-friendly interface to analyze the sentiment of any given text.

## Features
- Sentiment analysis using Google's Generative AI.
- Interactive web interface with a modern design.
- Real-time sentiment analysis results.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- A valid Google API key for Generative AI

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SentimentAI-WebApp
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirement.txt
   ```

4. Set your Google API key as an environment variable:
   ```bash
   export GOOGLE_API_KEY="your-google-api-key"  # On Windows: set GOOGLE_API_KEY="your-google-api-key"
   ```

---

## Usage

1. Start the Flask server:
   ```bash
   python server.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Enter text in the input box and click "Analyze Sentiment" to get the sentiment analysis result.

---

## Project Structure

```
SentimentAI-WebApp/
├── AI.py                  # Handles interaction with Google's Generative AI
├── sentiment_analysis.py  # Contains the sentiment analysis logic
├── server.py              # Flask server setup
├── templates/
│   └── index.html         # Frontend HTML template
├── static/
│   └── mywebscript.js     # JavaScript for frontend interactivity
├── secret_settings.py     # Stores sensitive API keys
├── requirement.txt        # Python dependencies
└── .gitignore             # Files to ignore in version control
```

---

## API Endpoints

### `GET /`
- Renders the main web interface.

### `GET /sentimentAnalyzer`
- **Query Parameter**: `textToAnalyze` - The text to analyze.
- **Response**: Sentiment analysis result (label and confidence score).

---

## Dependencies
- Flask: Web framework for Python.
- google-generativeai: Library for interacting with Google's Generative AI.

Install all dependencies using:
```bash
pip install -r requirement.txt
```

---

## Notes
- Ensure your Google API key has the necessary permissions for Generative AI.
- For production, disable `debug` mode in `server.py`.

---

## License
This project is licensed under the MIT License.

