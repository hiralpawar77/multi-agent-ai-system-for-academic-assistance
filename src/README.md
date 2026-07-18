this folder contains source code for data preprocessing, training, and inference.

# Source Code

This folder contains all application source code.

## Files

| File | Description |
|---|---|
| `app.py` | Flask backend server with all 5 API endpoints |
| `index.html` | Frontend chat interface served by Flask |
| `test_api.py` | Automated API testing script — 17/17 tests pass |
| `architecture_diagram.py` | Generates system architecture diagram |
| `sequence_diagram.py` | Generates sequence diagram |
| `data_cleaning.ipynb` | Data cleaning and preprocessing notebook |

## How to Run

### Install dependencies
```bash
pip install flask flask-cors groq python-dotenv
```

### Set up environment variable
Create a `.env` file in the root folder and add the Groq API key

### Start the backend server
```bash
python src/app.py
```

### Open the frontend
Visit `http://localhost:5000` in your browser.

### Run API tests
```bash
python src/test_api.py
```