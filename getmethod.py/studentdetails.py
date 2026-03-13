import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjA5ODU0MCwiZXhwIjoxNzcyMTg0OTQwfQ.y1mLQqrAvt8ZUoTU4o4cQ8gOmf4Gj45Uu5K057LUP1g"

def get_request():
    url=f"{base_url}/api/student"


    print("get url:"+url)
    headers={"Authorization":f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)

    try:
        json_data = response.json()
        print(json.dumps(json_data, indent=4))
    except json.JSONDecodeError:
        print("Response is not JSON:", response.text)
get_request()