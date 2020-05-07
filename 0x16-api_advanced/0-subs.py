#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    # set custom user-agent
    user_agent = '0x16-api_advanced-jmajetich'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers)

    # load response unit from json
    data = r.json()['data']
    # extract list of pages
    pages = data['children']
    # check if list has contents
    if not pages:
        return 0
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subreddit_subscribers']
