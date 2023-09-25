#!/usr/bin/python3

"""Fetch employee data from a simple REST API and load all
employee data into json file
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'
    all_employees = requests.get('{}/users'.format(url)).json()
    all_employees_data = []
    for employee in all_employees:
        all_employees_data.append(
            (int(employee.get('id')), employee.get('username'))
        )
    all_employees_tasks = requests.get('{}/todos'.format(url)).json()

    output_file = 'todo_all_employees.json'
    with open(output_file, 'w', encoding='utf-8') as json_output:
        all_employees_tasks_dict = {}
        for data in all_employees_data:
            employee_tasks = [item for item in all_employees_tasks if item.get('userId') == data[0]]
            username = data[1]
            tasks_list = []
            tasks_dict = {}
            for task in employee_tasks:
                tasks_dict.update({'username': username})
                tasks_dict.update({'task': task.get('title')})
                tasks_dict.update({'completed': task.get('completed')})
                tasks_list.append(tasks_dict)
            all_employees_tasks_dict.update({str(data[0]): tasks_list})

        json.dump(all_employees_tasks_dict, json_output)
