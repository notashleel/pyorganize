# PyOrganize

**PyOrganize** is a user-friendly Python application designed to help you organize, track, and manage your to-do lists efficiently. With a simple terminal-based interface and SQLite for data storage, you can easily add, edit, delete, list, and mark tasks as done.

## Features

- **Add Task**: Quickly add new tasks to your list.
- **Edit Task**: Modify existing tasks to keep your list up-to-date.
- **Delete Task**: Remove tasks that are no longer needed.
- **List Tasks**: Display all current tasks along with their status.
- **Mark Task as Done**: Mark tasks as completed to keep track of your progress.
- **User-Friendly Interface**: Navigate through options easily with a terminal-based menu.

## Installation

1. Clone the repository or download the source code.
2. Make sure you have Python installed (preferably version 3.6 or higher).
3. Install the required libraries using pip:
    ```sh
    pip install colorama
    pip install prettytable
    ```

## Usage

1. Navigate to the directory containing the source code.
2. Run the application:
    ```sh
    python pyorganize.py
    ```
3. Use the arrow keys to navigate through the menu and press Enter to select an option.
4. Follow the prompts to add, edit, delete, list, or mark tasks as done.

## Code Overview

### Database Initialization

The database is initialized with a table named `tasks` containing columns for task ID, task description, and task status.

```python
def initialize_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)')
    conn.commit()
    conn.close()
```

### Task Management Functions

- **add_task**: Adds a new task with a 'Pending' status.
- **edit_task**: Edits the task description based on the task ID.
- **delete_task**: Deletes a task based on the task ID.
- **list_tasks**: Retrieves all tasks from the database.
- **mark_task_as_done**: Updates the status of a task to 'Done'.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

---