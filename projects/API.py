import requests

url = "https://jsearch.p.rapidapi.com/search-v2"

role = input("Enter job role to search: ")
querystring = {"query":role,
               "num_pages":"1",
               "country":"us",
               "date_posted":"all"}

headers = {
	"x-rapidapi-key": "85edb7469fmsh3f449a81d084be5p13a5f3jsn1d6043b24171",
	"x-rapidapi-host": "jsearch.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)


data = response.json()
jobs = data['data']['jobs']

print(f"\n Found {len(jobs)} jobs\n")

for job in jobs:
    print(f"Role: {job['job_title']}")
    print(f"Company: {job['employer_name']}")
    print(f"Location: {job['job_location']}")
    print("-" * 40)

all_skills = []
common_skills = ["python", "sql", "java", "javascript", "aws", "docker", 
                 "git", "api", "django", "fastapi", "react", "mongodb"]

for job in jobs:
    description = job['job_description'].lower()
    for skill in common_skills:
        if skill in description:
            all_skills.append(skill)

print("\n Top Skills Companies Are Looking For:\n")
for skill in common_skills:
    count = all_skills.count(skill)
    if count > 0:
        bar = "📝" * count
        print(f"{skill.upper():12} {bar} ({count} jobs)")