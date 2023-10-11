#!/usr/bin/python3

"""Fetch the title of the first 10 hot posts of a subreddit supplied from
the command line
"""
import sys
import requests


def top_ten(subreddit):
    """get and print the first 10 hot posts of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?raw_json=1'.format(subreddit)
    headers = {'user-agent': 'my_alx/0.0.1'}
    fetch = requests.get(url, headers=headers, allow_redirects=False)
    fetch_json = fetch.json()

    if fetch.status_code != 200:
        print('None')
        return

    children = fetch_json.get('data').get('children')

    count = 0
    for listing in children:
        if count == 9:
            break
        for key, val in listing.items():
            if key == 'data':
                print(val.get('title'))
                count += 1


top_ten(sys.argv[1])
