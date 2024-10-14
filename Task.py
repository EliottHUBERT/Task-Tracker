from datetime import datetime
import json
import os

class Task:
    def __init__(self, id, description, tasks, status='todo'):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
        self.tasks = tasks 

    def update_status(self, new_status):
        self.status = new_status
        self.updatedAt = datetime.now()
        self.save()

    def update_description(self, new_description):
        self.description = new_description
        self.updatedAt = datetime.now()
        self.save()

    def __repr__(self):
        return (f"Task(id={self.id}, description={self.description}, "
                f"status={self.status}, createdAt={self.createdAt}, "
                f"updatedAt={self.updatedAt})")

    def save(self):
        task_data = {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.updatedAt.isoformat()
        }

        task_found = False
        for i, task in enumerate(self.tasks):
            if task['id'] == self.id:
                self.tasks[i] = task_data
                task_found = True
                break

        if not task_found:
            self.tasks.append(task_data)

        with open('Tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)


def load_tasks():
    if os.path.exists('Tasks.json'):
        try:
            with open('Tasks.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []