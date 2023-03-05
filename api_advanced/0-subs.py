#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}  # custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        return data["subscribers"]
    else:
        return 0

