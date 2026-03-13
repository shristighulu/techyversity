
import requests
import json

# Base URL
base_url = "https://api.techyversity.com"
# Auth token
auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWEwMWVlOWM4MWNhOGQ3NmUwZjI2YTMiLCJyb2xlIjoidGVhY2hlciIsImlhdCI6MTc3MjM1MTE3MiwiZXhwIjoxNzcyNDM3NTcyfQ.68UrWRGNsDBZ8GFzlNuzGCZhQ8T1hQOkP6bhnk5wGc4"

def delete_request():
    url = base_url + f"/api/lesson?id=69980bb2dd8c8289eb507216"
    print("DELETE URL:", url)

    headers = {"Authorization": auth_token}

    # Call the DELETE request first
    response = requests.delete(url, headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json delete request:",json_str)

    # Return status code for verification
    return response.status_code


# Call function
delete_request()