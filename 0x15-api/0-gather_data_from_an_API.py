#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[2]
    url = 'https://jsonplaceholder.typicode.com/users/'
    res = requests.get(url)
    if res.status_code == 200:
        users = res.json()
        for i in users:
            print(i)
        
    
