#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Returns top 10 titles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "ALX-APIproject"}

    result = requests.get(url,
                          headers=headers,
                          params={"limit": "10"})

    if (result.status_code == 200):
        for post in result.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
