#!/usr/bin/python3
""" 2-recurse.py """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns list with titles of all hot articles in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {"limit": 100, "after": after}
    response = requests.get(
                            url, 
                            headers=headers, 
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]
        hot_list += [post["data"]["title"] for post in data["children"]]
        if data["after"] is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data["after"])
    elif response.status_code == 404:
        return None
