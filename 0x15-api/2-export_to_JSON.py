#!/usr/bin/python3

"""Fetch employee data from a simple REST API and load into csv file
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(sys.argv[1])
    response_user = requests.get('{}/users/{}'.format(url, employee_id))

    username = response_user.json().get('username')
    all_tasks = requests.get('{}/todos'.format(url)).json()
    employee_tasks_all = [task for task in all_tasks if
                          task.get('userId') == employee_id]

    output_file = '{}.json'.format(employee_id)
    with open(output_file, 'w', encoding='utf-8') as json_output:
        tasks_list = []
        for task in employee_tasks_all:
            tasks_dict = {'task': task.get('title')}
            tasks_dict.update({'completed': task.get('completed')})
            tasks_dict.update({'username': username})
            tasks_list.append(tasks_dict)
        json.dump({employee_id: tasks_list}, json_output)
