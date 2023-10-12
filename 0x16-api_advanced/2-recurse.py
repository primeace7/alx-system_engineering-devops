#!/usr/bin/python3

"""
Recursively fetch the title of all hot posts of a subreddit supplied from
the command line
"""
import requests
import sys


def helper(subreddit, hot_list, name):
    """recursive helper function to get all titles of hot subreddits
    """
    use_name = ''
    url = 'https://www.reddit.com/r/{}/hot.json?raw_json=1&limit=10&after={}'.\
        format(subreddit, name)
    headers = {'user-agent': 'my_alx/0.0.1'}
    fetch = requests.get(url, headers=headers, allow_redirects=False)
    fetch_json = fetch.json()

    if fetch.status_code != 200:
        return None

    children = fetch_json.get('data').get('children')

    for listing in children:
        for key, val in listing.items():
            if key == 'data':
                use_name = val.get('name')
                hot_list.append(val.get('title'))

    if len(children) == 0:
        return hot_list
    else:
        return helper(subreddit, hot_list, use_name)


def recurse(subreddit, hot_list=[]):
    """recursively get and append the hot posts of a subreddit
    """

    output_list = helper(subreddit, hot_list, name='')
    return output_list
