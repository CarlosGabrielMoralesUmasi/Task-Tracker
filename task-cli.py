import json
import os
import sys
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: task-cli add \"Task description\"")
            sys.exit(1)
        description = sys.argv[2]
        tasks = load_tasks()
        new_id = max([task['id'] for task in tasks], default=0) + 1
        now = datetime.now().isoformat()
        new_task = {
            'id': new_id,
            'description': description,
            'status': 'todo',
            'createdAt': now,
            'updatedAt': now
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task added successfully (ID: {new_id})")

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> \"New task description\"")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid task ID")
            sys.exit(1)
        description = sys.argv[3]
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = description
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task {task_id} updated successfully")
                break
        else:
            print(f"Task with ID {task_id} not found")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid task ID")
            sys.exit(1)
        tasks = load_tasks()
        new_tasks = [task for task in tasks if task['id'] != task_id]
        if len(new_tasks) == len(tasks):
            print(f"Task with ID {task_id} not found")
        else:
            save_tasks(new_tasks)
            print(f"Task {task_id} deleted successfully")

    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <id>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid task ID")
            sys.exit(1)
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'in-progress'
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task {task_id} marked as in progress")
                break
        else:
            print(f"Task with ID {task_id} not found")

    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <id>")
            sys.exit(1)
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid task ID")
            sys.exit(1)
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = 'done'
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task {task_id} marked as done")
                break
        else:
            print(f"Task with ID {task_id} not found")

    elif command == 'list':
        tasks = load_tasks()
        if len(sys.argv) == 3:
            status_filter = sys.argv[2]
            if status_filter not in ['todo', 'in-progress', 'done']:
                print("Invalid status. Use 'todo', 'in-progress', or 'done'")
                sys.exit(1)
            filtered_tasks = [task for task in tasks if task['status'] == status_filter]
        else:
            filtered_tasks = tasks
        if not filtered_tasks:
            print("No tasks found")
        else:
            for task in filtered_tasks:
                print(f"ID: {task['id']}")
                print(f"Description: {task['description']}")
                print(f"Status: {task['status']}")
                print(f"Created At: {task['createdAt']}")
                print(f"Updated At: {task['updatedAt']}")
                print("-" * 20)

    else:
        print(f"Unknown command: {command}")
        print("Available commands: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == '__main__':
    main()
