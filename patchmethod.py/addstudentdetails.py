
import requests
import json

# Base URL
base_url = "https://api.techyversity.com"

# Auth token (raw token only, no "Bearer")
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjA5ODU0MCwiZXhwIjoxNzcyMTg0OTQwfQ.y1mLQqrAvt8ZUoTU4o4cQ8gOmf4Gj45Uu5K057LUP1g"

def patch_request():
    url = f"{base_url}/api/student/profile"
    print("patch url:", url)
    
    headers = {"Authorization": f"Bearer {auth_token}"}
  
    data ={
  "firstName": "shriti",
  "lastName": "ghulu",
  "phoneNumber": "98756739810",
  "state": "Bagmati",
  "address": {
      "street": "namobudharoad",
      "city": "Panauti-06,kavrepalanchok",
      "state": "Bagmati",
      "zipCode": "44088",
      "country": "Nepal"
  }
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