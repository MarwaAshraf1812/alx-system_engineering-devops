#!/usr/bin/python3
"""Gather employee data from API"""

import json
import requests
import sys

if __name__ == "__main__":

    # Create a persistent session for making multiple requests efficiently
    sessionR = requests.Session()

    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage:  {} <employee_id>".format(sys.argv[0]))
        exit(1)

    e_id = sys.argv[1]
    id_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(e_id)
    name_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(e_id)

    employee_id = sessionR.get(id_URL)
    employee_name = sessionR.get(name_URL)

    # Convert the json responses to Python dict
    json_ = employee_id.json()

    # Extract the name of employee to display the employee's name when printing
    e_name = employee_name.json()['name']
    user_name = employee_name.json()['username']

    # Count the total number of completed tasks
    total_tasks = []
    j_task_list = {}

    for task in json_:
        total_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_name
        })

    j_task_list[e_id] = total_tasks

    json_file = e_id + ".json"
    with open(json_file, 'w') as f:
        json.dump(j_task_list, f)
