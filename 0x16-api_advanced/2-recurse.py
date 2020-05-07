#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """Request subreddit recursively using pagination
    """
    # set custom user-agent
    user_agent = '0x16-api_advanced-jmajetich'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # if page specified, pass as parameter
    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    # load response unit from json
    data = r.json()['data']

    # extract list of pages
    posts = data['children']
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
