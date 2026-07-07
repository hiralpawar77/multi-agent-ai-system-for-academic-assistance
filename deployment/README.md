this folder contains deployment files like Dockerfile and deployment scripts.

# Deployment

This folder contains deployment instructions and configuration.

## How to Deploy Locally

1. Clone the repository
2. Install dependencies:
```bash
pip install flask flask-cors groq
```
3. Set your Groq API key in `src/app.py`
4. Run the server:
```bash
python src/app.py
```
5. Open `src/index.html` in your browser

## Requirements
- Python 3.8+
- pip packages: flask, flask-cors, groq