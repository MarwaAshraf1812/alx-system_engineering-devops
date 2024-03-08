#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit."""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent header to avoid Too Many Requests issues
    headers = {"User-Agent": "My-User-Agent"}

    try:
        sub_info = requests.get(url, headers=headers, allow_redirects=False)

        if sub_info.status_code >= 300:
            return 0

        # Parse the JSON response and extract the number of subscribers
        data = sub_info.json().get("data")
        if data and "subscribers" in data:
            return data["subscribers"]
        else:
            # Handle the case where the JSON structure is unexpected
            return 0

    except requests.RequestException:
        # Handle any exception that might occur during the request
        return 0
