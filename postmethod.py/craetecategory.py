import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMjUyMzIsImV4cCI6MTc3MjQxMTYzMn0.UzSz1rEh3bx4OITfXDKaqEiRJqLCU_Y0PaN_oi7bxUc"

def post_request():
    url=f"{base_url}/api/category/add"


    print("post url:"+url)
    headers={"Authorization":f"Bearer {auth_token}"}
    data={
    "title":"design and development",
    "description":"Enhance your business.."
    
       
    }
    response=requests.post(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post request:",json_str)
   # Check login success
    assert response.status_code == 201
post_request()
