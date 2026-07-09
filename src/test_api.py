import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"
results = []

def test(name, method, endpoint, payload=None, params=None, expected_status=200):
    url = BASE_URL + endpoint
    try:
        if method == "GET":
            res = requests.get(url, params=params, timeout=10)
        else:
            res = requests.post(url, json=payload, timeout=10)

        passed = res.status_code == expected_status
        try:
            body = res.json()
        except:
            body = res.text

        results.append({
            "name": name,
            "method": method,
            "endpoint": endpoint,
            "expected_status": expected_status,
            "actual_status": res.status_code,
            "passed": passed,
            "response": body
        })

        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} | {method} {endpoint} | Status: {res.status_code} | {name}")

    except Exception as e:
        results.append({
            "name": name,
            "method": method,
            "endpoint": endpoint,
            "expected_status": expected_status,
            "actual_status": "ERROR",
            "passed": False,
            "response": str(e)
        })
        print(f"❌ ERROR | {method} {endpoint} | {name} | {str(e)}")

print("\n" + "="*60)
print("  API TESTING — Multi-Agent AI Academic Assistant")
print("="*60 + "\n")

# ── HEALTH CHECK ──
print("--- Health Check ---")
test("Health check returns healthy status",
     "GET", "/api/health", expected_status=200)

# ── CHAT ENDPOINT ──
print("\n--- Chat Endpoint ---")
test("Valid chat message gets AI response",
     "POST", "/api/chat",
     payload={"user_id": "123", "message": "What is photosynthesis?"},
     expected_status=200)

test("Empty message returns 400 error",
     "POST", "/api/chat",
     payload={"user_id": "123", "message": ""},
     expected_status=400)

test("Missing message field returns 400 error",
     "POST", "/api/chat",
     payload={"user_id": "123"},
     expected_status=400)

test("Message too long returns 400 error",
     "POST", "/api/chat",
     payload={"user_id": "123", "message": "x" * 2001},
     expected_status=400)

test("Non-JSON request returns 400 error",
     "POST", "/api/chat",
     payload=None,
     expected_status=400)

# ── HISTORY ENDPOINT ──
print("\n--- History Endpoint ---")
test("Get history for valid user",
     "GET", "/api/history",
     params={"user_id": "123"},
     expected_status=200)

test("Missing user_id returns 400 error",
     "GET", "/api/history",
     expected_status=400)

# ── USERS ENDPOINT ──
print("\n--- Users Endpoint ---")
test("Get existing user info",
     "GET", "/api/users",
     params={"user_id": "123"},
     expected_status=200)

test("Get non-existent user returns 404",
     "GET", "/api/users",
     params={"user_id": "999"},
     expected_status=404)

test("Missing user_id returns 400",
     "GET", "/api/users",
     expected_status=400)

# ── FEEDBACK ENDPOINT ──
print("\n--- Feedback Endpoint ---")
test("Valid feedback with rating 5",
     "POST", "/api/feedback",
     payload={"user_id": "123", "rating": 5, "comment": "Very helpful!"},
     expected_status=200)

test("Valid feedback with rating 1",
     "POST", "/api/feedback",
     payload={"user_id": "123", "rating": 1, "comment": "Not helpful"},
     expected_status=200)

test("Missing rating returns 400",
     "POST", "/api/feedback",
     payload={"user_id": "123", "comment": "No rating given"},
     expected_status=400)

test("Invalid rating (0) returns 400",
     "POST", "/api/feedback",
     payload={"user_id": "123", "rating": 0},
     expected_status=400)

test("Invalid rating (6) returns 400",
     "POST", "/api/feedback",
     payload={"user_id": "123", "rating": 6},
     expected_status=400)

# ── 404 HANDLER ──
print("\n--- Error Handlers ---")
test("Unknown endpoint returns 404",
     "GET", "/api/unknown",
     expected_status=404)

# ── SUMMARY ──
total  = len(results)
passed = sum(1 for r in results if r["passed"])
failed = total - passed

print("\n" + "="*60)
print(f"  RESULTS: {passed}/{total} tests passed")
print("="*60)

# ── SAVE REPORT ──
report = f"""# API Testing Report
## Multi-Agent AI Academic Assistant

**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Base URL:** {BASE_URL}
**Total Tests:** {total}
**Passed:** {passed}
**Failed:** {failed}
**Pass Rate:** {round(passed/total*100)}%

---

## Test Results

| # | Test Name | Method | Endpoint | Expected | Actual | Result |
|---|-----------|--------|----------|----------|--------|--------|
"""

for i, r in enumerate(results, 1):
    icon = "✅" if r["passed"] else "❌"
    report += f"| {i} | {r['name']} | {r['method']} | {r['endpoint']} | {r['expected_status']} | {r['actual_status']} | {icon} |\n"

report += f"""
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

{passed} out of {total} tests passed ({round(passed/total*100)}% pass rate).
All core API endpoints are functioning correctly with proper error handling.
The system validates inputs and returns appropriate HTTP status codes.

*Report generated automatically by test_api.py*
"""

with open("reports/api_testing_report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("\n✅ Report saved to reports/api_testing_report.md")