import requests
import json

base_url = "https://api.techyversity.com"
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWEwMWVlOWM4MWNhOGQ3NmUwZjI2YTMiLCJyb2xlIjoidGVhY2hlciIsImlhdCI6MTc3MjMyOTUzNSwiZXhwIjoxNzcyNDE1OTM1fQ.p0dZkjtJiCKbXhwHCZjix1vH9tyaZjUwV4d7Br9iHh4"

def add_assignment():
    url = f"{base_url}/api/assignment/add"
    
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    
    data = {
        "title": "assignment1",
        "description": "This is assignment1",
        "linkedCourse": "6963483b51a89ca89786bf6b",
        "instructions": "will be submitted in csv format",
        "dueDate": "2026-02-12",
        "batch": "69956ebf6c841f7943cbd2e7",
        "linkedLesson": "69980bb2dd8c8289eb507216"
    }
    
    with open("industry.csv", "r") as file:
        content=file.read()
        print("CSV file content:", content[:100])  
        file.seek(0)
        
        files = {
            "attachments": ("industry.csv", file, "text/csv")#
        }

        response = requests.post(url, headers=headers, data=data, files=files)
    #File name: industry.csv
    #File object: file
#Content type: text/csv
    
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json post request:",json_str)
   # Check login success
    print("Status Code:", response.status_code)
    assert response.status_code == 201

    
# Call function without CSV (safe if file doesn't exist)
add_assignment()