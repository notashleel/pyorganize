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

### Display Function

```python
def display_tasks():
    tasks = list_tasks()
    for task in tasks:
        print(f"{task[0]}. {task[1]} [{task[2]}]")
```

### Main Menu

The main function initializes the database and handles user input to navigate through the menu and perform actions.

```python
def main():
    initialize_database()
    current_choice = 1
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    while True:
        os.system('cls')
        terminal_size = shutil.get_terminal_size().columns
        print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
        print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
        print('-' * terminal_size)
        print()

        menu_options = ["Add a new task", "Edit a prexisting task", "Delete a task", "List all current tasks", "Mark task as done", "Exit out of PyOrganize"]
        
        for option in menu_options:
            if current_choice == menu_options.index(option) + 1:
                print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{option}{END}")
            else:
                print(f"    {option}")
        
        i = getch()
        if (i==b'\xe0' or i == b'\x00'):
            j = getch()
            if(j==b'H'):
                current_choice -= 1
            elif(j==b'P'):
                current_choice += 1
            if(current_choice < 1):
                current_choice = 1
            if(current_choice > 6):
                current_choice = 6
        elif i == b'\r':
            if current_choice == 1:
                os.system('cls')
                print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                print('-' * terminal_size)
                print()
                task = input(f'{Fore.LIGHTBLUE_EX}{BOLD}{UNDERLINE}Enter the task{END}:{Fore.RESET} {Fore.LIGHTCYAN_EX}')
                add_task(task)
            if current_choice == 2:
                tasks_pointer = 1
                while True:
                    os.system('cls')
                    task_list = []
                    print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    print(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    for i in list_tasks():
                        task_list.append(i[1])
                    for task in task_list:
                        if tasks_pointer == task_list.index(task) + 1:
                            print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{task}{END}")
                        else:
                            print(f"    {task}")
                    i = getch()
                    if (i==b'\xe0' or i == b'\x00'):
                        j = getch()
                        if(j==b'H'):
                            tasks_pointer -= 1
                        elif(j==b'P'):
                            tasks_pointer += 1
                        if(tasks_pointer < 1):
                            tasks_pointer = 1
                        if(tasks_pointer > len(task_list)):
                            tasks_pointer = len(task_list)
                    elif i == b'\r':
                        os.system('cls')
                        task_id = list_tasks()[tasks_pointer - 1][0]
                        new_task = input(f'{Fore.LIGHTBLUE_EX}{BOLD}{UNDERLINE}Enter the new task{END}:{Fore.RESET} {Fore.LIGHTCYAN_EX}')
                        edit_task(task_id, new_task)
                        break
                    elif i == b'\x1b':
                        break
            if current_choice == 6:
                os.system('cls')
                print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                print('-' * terminal_size)
                print()
                print(f"{Fore.LIGHTRED_EX}{BOLD}Exiting out of PyOrganize...{END}{Fore.RESET}".center(terminal_size))
                break
            if current_choice == 3:
                tasks_pointer = 1
                while True:
                    os.system('cls')
                    task_list = []
                    print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    print(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    for i in list_tasks():
                        task_list.append(i[1])
                    for task in task_list:
                        if tasks_pointer == task_list.index(task) + 1:
                            print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{task}{END}")
                        else:
                            print(f"    {task}")
                    i = getch()
                    if (i==b'\xe0' or i == b'\x00'):
                        j = getch()
                        if(j==b'H'):
                            tasks_pointer -= 1
                        elif(j==b'P'):
                            tasks_pointer += 1
                        if(tasks_pointer < 1):
                            tasks_pointer = 1
                        if(tasks_pointer > len(task_list)):
                            tasks_pointer = len(task_list)
                    elif i == b'\r':
                        os.system('cls')
                        task_id = list_tasks()[tasks_pointer - 1][0]
                        delete_task(task_id)
                        break
                    elif i == b'\x1b':
                        break
            if current_choice == 5:
                tasks_pointer = 1
                while True:
                    os.system('cls')
                    task_list = []
                    print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    print(f'{UNDERLINE

}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    for i in list_tasks():
                        task_list.append(i[1])
                    for task in task_list:
                        if tasks_pointer == task_list.index(task) + 1:
                            print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{task}{END}")
                        else:
                            print(f"    {task}")
                    i = getch()
                    if (i==b'\xe0' or i == b'\x00'):
                        j = getch()
                        if(j==b'H'):
                            tasks_pointer -= 1
                        elif(j==b'P'):
                            tasks_pointer += 1
                        if(tasks_pointer < 1):
                            tasks_pointer = 1
                        if(tasks_pointer > len(task_list)):
                            tasks_pointer = len(task_list)
                    elif i == b'\r':
                        os.system('cls')
                        task_id = list_tasks()[tasks_pointer - 1][0]
                        mark_task_as_done(task_id)
                        break
                    elif i == b'\x1b':
                        break
            if current_choice == 4:
                os.system('cls')
                print(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                print(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                print('-' * terminal_size)
                print()
                print(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                print()
                display_tasks()
                print()
                getch()

if __name__ == "__main__":
    main()
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to adjust any part of this README to better fit your specific needs or preferences!