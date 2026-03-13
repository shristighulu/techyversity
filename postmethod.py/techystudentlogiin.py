import requests
import json
#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="token value"

def post_request():
    url=f"{base_url}/api/auth/login"
    print("post url:"+url)
    headers={"Authorization":auth_token}
    data={
        "email":"shristighuluu@gmail.com",
        "password":"Letme@123"
    }
    response=requests.post(url,json=data,headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post request:",json_str)
   # Check login success
    assert response.status_code == 200
    
    # response = requests.post(url, json=data, headers=headers)

    # json_data = response.json()
    # print("Response JSON:\n", json.dumps(json_data, indent=4))

    # # Better assertion with message
    # assert response.status_code == 200, f"Login failed! Status: {response.status_code}"

    # token = json_data.get("token")
    # print("Login successful! Token received.")
    # return token


post_request()
