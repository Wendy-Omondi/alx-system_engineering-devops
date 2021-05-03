#!/usr/bin/python3
"""
    Returns information about a TO DO list progress.
    for a given employee ID using a given REST API.
"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    todo_list = requests.get(url + "todos").json()

    dict_list = {item.get("id"):
                 [{"task": j.get("title"),
                     "completed": j.get("completed"),
                     "username": item.get("username")}
                     for j in todo_list
                     if j.get("USER_ID") == item.get("id")]
                 for item in user}

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dict_list, f)
