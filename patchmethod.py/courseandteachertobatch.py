import requests
import json


#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMjU5NzksImV4cCI6MTc3MjQxMjM3OX0.1z7534hr6wdbkFrqJKAjioOzMTAXfyZLHI_Ixd2uYD0"


#put request
def patch_request():
    url=base_url +f"/api/batch/add"
    print("patch url:"+url)
    headers={"Authorization":auth_token}
    params={
    "courseId": "6963478e51a89ca89786bec5",
    "teacherId": "69a01ee9c81ca8d76e0f26a3",
    "batchId": "69956ebf6c841f7943cbd2e7"}
    response = requests.patch(url, headers=headers, params=params)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put request:",json_str)

    if response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to patch user")

  
patch_request()