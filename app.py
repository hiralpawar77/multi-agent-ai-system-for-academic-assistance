from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Simple in-memory storage
chat_history = {}
users = {
    "123": {"id": "123", "name": "Student", "email": "student@example.com"}
}
feedback_store = []

# ─────────────────────────────────────────
# HELPER: Standard error response
# ─────────────────────────────────────────
def error_response(message, status_code=400):
    return jsonify({
        "status": "error",
        "message": message
    }), status_code

# ── SERVE FRONTEND ──
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

# ─────────────────────────────────────────
# 1. HEALTH CHECK
# ─────────────────────────────────────────
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Server is running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# ─────────────────────────────────────────
# 2. CHAT ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/chat', methods=['POST'])
def chat():
    # Check request has JSON
    if not request.is_json:
        return error_response("Request must be JSON", 400)

    data = request.get_json()

    # Check required fields
    if not data:
        return error_response("Request body is empty", 400)

    message = data.get('message', '').strip()
    user_id = data.get('user_id', 'anonymous')

    # Validate message
    if not message:
        return error_response("Message field is required and cannot be empty", 400)

    if len(message) > 2000:
        return error_response("Message is too long. Maximum 2000 characters allowed", 400)

    try:
        # Build conversation history for context
        history = chat_history.get(user_id, [])
        messages_for_ai = [
            {
                "role": "system",
                "content": """You are a helpful academic assistant for students.
                You help with essays, explanations, research, study tips,
                and academic questions. Be clear, friendly, and educational."""
            }
        ]

        # Add previous messages for context
        for msg in history[-10:]:
            messages_for_ai.append({
                "role": "user" if msg["role"] == "user" else "assistant",
                "content": msg["message"]
            })

        # Add current message
        messages_for_ai.append({
            "role": "user",
            "content": message
        })

        # Call Groq AI
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages_for_ai,
            max_tokens=1024,
            temperature=0.7,
            timeout=30  # Timeout after 30 seconds
        )

        ai_response = completion.choices[0].message.content

        # Save to history
        if user_id not in chat_history:
            chat_history[user_id] = []

        chat_history[user_id].append({
            "role": "user",
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        chat_history[user_id].append({
            "role": "ai",
            "message": ai_response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return jsonify({
            "status": "success",
            "response": ai_response
        })

    except Exception as e:
        error_msg = str(e)

        # Handle specific error types
        if "timeout" in error_msg.lower():
            return error_response("AI model took too long to respond. Please try again.", 504)
        elif "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            return error_response("AI service authentication failed. Please contact support.", 401)
        elif "rate_limit" in error_msg.lower():
            return error_response("Too many requests. Please wait a moment and try again.", 429)
        else:
            return error_response(f"AI service error: {error_msg}", 500)

# ─────────────────────────────────────────
# 3. CHAT HISTORY ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/history', methods=['GET'])
def get_history():
    user_id = request.args.get('user_id', '').strip()

    if not user_id:
        return error_response("user_id parameter is required", 400)

    try:
        history = chat_history.get(user_id, [])
        return jsonify({
            "status": "success",
            "user_id": user_id,
            "history": history,
            "total_messages": len(history)
        })

    except Exception as e:
        return error_response(f"Failed to retrieve history: {str(e)}", 500)

# ─────────────────────────────────────────
# 4. USERS ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/users', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id', '').strip()

    if not user_id:
        return error_response("user_id parameter is required", 400)

    try:
        user = users.get(user_id)

        if not user:
            return error_response(f"User with id '{user_id}' not found", 404)

        return jsonify({
            "status": "success",
            "user": user
        })

    except Exception as e:
        return error_response(f"Failed to retrieve user: {str(e)}", 500)

# ─────────────────────────────────────────
# 5. FEEDBACK ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/feedback', methods=['POST'])
def feedback():
    if not request.is_json:
        return error_response("Request must be JSON", 400)

    data = request.get_json()

    if not data:
        return error_response("Request body is empty", 400)

    user_id = data.get('user_id', 'anonymous')
    rating = data.get('rating')
    comment = data.get('comment', '').strip()

    # Validate rating
    if rating is None:
        return error_response("Rating field is required", 400)

    if not isinstance(rating, int) or rating < 1 or rating > 5:
        return error_response("Rating must be a number between 1 and 5", 400)

    try:
        feedback_store.append({
            "user_id": user_id,
            "rating": rating,
            "comment": comment,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return jsonify({
            "status": "success",
            "message": f"Feedback recorded. Thank you for rating {rating}/5!"
        })

    except Exception as e:
        return error_response(f"Failed to save feedback: {str(e)}", 500)

# ─────────────────────────────────────────
# HANDLE 404 - Route not found
# ─────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return error_response("Endpoint not found", 404)

# ─────────────────────────────────────────
# HANDLE 405 - Method not allowed
# ─────────────────────────────────────────
@app.errorhandler(405)
def method_not_allowed(e):
    return error_response("Method not allowed for this endpoint", 405)

# ─────────────────────────────────────────
# RUN SERVER
# ─────────────────────────────────────────
if __name__ == '__main__':
    print("Starting Flask server with error handling...")
    print("Visit https://web-production-ffbc.up.railway.app/api/health to test")