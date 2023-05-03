#!/usr/bin/python3
"""a Python script that, using this REST API,
for a given employee ID,
returns information about
his/her TODO list progress
"""

import csv
import requests
from sys import argv

def export_to_csv():
    """
    This export to the data to csv
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    employeeId = int(argv[1])
    userUrl = f'https://jsonplaceholder.typicode.com/users/{employeeId}'
    res = requests.get(userUrl)
    if res.status_code == 200:
        users = res.json()
        userName = users['name']

    todoUrl = f'{url}/?userId={employeeId}'
    res = requests.get(todoUrl)
    if res.status_code == 200:
        todo = res.json()
        
        csv_name = "{}.csv".format(employeeId)
        with open(csv_name, "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            # writer.writeheader()
            for task in todo:
                writer.writerow([employeeId, userName, task.get('completed'), task.get('title')])
        

if __name__ == '__main__':
    export_to_csv()