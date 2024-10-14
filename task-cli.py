import argparse
from Task import Task, load_tasks
import json
def add_task(description):
    tasks = load_tasks()
    max_id = max(task['id'] for task in tasks) + 1 if tasks else 1
    task = Task(max_id, description, tasks)
    task.save()
    print(f'Task added successfully (ID: {task.id})')

def update_task(task_id, description):
    tasks = load_tasks()
    for task_data in tasks:
        if task_data['id'] == task_id:
            task = Task(task_data['id'], task_data['description'], tasks, task_data['status'])
            task.update_description(description)
            print(f'Task updated successfully (ID: {task.id})')
            return
    print(f'Task with id {task_id} not found.')

def delete_task(task_id):
    tasks = load_tasks()
    for task_data in tasks:
        if task_data['id'] == task_id:
            tasks.remove(task_data)
            with open('Tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            print(f'Task deleted successfully (ID: {task_id})')
            return
    print(f'Task with id {task_id} not found.')

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task_data in tasks:
        if task_data['id'] == task_id:
            task = Task(task_data['id'], task_data['description'], tasks, task_data['status'])
            task.update_status('in-progress')
            print(f'Task marked in progress successfully (ID: {task.id})')
            return
    print(f'Task with id {task_id} not found.')

def mark_done(task_id):
    tasks = load_tasks()
    for task_data in tasks:
        if task_data['id'] == task_id:
            task = Task(task_data['id'], task_data['description'], tasks, task_data['status'])
            task.update_status('done')
            print(f'Task marked done successfully (ID: {task.id})')
            return
    print(f'Task with id {task_id} not found.')

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"Task ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

parser = argparse.ArgumentParser(description='Task CLI')
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('description')

update_parser = subparsers.add_parser('update')
update_parser.add_argument('task_id', type=int)
update_parser.add_argument('description')

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('task_id', type=int)

mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
mark_in_progress_parser.add_argument('task_id', type=int)

mark_done_parser = subparsers.add_parser('mark-done')
mark_done_parser.add_argument('task_id', type=int)

list_parser = subparsers.add_parser('list')
list_parser.add_argument('status', nargs='?', choices=['done', 'todo', 'in-progress'])

args = parser.parse_args()

match args.command:
    case 'add':
        add_task(args.description)
    case 'update':
        update_task(args.task_id, args.description)
    case 'delete':
        delete_task(args.task_id)
        pass
    case 'mark-in-progress':
        mark_in_progress(args.task_id)
        pass
    case 'mark-done':
        mark_done(args.task_id)
        pass
    case 'list':
        list_tasks(args.status)
        pass
