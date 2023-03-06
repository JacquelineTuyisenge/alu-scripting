#!/usr/bin/python3
""" print titles of first ten hot posts listed for a given subreddit """
import requests


def top_ten(subreddit)
    """ print titles of ten hot posts listed """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'mozilla/5.0'}
    response = requests.get(url, allow_reddits=False)

    if response.status_code != 200:
        print(None)
        return
    posts = response.json()["data"]["immature"]
    for post in posts
        print(post["data"]["title"])
