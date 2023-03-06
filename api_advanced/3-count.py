#!/usr/bin/python3

""" 3-count.py """
import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """ prints a sorted count of given keywords """

    # Base case: when there are no more articles to parse
    if after == '':
        # Sort the word count in descending order by count, and then in ascending order alphabetically
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        # Print the word count for each keyword
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
        return

    # Set up the parameters for the API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    # Make the API request
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error {response.status_code}: Could not fetch data from Reddit API")
        return

    # Parse the JSON data in the response
    data = response.json()

    # Extract the titles of the articles and count the occurrence of each keyword
    for post in data["data"]["children"]:
        title = post["data"]["title"]
        for word in word_list:
            # Check if the word appears in the title (case-insensitive)
            # You may need to modify this check to exclude words that contain the keyword (e.g. java. or java!)
            if word.lower() in title.lower():
                # Add the count to the word count dictionary
                if word.lower() in word_count:
                    word_count[word.lower()] += title.lower().count(word.lower())
                else:
                    word_count[word.lower()] = title.lower().count(word.lower())

    # Recursively call the function with the next "after" parameter to get the next set of articles
    after = data["data"]["after"]
    count_words(subreddit, word_list, after, word_count)
