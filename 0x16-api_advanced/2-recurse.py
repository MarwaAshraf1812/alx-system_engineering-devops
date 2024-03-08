#!/usr/bin/python3
"""Module for task 2"""


def recurse(subreddit, hot_list=[], after=None, dist=0):
    """Recursively fetch titles of all hot articles for a given subreddit."""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "My-User-Agent"}

    # Initialize dist before using it in params
    dist = dist if dist is not None else 0
    params = {"after": after, "dist": dist, "limit": 100}

    sub_info = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if sub_info.status_code == 404:
        return None

    data = sub_info.json().get("data")
    after = data.get("after")
    dist += data.get("dist")

    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, dist)
    return hot_list
