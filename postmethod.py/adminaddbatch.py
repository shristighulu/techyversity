import requests
import json

# Base URL
base_url = "https://api.techyversity.com"

# Auth token (raw token ONLY, no "Bearer" prefix)
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIwNzYzMzIsImV4cCI6MTc3MjE2MjczMn0._OF5UQlddD5ExHRk6DhH0wec8rRnYNVyHtB5k-tnhyU"

def post_request():
    url = f"{base_url}/api/batch/add"
    print("post url:", url)
    
    # Correct header
    headers = {"Authorization": f"Bearer {auth_token}"}
    print("Headers being sent:", headers)  # Debug print

    data = {
        "title": "sh batch",
        "description": "hello everyone..",
        "schedules": {
            "startDateAndTime": "2026-02-26T07:52",
            "endDateAndTime": "2026-04-26T07:52"
        }
    }

    response = requests.post(url, json=data, headers=headers)
    
    # Convert response to JSON safely
    try:
        json_data = response.json()
        print("JSON Response:")
        print(json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Response is not valid JSON:")
        print(response.text)
    
    # Optional: assert success
    if response.status_code != 201:
        print("Test Failed - Expected 201 but got", response.status_code)
    else:
        print("Test Passed")

# Call function
post_request()