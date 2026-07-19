import requests

from indian_jobs import fetch_indian_jobs


def fetch_remote_jobs():

    try:

        url = "https://remotive.com/api/remote-jobs"

        response = requests.get(
            url,
            timeout=20
        )

        data = response.json()

        remote_jobs = []

        for job in data.get("jobs", [])[:30]:

            remote_jobs.append({

                "title": job.get(
                    "title",
                    "Unknown Job"
                ),

                "company_name": job.get(
                    "company_name",
                    "Unknown Company"
                ),

                "location": "Remote / International",

                "description": job.get(
                    "description",
                    ""
                ),

                "url": job.get(
                    "url",
                    ""
                )

            })

        return remote_jobs

    except Exception as e:

        print(
            "Remote jobs error:",
            e
        )

        return []


def fetch_jobs():

    # Get Indian jobs
    indian_jobs = fetch_indian_jobs()

    # Get international remote jobs
    remote_jobs = fetch_remote_jobs()

    # Combine both
    all_jobs = indian_jobs + remote_jobs

    print(
        "Indian jobs:",
        len(indian_jobs)
    )

    print(
        "Remote jobs:",
        len(remote_jobs)
    )

    return all_jobs