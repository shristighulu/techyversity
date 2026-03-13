
import requests
import json


#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMzAwOTYsImV4cCI6MTc3MjQxNjQ5Nn0.Rxht9W0hjZeuaiqJ6bXyf4PB1OMnTEyUJGwvehlNo4g"

#put request
def patch_request():
    url=base_url +f"/api/admin/users?id=699d6a99d47bae555688f79d"
    print("patch url:"+url)
    headers={"Authorization":auth_token}
    data={
        "firstName":"shristi",
    "lastName":"Shrestha",
    "email":"shristighuluu@gmail.com",

    }
    response = requests.patch(url, json=data, headers=headers)
    
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json patch request:",json_str)

    if response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to patch user")


patch_request()