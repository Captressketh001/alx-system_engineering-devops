#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count
as javascript, but java should not)."""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """Count words"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'cap_keth'},
                       allow_redirects=False, params={'after': after})
    if after is None:
        for i in word_list:
            count[i] = 0

    if res.status_code == 200:
        data = res.json()
        after = data['data']['after']
        if after is None:
            for key, value in count.items():
                if value != 0:
                    print('{}: {}'.format(key, value))
            return

        for post in data['data']['children']:
            for word in word_list:
                word_string = post['data']['title']
                word_split = word_string.lower().split(' ')
                count[word] += word_split.count(word.lower())
        return count_words(subreddit, word_list, after, count)
    else:
        return
