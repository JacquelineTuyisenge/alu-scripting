#!/usr/bin/python3
"""
write recursive functions and list of hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns list with titles of hot articles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        if data["after"] is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data["after"])
    elif response.status_code == 404:
        return None
