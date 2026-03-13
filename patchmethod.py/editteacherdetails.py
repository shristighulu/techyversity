
import requests
import json

# Base URL
base_url = "https://api.techyversity.com"

# Auth token (raw token only, no "Bearer")
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMzA5MTMsImV4cCI6MTc3MjQxNzMxM30._HqmmRf7zo70DVzhBZ5rmlyZwRrxi-xJSmdNvRkWfS0"

def patch_request():
    url = f"{base_url}/api/teacher?id=69956eaad47bae555688ea8f"
    print("patch url:", url)
    
    headers = {"Authorization": f"Bearer {auth_token}"}
  
    data ={
  
    "qualifications":["bachelor","master"],
    "specialization":["data science","devops"], 
    "experience":"5"
}

    response = requests.patch(url, json=data, headers=headers)
    
    # Directly get JSON response (assumes API always returns JSON)
    json_data = response.json()
    print("JSON Response:")
    print(json.dumps(json_data, indent=4))
    
    # Optional: check success
    if response.status_code != 201:
        print("Test Failed - Expected 201 but got", response.status_code)
    else:
        print("Test Passed")

# Call the function
patch_request()