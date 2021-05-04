#!/usr/bin/python3
"""
    Returns information about a TO DO list progress.
    for a given employee ID using a given REST API.
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo_list = requests.get(url + "todos", params={"userId": argv[1]}).json()
    USER_ID = argv[1]
    USERNAME = user.get('username')

    with open('2.csv', mode='w') as employee_file:
        user_writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            user_writer.writerow([USER_ID, USERNAME, task.get('completed'),
                                  task.get('title')])
