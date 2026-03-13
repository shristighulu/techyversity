import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIwMDQ0ODUsImV4cCI6MTc3MjA5MDg4NX0.XCMWBAZ-a-6yK5s3ltDfYN23jTjuMEEUSvgXf87xWWw"

def get_request(page):
    url=f"{base_url}/api/admin/users?page={page}"
    print(f"get url:{url}") 
    headers={"Authorization":auth_token}if auth_token else{}
    response=requests.get(url,headers=headers)
    assert response.status_code==200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print(f"Get response content:{page}",json_str)
    print("....get user is done..")
    print("....=====....")
    
#function call
get_request(2)