import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMzE4MTIsImV4cCI6MTc3MjQxODIxMn0.j9aDLxjuDF8dKxG6ZdBwtGVLBTRbC1_C2wA3O2OKfyM"
def get_request():
    url=f"{base_url}/api/inquiry/list?page=2&perPage=10"


    print("get url:"+url)
    headers={"Authorization":f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)

    try:
        json_data = response.json()
        #to print json data in readable format
        print(json.dumps(json_data, indent=4))
        # print("Get response content:",json_str)
    except json.JSONDecodeError:
        print("Response is not JSON:", response.text)
get_request()