#!/usr/bin/python3

"""Fetch employee data from a simple REST API
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])
    response_user = requests.get('{}/users/{}'.format(url, employee_id))

    employee_name = response_user.json().get('name')
    all_tasks = requests.get('{}/todos'.format(url)).json()
    employee_tasks_all = [task for task in all_tasks if
                          task.get('userId') == employee_id]
    employee_tasks_done = [task for task in employee_tasks_all if
                           task.get('completed')]
    employee_tasks_count = len(employee_tasks_all)

    print('Employee {} is done with tasks ({}/{}):'.format(
        employee_name, len(employee_tasks_done), employee_tasks_count))
    for task in employee_tasks_done:
        print('\t {}'.format(task['title']))
