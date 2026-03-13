import requests
import json

# Base URL
base_url = "https://api.techyversity.com"
# Auth token
auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzIwMDQ0ODUsImV4cCI6MTc3MjA5MDg4NX0.XCMWBAZ-a-6yK5s3ltDfYN23jTjuMEEUSvgXf87xWWw"

def delete_request(user_id):
    # Use query param (or path param if API supports it)
    url = base_url + f"/api/admin/users?id={user_id}"
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

    # If response is JSON, pretty print
    # if response.text.startswith("{"):
    #     json_data = response.json()
    #     json_str = json.dumps(json_data, indent=4)
    #     print("JSON Response:\n", json_str)

    # Return status code for verification
    return response.status_code


# Call function
user_id_delete = "6989912be0c52c6c1dd4ced0"
delete_request(user_id_delete)