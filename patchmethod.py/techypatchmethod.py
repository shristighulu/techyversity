import requests
import json


#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIwMDQ0ODUsImV4cCI6MTc3MjA5MDg4NX0.XCMWBAZ-a-6yK5s3ltDfYN23jTjuMEEUSvgXf87xWWw"


#put request
def patch_request(user_id):
    url=base_url +f"/api/admin/users?id={user_id}"
    print("patch url:"+url)
    headers={"Authorization":auth_token}
    data={
        "firstName":"aaravi",
    "lastName":"Shresth",
    "email":"Unika@123.com",
    "password":"try@Now122",
    "role":"student"
    }
    response = requests.patch(url, json=data, headers=headers)
    # print("PATCH Status:", response.status_code)
    # print("PATCH Response:", response.json )
    

    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put request:",json_str)

    if response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to patch user")

# Example usage
user_id_to_update = "699ebc21033221808df48cf3"  
patch_request(user_id_to_update)

