#!/usr/bin/python3
"""Request employee ID from API
"""

from json import dump
import requests
from sys import argv

if __name__ == "__main__":

    def make_request(resource, param=None):
        """Retrieve user from API
        """
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if param:
            url += ('?' + param[0] + '=' + param[1])

        # make request
        r = requests.get(url)

        # extract json response
        r = r.json()
        return r

    user = make_request('users', ('id', argv[1]))[0]
    tasks = make_request('todos', ('userId', argv[1]))

    # format before exporting
    user_id = user['id']
    export = {user_id: []}
    for task in tasks:
        export[user_id].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': user['username']})

    filename = argv[1] + '.json'
    with open(filename, mode='w') as f:
        dump(export, f)
