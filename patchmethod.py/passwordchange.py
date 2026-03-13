import requests
import json


#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjA5MTgxOSwiZXhwIjoxNzcyMTc4MjE5fQ.C5WfVw5lS6CboBkvW-3Q3-VAI4bIOsdiccqGP0mh110"

#put request
def patch_request():
    url=base_url +"/api/auth/password"
    # print("patch url:"+url)
    headers={"Authorization":auth_token}
    data={
    "oldPassword":"Newpassword@123",
    "newPassword":"Letme@123"
}
    response = requests.patch(url, json=data, headers=headers)
    # print("PATCH Status:", response.status_code)
    # print("PATCH Response:", response.json )
    

    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put request:",json_str)

    if response.status_code == 200:
        print("Password changed successfully!")
    else:
        print("Failed to change password")

  
patch_request()

