#!/usr/bin/python3

import requests
from sys import argv
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo_list = requests.get(url + "todos", params={"userId": argv[1]}).json()
    USER_ID = argv[1]
    USERNAME = user.get('username')
    TASK_TITLE = []
    TASKS = {}

    for item in todo_list:
        task = {}
        task['task'] = item.get('title')
        task['completed'] = item.get('completed')
        task['username'] = USERNAME
        TASK_TITLE.append(task)

    TASKS[USER_ID] = TASK_TITLE

    with open("{:}.json".format(USER_ID), 'w') as f:
        json.dump(TASKS, f)
