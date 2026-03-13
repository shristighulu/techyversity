import requests
import json

# Base URL
base_url = "https://api.techyversity.com"

# Auth token (raw token only, no "Bearer")
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTlkNmE5OWQ0N2JhZTU1NTY4OGY3OWQiLCJyb2xlIjoic3R1ZGVudCIsImlhdCI6MTc3MjEwMDIyMCwiZXhwIjoxNzcyMTg2NjIwfQ.XhMQkQexJTEr_PnSK3tg2BjZ2b1TWkNDk22EiEvoI9U"

def post_request(course_id, batch_id):
    print("Course ID:", course_id)
    print("Batch ID:", batch_id)
    url = f"{base_url}/api/student/enroll?courseId={course_id}&batchId={batch_id}"
    print("post url:", url)
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    print("Headers being sent:", headers)

    data ={
        "firstName": "shriti",
    "lastName": "ghulu",
    "email": "shristighuluu@gmail.com",
    "coursetitle":"Full stack Development"
    }

    response = requests.post(url, json=data, headers=headers)
    
    # Directly get JSON response (assumes API always returns JSON)
    json_data = response.json()
    print("JSON Response:")
    print(json.dumps(json_data, indent=4))
    
    # Optional: check success
    if response.status_code != 201:
        print("Test Failed - Expected 201 but got", response.status_code)
    else:
        print("Test Passed")
        
my_course_id = "696347e051a89ca89786bf1d" #data science course id
my_batch_id = "6995708dc81ca8d76e0f1509"#january batch

# Call the function with the IDs
post_request(my_course_id, my_batch_id)