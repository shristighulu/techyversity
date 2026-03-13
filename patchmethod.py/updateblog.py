import requests
import json


#base  url:
base_url="https://api.techyversity.com"
#auth_token
auth_token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTViNTE3MjA4N2NlZTI3YjFhNTI2NjEiLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3NzMxMjQ5OTcsImV4cCI6MTc3MzIxMTM5N30.O6urCSmvB1slflsCnt6AtXY2iCgRQYALamjfZWhKQG0"

#put request
def patch_request():
    url=base_url +f"/api/blog?id=69afc9db00df3ec13a0e651f"
    print("patch url:"+url)
    headers={"Authorization":auth_token}
    data = {
        "title": "Importance of Practical Learning in Technology",
        "content": """
In the field of technology, theoretical knowledge alone is not enough. Students must also develop practical skills to understand how systems work in real-world situations.
Practical learning allows students to apply concepts through coding exercises, projects, and real case studies. This helps them gain confidence and experience before entering the job market.
Educational platforms like Techyversity focus on combining theory with practical learning. Through hands-on projects and real-world scenarios, students can develop skills that employers actually look for.
Practical learning not only improves technical knowledge but also strengthens problem-solving and critical thinking abilities.
""",
        "tags": ["online learning", "education", "flexibility", "e-learning", "Techyversity", "problem-solving"]
        
    }
    response = requests.patch(url, json=data, headers=headers)
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    print("json put request:",json_str)

    if response.status_code == 200:
        print("User updated successfully!")
    else:
        print("Failed to patch user")

  
patch_request()