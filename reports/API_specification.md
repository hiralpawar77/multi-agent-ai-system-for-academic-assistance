# API Specification Document
## Multi-Agent AI System for Academic Assistance

---

## Base URL

http://localhost:5000

---

## Endpoints

### 1. POST /api/chat
**Purpose:** Send a user prompt to the AI and get a response.

**Request Body:**
```json
{
  "user_id": "123",
  "message": "Explain Newton's second law"
}
```

**Response:**
```json
{
  "status": "success",
  "response": "Newton's second law states that F = ma..."
}
```

---

### 2. GET /api/history
**Purpose:** Retrieve past conversations for a user.

**Query Parameter:** `?user_id=123`

**Response:**
```json
{
  "status": "success",
  "history": [
    {"role": "user", "message": "Explain Newton's second law"},
    {"role": "ai", "message": "Newton's second law states..."}
  ]
}
```

---

### 3. GET /api/users
**Purpose:** Fetch user information.

**Query Parameter:** `?user_id=123`

**Response:**
```json
{
  "status": "success",
  "user": {
    "id": "123",
    "name": "Student Name",
    "email": "student@example.com"
  }
}
```

---

### 4. POST /api/feedback
**Purpose:** Store user ratings/feedback on AI responses.

**Request Body:**
```json
{
  "user_id": "123",
  "message_id": "456",
  "rating": 5,
  "comment": "Very helpful explanation!"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Feedback recorded"
}
```

---

### 5. GET /api/health
**Purpose:** Check if the server is running properly.

**Response:**
```json
{
  "status": "healthy",
  "message": "Server is running"
}
```

---

## Error Response Format
All endpoints return this format on error:
```json
{
  "status": "error",
  "message": "Description of what went wrong"
}
```