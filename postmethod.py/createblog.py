import requests
import json

base_url = "https://api.techyversity.com"
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzMxMjQ5OTcsImV4cCI6MTc3MzIxMTM5N30.O6urCSmvB1slflsCnt6AtXY2iCgRQYALamjfZWhKQG0"

def create_blog():
    url = f"{base_url}/api/blog"
    
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }
    
    data = {
        "title": "Importance of Practical Learning in Technology",
        "content": """
In the field of technology, theoretical knowledge alone is not enough. Students must also develop practical skills to understand how systems work in real-world situations.
Practical learning allows students to apply concepts through coding exercises, projects, and real case studies. This helps them gain confidence and experience before entering the job market.
Educational platforms like Techyversity focus on combining theory with practical learning. Through hands-on projects and real-world scenarios, students can develop skills that employers actually look for.
Practical learning not only improves technical knowledge but also strengthens problem-solving and critical thinking abilities.
""",
        "tags": ["online learning", "education", "flexibility", "e-learning", "Techyversity"]
        
    }
    with open("C:\\Users\\Dell\\Pictures\\capture.jpg", "rb") as img:
        files = {"thumbnail": ("blogimage.jpg", img, "image/jpg")}
    


        response = requests.post(url, headers=headers, data=data, files=files)
        json_data=response.json()
        json_str=json.dumps(json_data,indent=4)
        print("json post request:",json_str)
   # Check login success
        print("Status Code:", response.status_code)
        assert response.status_code == 201

    
# Call function without CSV (safe if file doesn't exist)
create_blog()