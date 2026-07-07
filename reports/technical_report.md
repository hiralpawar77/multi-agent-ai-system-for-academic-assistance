# Technical Report
## Multi-Agent AI System for Academic Assistance

---

## 1. Introduction

This project develops a web-based multi-agent AI system designed to assist
students with academic tasks. The system allows students to interact with an
AI assistant through a chat interface, receiving help with essays, research,
study tips, and academic questions.

---

## 2. System Architecture

The system follows a client-server architecture with 4 layers:

### 2.1 Client Layer
- Built using HTML, CSS, and JavaScript
- Provides a chat interface for students
- Features include: message input, response display, loading indicators,
  and a star rating system for feedback

### 2.2 Server Layer
- Built using Python and Flask
- Handles all incoming requests from the frontend
- Implements REST API endpoints
- Manages chat history and user feedback in memory

### 2.3 AI Model Layer
- Uses Groq API with LLaMA 3 8B model
- Processes student questions and generates academic responses
- Maintains conversation context for follow-up questions
- Configured with a system prompt focused on academic assistance

### 2.4 Data Layer
- Contains raw and cleaned academic datasets
- Data was collected and preprocessed in Weeks 1 and 2
- Stored in CSV/Excel format in the data/ directory

---

## 3. API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| /api/health | GET | Check server status |
| /api/chat | POST | Send prompt to AI and receive response |
| /api/history | GET | Retrieve past conversations |
| /api/users | GET | Fetch user information |
| /api/feedback | POST | Store user ratings and comments |

---

## 4. Frontend Interface

The frontend chat interface includes:

- **Header** — Displays system name and live server status
- **Welcome Screen** — Shows suggested questions for new users
- **Chat Window** — Displays conversation with user and AI bubbles
- **Loading Indicator** — Animated dots while waiting for AI response
- **Input Area** — Text box with send button and keyboard shortcuts
- **Feedback System** — Star rating below each AI response

---

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Backend programming language |
| Flask | Web framework for REST API |
| Flask-CORS | Handle cross-origin requests |
| Groq API | AI model integration |
| LLaMA 3 8B | Large language model |
| HTML/CSS/JS | Frontend interface |
| Pandas | Data processing |
| Jupyter Notebook | Data cleaning and analysis |
| Git/GitHub | Version control |

---

## 6. Weekly Progress

### Week 1 — Data Collection
- Set up project repository on GitHub
- Collected academic datasets
- Organized raw data in data/raw/ directory

### Week 2 — Data Cleaning
- Cleaned and preprocessed collected datasets
- Removed duplicates and handled missing values
- Saved cleaned data in data/cleaned/ directory
- Documented process in data_cleaning.ipynb

### Week 3 — Design and Development
- Studied AI client-server architecture
- Designed and documented 5 REST API endpoints
- Built Flask backend server with all endpoints
- Built frontend chat interface
- Integrated Groq AI for real responses
- Organized GitHub repository
- Prepared technical report and documentation

---

## 7. Challenges and Solutions

| Challenge | Solution |
|---|---|
| AI responses showing as plain text | Added markdown-to-HTML formatter in JavaScript |
| Frontend not connecting to backend | Added Flask-CORS to allow cross-origin requests |
| Responses losing context | Passed last 10 messages as history to AI in every request |

---

## 8. Results

The system successfully:
- Accepts student questions through a clean chat interface
- Sends questions to the Groq AI model via Flask backend
- Returns formatted, helpful academic responses
- Stores chat history per user session
- Collects feedback through a star rating system
- Exposes 5 working REST API endpoints

---

## 9. Conclusion

The Multi-Agent AI System for Academic Assistance was successfully designed
and developed in Week 3. The system demonstrates a complete client-server
architecture with a working AI integration, clean frontend interface, and
documented REST API. The project is version controlled on GitHub and ready
for further development and deployment.

---
