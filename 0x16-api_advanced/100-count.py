#!/usr/bin/python3

"""
Query reddit API and parse the title of all hot articles, and count the number
of all given keywords in sorted order
"""
from operator import itemgetter
import requests
import sys


def helper(subreddit, hot_dict, name, word_list):
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
                title_words = val.get('title').lower().split()
                for word in title_words:
                    for token in word_list:
                        if token == word:
                            if word in hot_dict:
                                hot_dict[word] += 1
                            else:
                                hot_dict[word] = 1

    if len(children) == 0:
        return hot_dict
    else:
        return helper(subreddit, hot_dict, use_name, word_list)


def count_words(subreddit, word_list):
    """count and print the number of occurences of each word in word_list
    in all hot titles of subreddit
    """

    split_list = word_list.split()
    word_list = [word.lower() for word in split_list]
    output_dict = helper(subreddit, hot_dict={}, name='', word_list=word_list)

    # get a dict of the keywords that have at least 1 occurrence
    sorted_list = sorted(output_dict.items(),
                         key=itemgetter(1, 0), reverse=True)
    for item in sorted_list:
        print('{}: {}'.format(item[0], item[1]))
