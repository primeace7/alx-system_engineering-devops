#!/usr/bin/python3

"""Fetch the number of followers of a subreddit supplied from
the command line
"""
import sys
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json?raw_json=1'.format(subreddit)
    headers = {'user-agent': 'my_alx/0.0.1'}
    fetch = requests.get(url, headers=headers, allow_redirects=False)
    fetch_json = fetch.json()

    if fetch.status_code != 200:
        return 0

    subs = fetch_json.get('data').get('subscribers')
    return subs
