#!/usr/bin/python3

"""Fetch employee data from a simple REST API and load into csv file
"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'

    def get_username(emp_id):
        """Gets an employees username given their id
        """
        user = requests.get('{}/users/{}'.format(url, emp_id)).json()
        username = user.get('username')
        return username

    def get_emp_tasks(emp_id, username):
        """Gets all tasks for a particular employee and returns them
        as a list of dicts
        """
        employee_id = emp_id
        all_tasks = requests.get('{}/todos'.format(url)).json()
        employee_tasks_all = [task for task in all_tasks if
                              task.get('userId') == employee_id]

        tasks_list = []
        for task in employee_tasks_all:
            tasks_dict = {'username': username}
            tasks_dict.update({'task': task.get('title')})
            tasks_dict.update({'completed': task.get('completed')})
            tasks_list.append(tasks_dict)
        return tasks_list

    all_employees = requests.get('{}/users'.format(url)).json()
    all_emp_ids = [emp.get('id') for emp in all_employees]
    all_tasks_dict = {}
    for emp_id in all_emp_ids:
        username = get_username(emp_id)
        tasks = get_emp_tasks(emp_id, username)
        all_tasks_dict.update({str(emp_id): tasks})

    output_file = 'todo_all_employees.json'
    with open(output_file, 'w', encoding='utf-8') as json_output:
        json.dump(all_tasks_dict, json_output)
