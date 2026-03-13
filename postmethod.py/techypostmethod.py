import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIwMDQ0ODUsImV4cCI6MTc3MjA5MDg4NX0.XCMWBAZ-a-6yK5s3ltDfYN23jTjuMEEUSvgXf87xWWw "

def post_request():
    url=f"{base_url}/api/auth/register"
    print("post url:"+url)
    headers={"Authorization":f"Bearer {auth_token}"}
    data={
    "firstName":"Unika",
    "lastName":"Shrestha",
    "email":"Unika@123.com",
    "password":"try@Now122",
    "role":"student"
    }
    response=requests.post(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post request:",json_str)
    # user_id=json_data["id"]
    user_id=json_data["id"]
    print("user id===>",user_id)
    assert response.status_code==201
    assert "name" in json_data
    return user_id
#call function
user_id=post_request()

