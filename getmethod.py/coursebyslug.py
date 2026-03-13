import requests
import json

# base url
base_url = "https://api.techyversity.com"

# auth token (raw token only)
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjMyMjE5MSwiZXhwIjoxNzcyNDA4NTkxfQ.37VhgAqVOpDJf308KNBts8V0nNLobjhH0mGGuuLHYVk"

def get_request():
    url = f"{base_url}/api/course/slug"

    params = {
        "slug": "devops-engineering"
    }

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    print("GET URL:", url)

    response = requests.get(url, headers=headers, params=params)

    print("Final URL:", response.url)
    print("Status code:", response.status_code)

    json_data = response.json()
    print(json.dumps(json_data, indent=4))

    assert response.status_code == 200

# call function
get_request()