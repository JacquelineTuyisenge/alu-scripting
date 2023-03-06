#!/usr/bin/python3
"""Rwite recursive function and titles oh hot articles."""
import praw


def count_words(subreddit, word_list, count_dict=None, after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given
    keywords. If word_list contains the same word (case-insensitive), the final count should be the sum of each duplicate.
    Results are printed in descending order, by the count, and if the count is the same for separate keywords, they are sorted
    alphabetically (ascending, from A to Z). Words with no matches are skipped and not printed. Words must be printed in lowercase.
    Results are based on the number of times a keyword appears, not titles it appears in. java java java counts as 3 separate occurrences
    of java.
    
    :param subreddit: The subreddit to search
    :param word_list: A list of words to search for
    :param count_dict: A dictionary of keyword counts, used for recursive calls
    :param after: The after parameter for the Reddit API, used for recursive calls
    :return: None
    """
    
    # Initialize count_dict if it's not passed in
    if count_dict is None:
        count_dict = {}
    
    # Initialize the Reddit API client
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    # Make the API call
    try:
        subreddit_obj = reddit.subreddit(subreddit)
        hot_articles = subreddit_obj.hot(limit=100, params={"after": after})
    except praw.exceptions.Redirect as e:
        # Invalid subreddit, do nothing
        return
    
    # Loop through the hot articles
    for article in hot_articles:
        # Split the title into words and lowercase them
        words = article.title.lower().split()

        # Loop through the words and update the count_dict for each word in the word_list
        for word in words:
            # Strip out periods, exclamation points, and underscores at the end of words
            word = word.rstrip('.!_')
            if word in word_list:
                # Add 1 to the count for the word, ignoring case
                count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

        # Recursively call count_words with the next page of articles
        count_words(subreddit, word_list, count_dict, article.name)

    # If we've reached the end of the articles, print the results
    if not after:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
