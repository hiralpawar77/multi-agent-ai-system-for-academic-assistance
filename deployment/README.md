this folder contains deployment files like Dockerfile and deployment scripts.

# Deployment

This folder contains deployment instructions and configuration.

## Live URL
https://web-production-ffbc.up.railway.app

## Platform
Railway — https://railway.app

## How to Deploy

### 1. Install dependencies
```bash
pip install flask flask-cors groq python-dotenv gunicorn
pip freeze > requirements.txt
```

### 2. Create Procfile
web: python src/app.py

### 3. Push to GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push
```

### 4. Deploy on Railway
- Sign in at railway.app with GitHub
- Click New Project → Deploy from GitHub repo
- Select your repository
- Add environment variable: `GROQ_API_KEY`
- Click Deploy

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |
| `PORT` | Auto-set by Railway |

## Verify Deployment
Visit the health check endpoint:
https://web-production-ffbc.up.railway.app/api/health

Expected response:
```json
{
  "status": "healthy",
  "message": "Server is running"
}
```