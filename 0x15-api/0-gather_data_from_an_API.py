#!/usr/bin/python3
'''a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''

import requests
from sys import argv

if __name__ == '__main__':
    employeeId = int(argv[1])
    userUrl = f'https://jsonplaceholder.typicode.com/users/{employeeId}'
    res = requests.get(userUrl)
    if res.status_code == 200:
        users = res.json()
        userName = users['name']

    todoUrl = f'https://jsonplaceholder.typicode.com/todos/?userId={employeeId}'
    res = requests.get(todoUrl)
    if res.status_code == 200:
        todo = res.json()
        no_of_tasks = len(todo)
        completed_task = [x for x in todo if x.get('completed')]
        done_task = len(completed_task)
        print("Employee {} is done with tasks({}/{}):".format(userName, done_task, no_of_tasks))
        for x in completed_task:
            print(f"\t {x.get('title')}")