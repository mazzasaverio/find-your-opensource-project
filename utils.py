import requests
import pandas as pd


def fetch_users_by_location(location, max_users, access_token):
    users = []
    page = 1
    headers = {"Authorization": f"token {access_token}"}
    while len(users) < max_users:
        url = f"https://api.github.com/search/users?q=location:{location}&per_page=100&page={page}"
        response = requests.get(url, headers=headers).json()
        batch = response.get("items", [])
        if not batch:
            break
        users.extend(batch[: max_users - len(users)])
        page += 1
    return [user["login"] for user in users]


def fetch_repo_details(username, max_repos, access_token):
    repos = []
    page = 1
    headers = {"Authorization": f"token {access_token}"}
    while len(repos) < max_repos:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers).json()
        if not response:
            break
        repos.extend(response[: max_repos - len(repos)])
        page += 1
    return [
        {
            "repo_name": repo.get("name", ""),
            "username": username,
            "creation_date": repo.get("created_at", ""),
            "stars": repo.get("stargazers_count", 0),
            "forks": repo.get("forks_count", 0),
            "last_update": repo.get("updated_at", ""),
            "description": repo.get("description", ""),
            "topics": repo.get("topics", []),
        }
        for repo in repos
    ]
