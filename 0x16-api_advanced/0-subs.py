#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of Reddit subscribers """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALX-APIproject"}

    result = requests.get(url,
                          headers=headers)
    if (result.status_code == 200):
        return result.json().get("data").get("subscribers")
    else:
        return 0
