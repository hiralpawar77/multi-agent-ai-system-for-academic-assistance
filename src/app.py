from flask import Flask, request, jsonify
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
# 2. CHAT ENDPOINT (now with real AI!)
# ─────────────────────────────────────────
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'anonymous')
        message = data.get('message', '')

        if not message:
            return jsonify({
                "status": "error",
                "message": "No message provided"
            }), 400

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
        for msg in history[-10:]:  # Last 10 messages
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
            temperature=0.7
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
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# ─────────────────────────────────────────
# 3. CHAT HISTORY ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/history', methods=['GET'])
def get_history():
    try:
        user_id = request.args.get('user_id', 'anonymous')
        history = chat_history.get(user_id, [])

        return jsonify({
            "status": "success",
            "user_id": user_id,
            "history": history
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# ─────────────────────────────────────────
# 4. USERS ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/users', methods=['GET'])
def get_user():
    try:
        user_id = request.args.get('user_id', '')

        if not user_id:
            return jsonify({
                "status": "error",
                "message": "user_id is required"
            }), 400

        user = users.get(user_id)

        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404

        return jsonify({
            "status": "success",
            "user": user
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# ─────────────────────────────────────────
# 5. FEEDBACK ENDPOINT
# ─────────────────────────────────────────
@app.route('/api/feedback', methods=['POST'])
def feedback():
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'anonymous')
        rating = data.get('rating', 0)
        comment = data.get('comment', '')

        if not rating:
            return jsonify({
                "status": "error",
                "message": "Rating is required"
            }), 400

        feedback_store.append({
            "user_id": user_id,
            "rating": rating,
            "comment": comment,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return jsonify({
            "status": "success",
            "message": "Feedback recorded, thank you!"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# ─────────────────────────────────────────
# RUN SERVER
# ─────────────────────────────────────────
if __name__ == '__main__':
    print("Starting Flask server with Groq AI...")
    print("Visit http://localhost:5000/api/health to test")
    app.run(debug=True, port=5000)