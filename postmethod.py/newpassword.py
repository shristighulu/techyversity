import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjA5MzgzMCwiZXhwIjoxNzcyMTgwMjMwfQ.z24Zwqq1OHvTSBkqTyyNWVXR0o_4JeL-NEUZeDgjHfA"

def patch_request():
    url=f"{base_url}/api/auth/resetPassword"


    print("patch url:"+url)
    headers={"Authorization":f"Bearer {auth_token}"}
    data={
        "email":"shristighuluu@gmail.com",
        "newPassword": "Newpassword@12345"
    
       
    }
    response=requests.patch(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post request:",json_str)
   # Check login success
    assert response.status_code == 200
patch_request()
