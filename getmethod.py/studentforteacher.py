import requests
import json

# base url
base_url = "https://api.techyversity.com"

# auth token
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWEwMWVlOWM4MWNhOGQ3NmUwZjI2YTMiLCJyb2xlIjoidGVhY2hlciIsImlhdCI6MTc3MjI3MDAxMSwiZXhwIjoxNzcyMzU2NDExfQ.9a0JV2cUwFUvB4DufVeQM1CbazLybvu_34N_L6MD2y4"

def get_request():
    url = f"{base_url}/api/teacher/students"

    params = {
        "page": 1,
        "perPage": 10,
    

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