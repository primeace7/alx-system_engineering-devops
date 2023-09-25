#!/usr/bin/python3

"""Fetch employee data from a simple REST API and load into csv file
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])
    response_user = requests.get('{}/users/{}'.format(url, employee_id))

    username = response_user.json().get('username')
    all_tasks = requests.get('{}/todos'.format(url)).json()
    employee_tasks_all = [task for task in all_tasks if
                          task.get('userId') == employee_id]

    output_file = '{}.csv'.format(employee_id)
    with open(output_file, 'w', encoding='utf-8') as csv_output:
        csv_writer = csv.writer(csv_output, quoting=csv.QUOTE_ALL)
        for task in employee_tasks_all:
            completion = task.get('completed')
            title = task.get('title')
            row_data = [employee_id, username, completion, title]
            csv_writer.writerow(row_data)
