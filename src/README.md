this folder contains source code for data preprocessing, training, and inference.

# Source Code

This folder contains the main application source code.

## Files
- `app.py` — Flask backend server with all API endpoints
- `index.html` — Frontend chat interface
- `architecture_diagram.py` — Script to generate the system architecture diagram
- `data_cleaning.ipynb` — Data cleaning and preprocessing notebook

## How to Run

### Backend
```bash
pip install flask flask-cors groq
python src/app.py
```

### Frontend
Open `src/index.html` in your browser while the backend is running.
