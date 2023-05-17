#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Find subreddits"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'cap_keth'},
                       allow_redirects=False, params={'after': after})
    if res.status_code == 200:
        data = res.json()
        after = data['data']['after']
        if after is None:
            return hot_list
        
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    pass
