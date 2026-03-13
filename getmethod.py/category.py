import requests
import json

# base url
base_url = "https://api.techyversity.com"

# auth token (raw token only)
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMjUyMzIsImV4cCI6MTc3MjQxMTYzMn0.UzSz1rEh3bx4OITfXDKaqEiRJqLCU_Y0PaN_oi7bxUc"

def get_request():
    url = f"{base_url}/api/category/"

    # params = {
    #     "slug": "devops-engineering"
    # }

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    print("GET URL:", url)

    response = requests.get(url, headers=headers, params=None)

    print("Final URL:", response.url)
    print("Status code:", response.status_code)

    json_data = response.json()
    print(json.dumps(json_data, indent=4))

    assert response.status_code == 200

# call function
get_request()