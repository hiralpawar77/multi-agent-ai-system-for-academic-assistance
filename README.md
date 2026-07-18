# Multi-Agent AI System for Academic Assistance

A web-based AI-powered academic assistant that helps students with essays,
research, study tips, and academic questions using a multi-agent architecture.

---

## Project Structure

```
multi-agent-ai-system-for-academic-assistance/
│
├── README.md
│
├── data/
│   ├── README.md
│   ├── raw/                         ← Original datasets
│   └── cleaned/                     ← Preprocessed datasets
│
├── src/
│   ├── README.md
│   ├── app.py                       ← Flask backend server
│   ├── index.html                   ← Frontend chat interface
│   ├── architecture_diagram.py      ← Architecture diagram generator
│   └── data_cleaning.ipynb          ← Data cleaning notebook
│
├── reports/
│   ├── README.md
│   ├── architecture_diagram.png     ← System architecture diagram
│   ├── API_specification.md         ← API documentation
│   └── technical_report.md          ← Technical report
│
└── deployment/
    └── README.md
```

## System Architecture

The system consists of 4 layers:

- **Client Layer** — HTML/CSS/JavaScript frontend chat interface
- **Server Layer** — Python Flask backend with REST API endpoints
- **AI Model Layer** — Groq API (LLaMA 3) for generating responses
- **Database Layer** — In-memory storage for chat history and feedback

---

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| /api/health | GET | Check server status |
| /api/chat | POST | Send prompt to AI |
| /api/history | GET | Retrieve chat history |
| /api/users | GET | Fetch user information |
| /api/feedback | POST | Store user ratings |

---

## Tech Stack

- **Backend:** Python, Flask, Flask-CORS
- **Frontend:** HTML, CSS, JavaScript
- **AI Model:** Groq API (LLaMA 3 8B)
- **Data Processing:** Pandas, Jupyter Notebook
- **Version Control:** Git, GitHub

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-agent-ai-system-for-academic-assistance.git
cd multi-agent-ai-system-for-academic-assistance
```

2. Install dependencies:
```bash
pip install flask flask-cors groq
```

3. Add your Groq API key in `src/app.py`:
```python
client = Groq(api_key="your_key_here")
```

4. Start the server:
```bash
python src/app.py
```

5. Open `src/index.html` in your browser and start chatting!

---

## Weekly Progress

| Week | Tasks | Status |
|---|---|---|
| Week 1 | Project setup, data collection | ✅ Done |
| Week 2 | Data cleaning and preprocessing | ✅ Done |
| Week 3 | System design, backend, frontend, documentation | ✅ Done |

## Demo Video
[Watch the demo video here] https://youtu.be/i3tLdPjtJb4

---

## Author
Internship Project Group number 95 — U2U Internship Program
