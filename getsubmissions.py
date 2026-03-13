import requests
import json

# base url
base_url = "https://api.techyversity.com"

# auth token (raw token only)
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWEwMWVlOWM4MWNhOGQ3NmUwZjI2YTMiLCJyb2xlIjoidGVhY2hlciIsImlhdCI6MTc3MjM1MTE3MiwiZXhwIjoxNzcyNDM3NTcyfQ.68UrWRGNsDBZ8GFzlNuzGCZhQ8T1hQOkP6bhnk5wGc4"

def get_request():
    url = f"{base_url}/api/assignment/submissions?assignmentId=69a3e681c81ca8d76e0f2b18"

    params = {
        "slug": "devops-engineering"
    }

    headers = {"Authorization": f"Bearer {auth_token}"}

    print("GET URL:", url)

    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    print(json.dumps(json_data, indent=4))

    # assert response.status_code == 200

# call function
get_request()