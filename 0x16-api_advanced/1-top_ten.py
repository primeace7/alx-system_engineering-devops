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

    children = fetch_json.get('data').get('children')

    for i in range(10):
        for listing in children:
            for key, val in listing.items():
                if key == 'data':
                    print(val.get('title'))


top_ten(sys.argv[1])
