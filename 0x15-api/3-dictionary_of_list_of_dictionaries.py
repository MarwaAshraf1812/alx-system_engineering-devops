#!/usr/bin/python3
"""for a given employee ID, this script returns
information about his/her TODO list progress."""

import json
import requests


if __name__ == "__main__":

    all_users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = all_users.json()
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = to_do.json()

    all_to_do = {}

    for user in users:
        user_tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                user_tasks.append(task_dict)
        all_to_do[user.get('id')] = user_tasks


    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_to_do, f)
