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

    with open("{}.json".format(USER_ID), "w") as json_file:
        json.dump({USER_ID: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todo_list]}, json_file)
