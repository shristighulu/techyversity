import requests
import json

base_url = "https://api.techyversity.com"
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWEwMWVlOWM4MWNhOGQ3NmUwZjI2YTMiLCJyb2xlIjoidGVhY2hlciIsImlhdCI6MTc3MjM1MTE3MiwiZXhwIjoxNzcyNDM3NTcyfQ.68UrWRGNsDBZ8GFzlNuzGCZhQ8T1hQOkP6bhnk5wGc4"

def add_lesson():
    url = f"{base_url}/api/lesson/add"
    
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    
    data = {
    
        "title":"Devops class",
        "description":"Newly Created class ",
        "duration":{
            "hour":1,
        "minutes":34
    },
    "linkedCourse":"6963478e51a89ca89786bec5",
    "batch": "69956ebf6c841f7943cbd2e7",
    "videoUrl": "https://youtu.be/RRBF2YWXFtY?si=4qsBzWfS_Th1f5NK"
}
    

    response = requests.post(url, headers=headers, data=data)
    #File name: industry.csv
    #File object: file
#Content type: text/csv
    
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post request:",json_str)
   # Check login success
    print("Status Code:", response.status_code)
    
# Call function without CSV (safe if file doesn't exist)
add_lesson()