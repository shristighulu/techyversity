import requests
import json

# Base URL
base_url = "https://api.techyversity.com"

# Auth token
auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWEwMWVlOWM4MWNhOGQ3NmUwZjI2YTMiLCJyb2xlIjoidGVhY2hlciIsImlhdCI6MTc3MjM1MDEwMCwiZXhwIjoxNzcyNDM2NTAwfQ.k0toW9sfbEQrna7zJAvmPs_-bEm0jWaKso2NqafVTj0"

def patch_request():
   
    url = base_url + "/api/assignment/update?id=69a3e681c81ca8d76e0f2b18"

    headers = {"Authorization": auth_token}
    data = {
        "title": "Assignment 2",
        "description": "to be... ",
        "linkedCourse": "6963478e51a89ca89786bec5",
        "instructions": "as per",
        "dueDate": "2026-03-01",
        "batch": "69956ebf6c841f7943cbd2e7",
        "linkedLesson": "69a3e63c716a89905662c1f9"
    }

    response = requests.patch(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json patch request:", json_str)

# Call the function
patch_request()