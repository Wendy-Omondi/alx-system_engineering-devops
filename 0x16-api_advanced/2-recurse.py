#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a llist
containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries Reddit API and returns titles list"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "ALX-APIproject"}

    try:
        result = requests.get(url,
                              headers=headers,
                              params={"after": after},
                              allow_redirects=False).json()
    except:
        return None

    if ("data" in result and "children" in result.get("data")):
        for i in result.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in result.get("data") and result.get("data").get("after"):
            return recurse(subreddit, hot_list,
                           result.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
