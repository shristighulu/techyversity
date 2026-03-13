import requests
import json


#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMjU5NzksImV4cCI6MTc3MjQxMjM3OX0.1z7534hr6wdbkFrqJKAjioOzMTAXfyZLHI_Ixd2uYD0"


#put request
def patch_request(category_id):
    url=base_url +f"/api/category/?id={category_id}"
    print("patch url:"+url)
    headers={"Authorization":auth_token}
    data={
    "title":"design and development",
    "description":"Enhance your ability.."
    }
    response = requests.patch(url, json=data, headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put request:",json_str)

    if response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to patch user")

category_id_to_update = "69a38b0b716a89905662c02a"  
patch_request(category_id_to_update)