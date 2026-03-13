import requests
import json

# base url
base_url = "https://api.techyversity.com"

# auth token
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjI2OTgwOSwiZXhwIjoxNzcyMzU2MjA5fQ.wPtfHshkrkNa3NbqOQx59AjDEvIqcJSb-FMq2qf2pSc"

def get_request():
    url = f"{base_url}/api/batch/enrolled-students"

    params = {
        "page": 1,
        "perPage": 10,
        "courseId": "6963478e51a89ca89786bec5",
        "batchId": "69945a51c81ca8d76e0f12d6",

    }

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    print("GET URL:", url)

    response = requests.get(url, headers=headers, params=params)

    print("Final URL:", response.url)
    print("Status code:", response.status_code)

    try:
        json_data = response.json()
        print(json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Response is not JSON:", response.text)

# call function
get_request()