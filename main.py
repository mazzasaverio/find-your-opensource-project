from utils import fetch_users_by_location, fetch_repo_details
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.environ.get("GITHUB_ACCESS_TOKEN")

locations = ["Milan", "Turin"]  # Add more cities as desired
max_users_per_location = 50
max_repos_per_user = 10

all_repos_info = []

for location in locations:
    users = fetch_users_by_location(
        location, max_users=max_users_per_location, access_token=access_token
    )
    for user in users:
        repos_info = fetch_repo_details(
            user, max_repos=max_repos_per_user, access_token=access_token
        )
        all_repos_info.extend(repos_info)

df = pd.DataFrame(all_repos_info)
df.head()
