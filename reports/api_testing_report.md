# API Testing Report
## Multi-Agent AI Academic Assistant

**Date:** 2026-07-09 19:59:11
**Base URL:** http://localhost:5000
**Total Tests:** 17
**Passed:** 17
**Failed:** 0
**Pass Rate:** 100%

---

## Test Results

| # | Test Name | Method | Endpoint | Expected | Actual | Result |
|---|-----------|--------|----------|----------|--------|--------|
| 1 | Health check returns healthy status | GET | /api/health | 200 | 200 | ✅ |
| 2 | Valid chat message gets AI response | POST | /api/chat | 200 | 200 | ✅ |
| 3 | Empty message returns 400 error | POST | /api/chat | 400 | 400 | ✅ |
| 4 | Missing message field returns 400 error | POST | /api/chat | 400 | 400 | ✅ |
| 5 | Message too long returns 400 error | POST | /api/chat | 400 | 400 | ✅ |
| 6 | Non-JSON request returns 400 error | POST | /api/chat | 400 | 400 | ✅ |
| 7 | Get history for valid user | GET | /api/history | 200 | 200 | ✅ |
| 8 | Missing user_id returns 400 error | GET | /api/history | 400 | 400 | ✅ |
| 9 | Get existing user info | GET | /api/users | 200 | 200 | ✅ |
| 10 | Get non-existent user returns 404 | GET | /api/users | 404 | 404 | ✅ |
| 11 | Missing user_id returns 400 | GET | /api/users | 400 | 400 | ✅ |
| 12 | Valid feedback with rating 5 | POST | /api/feedback | 200 | 200 | ✅ |
| 13 | Valid feedback with rating 1 | POST | /api/feedback | 200 | 200 | ✅ |
| 14 | Missing rating returns 400 | POST | /api/feedback | 400 | 400 | ✅ |
| 15 | Invalid rating (0) returns 400 | POST | /api/feedback | 400 | 400 | ✅ |
| 16 | Invalid rating (6) returns 400 | POST | /api/feedback | 400 | 400 | ✅ |
| 17 | Unknown endpoint returns 404 | GET | /api/unknown | 404 | 404 | ✅ |

---

## Endpoints Tested

### 1. GET /api/health
Verifies the server is running and returns a healthy status.

### 2. POST /api/chat
Sends a user message to the AI and returns a response.
Tests include: valid message, empty message, missing field, message too long, non-JSON request.

### 3. GET /api/history
Retrieves chat history for a specific user.
Tests include: valid user_id, missing user_id.

### 4. GET /api/users
Fetches user information by user_id.
Tests include: existing user, non-existent user, missing user_id.

### 5. POST /api/feedback
Stores a user rating for an AI response.
Tests include: valid ratings, missing rating, invalid rating values.

### 6. Error Handlers
Tests 404 handler for unknown endpoints.

---

## Conclusion

17 out of 17 tests passed (100% pass rate).
All core API endpoints are functioning correctly with proper error handling.
The system validates inputs and returns appropriate HTTP status codes.

*Report generated automatically by test_api.py*
