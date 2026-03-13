import requests
import json

# base url
base_url = "https://api.techyversity.com"

# auth token
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjI3MDM3MiwiZXhwIjoxNzcyMzU2NzcyfQ.JWk_aBHQvDa242BZJ7WcdZn25ZEd_xa9Er7T9oT8p4c"

def get_request():
    url = f"{base_url}/api/student/enrolled-courses"

    # params = {
    #     "page": 1,
    #     "perPage": 10,
    

    # }

    headers = {"Authorization": f"Bearer {auth_token}"}

    print("GET URL:", url)

    response = requests.get(url, headers=headers, params=None)

    print("Final URL:", response.url)
    print("Status code:", response.status_code)

    try:
        json_data = response.json()
        print(json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Response is not JSON:", response.text)

# call function
get_request()