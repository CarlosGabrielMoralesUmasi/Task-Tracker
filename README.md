
# Task CLI

A simple command-line interface (CLI) for managing tasks using a JSON file as storage. This tool allows you to add, update, delete, and manage the status of tasks.

## Features

- Add a new task with a description.
- Update an existing task's description.
- Delete a task by its ID.
- Mark tasks as "in-progress" or "done".
- List all tasks or filter tasks by their status.

## Prerequisites

- Python 3.x

## Usage

To run the CLI, use the following syntax:

```bash
python task-cli.py <command> [<args>]
```

### Commands

1. **Add a Task**

   Add a new task with a description.
   ```bash
   python task-cli.py add "Task description"
   ```
   **Example:**
   ```bash
   python task-cli.py add "Buy groceries"
   ```

2. **Update a Task**

   Update the description of an existing task by ID.
   ```bash
   python task-cli.py update <id> "New task description"
   ```
   **Example:**
   ```bash
   python task-cli.py update 1 "Buy groceries and cook dinner"
   ```

3. **Delete a Task**

   Delete a task by its ID.
   ```bash
   python task-cli.py delete <id>
   ```
   **Example:**
   ```bash
   python task-cli.py delete 1
   ```

4. **Mark a Task as In Progress**

   Mark a task as "in-progress" by ID.
   ```bash
   python task-cli.py mark-in-progress <id>
   ```
   **Example:**
   ```bash
   python task-cli.py mark-in-progress 1
   ```

5. **Mark a Task as Done**

   Mark a task as "done" by ID.
   ```bash
   python task-cli.py mark-done <id>
   ```
   **Example:**
   ```bash
   python task-cli.py mark-done 1
   ```

6. **List All Tasks**

   List all tasks or filter by status (`todo`, `in-progress`, `done`).
   ```bash
   python task-cli.py list
   python task-cli.py list <status>
   ```
   **Examples:**
   ```bash
   python task-cli.py list
   python task-cli.py list done
   python task-cli.py list todo
   ```

## File Structure

- `tasks.json`: JSON file where tasks are stored. This file is automatically created in the same directory if it does not exist.

## Example Workflow

```bash
# Add a new task
python task-cli.py add "Complete project documentation"

# List all tasks
python task-cli.py list

# Update a task
python task-cli.py update 1 "Complete and review project documentation"

# Mark a task as in-progress
python task-cli.py mark-in-progress 1

# Mark a task as done
python task-cli.py mark-done 1

# List tasks by status
python task-cli.py list done
```

