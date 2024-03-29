#!/usr/bin/python3
"""Gather employee data from API and export to CSV"""

import csv
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
    # e_name = employee_name.json()['name']
    user_name = employee_name.json()['username']

    # Count the total number of completed tasks
    total_tasks = 0

    # Iterate through tasks to count completed tasks
    for com_tasks in json_:
        if com_tasks['completed']:
            total_tasks += 1

    # Generate CSV file name using employee ID
    csv_file = e_id + ".csv"

    # Open the CSV file and write data
    with open(csv_file, "w", newline='') as f:
        f_writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for line in json_:
            f_writing.writerow([e_id, user_name, line.get('completed'),
                                line.get('title')])
