# CodeVerse: Kids' AI-Powered Coding Playground

**CodeVerse** is a fun and interactive coding platform for kids aged 5–14. It teaches programming through voice commands, funny AI feedback, and a game-like environment. This project is built using Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend.

## Features

- **Voice-to-Code**: Kids can speak simple programming commands, which are converted into Python code.
- **AI Error Comedy**: Friendly and funny messages when errors are encountered.
- **Web Interface**: Simple and playful UI for easy interaction.

## Project Structure

codeverse/
├── app.py # Main Flask app
├── ai_engine.py # Generates funny error messages
├── voice_to_code.py # Converts voice inputs to code
│
├── templates/
│ └── index.html # HTML frontend (rendered by Flask)
│
├── static/
│ ├── style.css # Styling for the web page
│ └── script.js # JavaScript for frontend logic
│
└── README.md # Project documentation
