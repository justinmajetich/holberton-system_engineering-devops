#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests


def count_words(subreddit, word_list, count_list=[], next_page=None):
    """Request subreddit recursively using pagination
    """
    # convert word_list to dict with count
    if not count_list:
        for word in word_list:
            count_list.append(dict({'keyword': word,
                                    'count': 0}))

    # NETWORKING
    # set custom user-agent
    user_agent = '0x16-api_advanced-jmajetich'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # if page specified, pass as parameter
    if next_page:
        url += '?after={}'.format(next_page)

    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    # DATA PARSING
    # load response unit from json
    data = r.json()['data']

    # extract list of pages
    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        # sort list by count
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)
        keywords_matched = 0
        # print keywords and counts
        for word in sorted_list:
            if word['count'] > 0:
                print('{}: {}'.format(word['keyword'], word['count']))
                keywords_matched += 1
        return
