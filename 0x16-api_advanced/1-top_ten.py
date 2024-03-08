#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 10}

    sub_info = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        print('None')
        return

    posts = sub_info.json().get("data", {}).get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title")
        print(title)
