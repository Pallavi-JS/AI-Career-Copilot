import requests

def fetch_jobs():

    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)

    data = response.json()

    return data["jobs"][:50]