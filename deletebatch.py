import requests
import json

# Base URL
base_url = "https://api.techyversity.com"
# Auth token
auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIzMjU5NzksImV4cCI6MTc3MjQxMjM3OX0.1z7534hr6wdbkFrqJKAjioOzMTAXfyZLHI_Ixd2uYD0"

def delete_request():
    # Use query param (or path param if API supports it)
    url = base_url + f"/api/batch/?id=69a01fb3c81ca8d76e0f26d7"
    print("DELETE URL:", url)

    headers = {"Authorization": auth_token}

    # Call the DELETE request first
    response = requests.delete(url, headers=headers)

    # Then print the response
    print("Status Code:", response.status_code)
    print("Response json:", response.json)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put request:",json_str)

    # Return status code for verification
    return response.status_code


# Call function
delete_request()