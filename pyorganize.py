import sqlite3
import os
import shutil
from colorama import Fore, Style
from msvcrt import getch
import re
from prettytable import PrettyTable
from term_piechart import Pie

def initialize_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)')
    conn.commit()
    conn.close()

def pending_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE status = ?', ('Pending',))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def tasks_done():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(id) FROM tasks WHERE status = ?', ('Done',))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def list_all_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY status DESC')
    tasks = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ["ID", "Task"]
    for i in tasks:
        table.add_row([i[0], i[1]])
    i = table.get_string()
    for j in i.split('\n'):
        printCenter(j)

def list_pending_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE status = ?', ('Pending',))
    tasks = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ["ID", "Task"]
    for i in tasks:
        table.add_row([i[0], i[1]])
    i = table.get_string()
    for j in i.split('\n'):
        printCenter(j)

def list_done_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE status = ?', ('Done',))
    tasks = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ["ID", "Task"]
    for i in tasks:
        table.add_row([i[0], i[1]])
    i = table.get_string()
    for j in i.split('\n'):
        printCenter(j)
        
        

def tasks_pending():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(id) FROM tasks WHERE status = ?', ('Pending',))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def add_task(task):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, status) VALUES (?, ?)', (task, 'Pending'))
    conn.commit()
    conn.close()

def edit_task(task_id, new_task):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def list_tasks():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task, status FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_task_as_done(task_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', ('Done', task_id))
    conn.commit()
    conn.close()

def display_tasks():
    tasks = list_tasks()
    for task in tasks:
        print(f"{task[0]}. {task[1]} [{task[2]}]")

def visible_length(text):
    return len(re.sub(r'\x1B[@-_][0-?]*[ -/]*[@-~]', '', text))

def printCenter(text):
    terminal_size = shutil.get_terminal_size().columns
    padding = (terminal_size - visible_length(text)) // 2
    print(' ' * padding + text)

def main():
    initialize_database()
    current_choice = 1
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    while True:
        os.system('cls')
        terminal_size = shutil.get_terminal_size().columns
        tasks_done_num = tasks_done()[0][0]
        tasks_pending_num = tasks_pending()[0][0]
        percentage = 0
        if tasks_done_num + tasks_pending_num != 0:
            percentage = (tasks_done_num / (tasks_done_num + tasks_pending_num)) * 100
        progress_bar = "█" * int(percentage / 2)
        progress_bar = f'{Fore.LIGHTBLUE_EX}{progress_bar}{Fore.RESET}'
        progress_bar += " " * (50 - int(percentage / 2))
        printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}")
        printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
        print('-' * terminal_size)
        print()
        printCenter(f'{BOLD}Progress:{END} |{progress_bar}| {int(percentage)}%'.center(terminal_size))
        print()
        printCenter(f'{UNDERLINE}{Fore.CYAN}Press {BOLD}↑ and ↓ arrow keys{END}{UNDERLINE}{Fore.CYAN} to go navigate through the menu{Fore.RESET}{END}'.center(terminal_size))
        print()
        print()

        menu_options = ["Add a new task", "Edit a prexisting task", "Delete a task", "List all current tasks", "Visualize your progress", "Mark task as done", "Exit out of PyOrganize"
        ]
        
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
            if(current_choice > 7):
                current_choice = 7
        elif i == b'\r':
            if current_choice == 1:
                os.system('cls')
                printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                print('-' * terminal_size)
                print()
                printCenter(f'{UNDERLINE}{Fore.RED}Press {BOLD}ENTER{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                print()
                task = input(f'{Fore.LIGHTBLUE_EX}{BOLD}{UNDERLINE}Enter the task{END}:{Fore.RESET} {Fore.LIGHTCYAN_EX}')
                if task != '':
                    add_task(task)
            if current_choice == 2:
                tasks_pointer = 1
                while True:
                    os.system('cls')
                    task_list = []
                    printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    printCenter(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    for i in list_tasks():
                        task_list.append(i[1])
                    for task in range(len(task_list)):
                        if tasks_pointer == task + 1:
                            print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{task_list[task]}{END}")
                        else:
                            print(f"    {task_list[task]}")
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
            if current_choice == 7:
                os.system('cls')
                printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                print('-' * terminal_size)
                print()
                printCenter(f"{Fore.LIGHTRED_EX}{BOLD}Exiting out of PyOrganize...{END}{Fore.RESET}".center(terminal_size))
                break
            if current_choice == 3:
                tasks_pointer = 1
                while True:
                    os.system('cls')
                    task_list = []
                    printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    printCenter(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    for i in list_tasks():
                        task_list.append(i[1])
                    for task in range(len(task_list)):
                        if tasks_pointer == task + 1:
                            print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{task_list[task]}{END}")
                        else:
                            print(f"    {task_list[task]}")
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
            if current_choice == 6:
                tasks_pointer = 1
                while True:
                    os.system('cls')
                    printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    printCenter('-' * terminal_size)
                    print()
                    printCenter(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    if (pending_tasks() == []):
                        printCenter(f"{Fore.LIGHTRED_EX}{BOLD}There are currently no pending tasks!{END}{Fore.RESET}".center(terminal_size))
                        i = getch()
                        if i == b'\x1b':
                            break
                        else:
                            continue
                    else:
                        id_list = []
                        name_list = []
                        pending_tasks_list = pending_tasks()
                        for task in pending_tasks_list:
                            id_list.append(task[0])
                            name_list.append(task[1])
                        for task in range(len(name_list)):
                            if tasks_pointer == task + 1:
                                print(f"{Fore.LIGHTBLUE_EX}>> {BOLD}{UNDERLINE}{name_list[task]}{END}")
                            else:
                                print(f"    {name_list[task]}")
                        i = getch()
                        if (i==b'\xe0' or i == b'\x00'):
                            j = getch()
                            if(j==b'H'):
                                tasks_pointer -= 1
                            elif(j==b'P'):
                                tasks_pointer += 1
                            if(tasks_pointer < 1):
                                tasks_pointer = 1
                            if(tasks_pointer > len(name_list)):
                                tasks_pointer = len(name_list)
                        elif i == b'\r':
                            os.system('cls')
                            task_id = id_list[tasks_pointer - 1]
                            mark_task_as_done(task_id)
                            break
                        elif i == b'\x1b':
                            break
            if current_choice == 4:
                category_pointer = 0
                while True:
                    os.system('cls')
                    printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    printCenter(f'{UNDERLINE}{Fore.RED}Press {BOLD}←, → and ESC{END}{UNDERLINE}{Fore.RED} keys to navigate through this menu{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    categories = ["All tasks", "Pending tasks", "Done tasks"]
                    for category in range(len(categories)):
                        if category == category_pointer:
                            categories[category_pointer] = f"{Fore.LIGHTBLUE_EX}{BOLD}{UNDERLINE}{categories[category]}{END}"
                    header = ''
                    for i in range(len(categories)):
                        if i == len(categories) - 1:
                            header += categories[i]
                        else:
                            header += categories[i] + " | "
                    printCenter(header)
                    if (category_pointer==0):
                        print()
                        list_all_tasks()
                    elif (category_pointer==1):
                        print()
                        list_pending_tasks()
                    elif (category_pointer==2):
                        print()
                        list_done_tasks()
                    i = getch()
                    if (i==b'\xe0' or i == b'\x00'):
                        j = getch()
                        if(j==b'K'):
                            category_pointer -= 1
                        elif(j==b'M'):
                            category_pointer += 1
                        if(category_pointer < 0):
                            category_pointer = 0
                        if(category_pointer > len(categories) - 1):
                            category_pointer = len(categories) - 1
                    elif i == b'\x1b':
                        break   
            if current_choice == 5:
                while True:
                    os.system('cls')
                    printCenter(f"{Fore.CYAN}Py{Style.BRIGHT}{Fore.BLUE}Organize{Style.RESET_ALL}".center(terminal_size))
                    printCenter(f"{Style.DIM}{Fore.CYAN}A user-friendly Python app to organize, track, and manage your to-do lists efficiently!{Style.RESET_ALL}".center(terminal_size))
                    print('-' * terminal_size)
                    print()
                    printCenter(f'{UNDERLINE}{Fore.RED}Press {BOLD}ESC{END}{UNDERLINE}{Fore.RED} to go back{Fore.RESET}{END}'.center(terminal_size))
                    print()
                    tasks_done_num = tasks_done()[0][0]
                    tasks_pending_num = tasks_pending()[0][0]
                    requests = [
                        {"name": "Completed", "value": tasks_done_num, "color": "cyan"},
                        {"name": "Pending", "value": tasks_pending_num, "color": "grey"},
                    ]
                    pie = Pie(
                    requests,
                    radius=5,
                    legend={"line": 0, "format": "{label} {name} {percent:>5.2f}%"},
                    )
                    print(pie)
                    i = getch()
                    if i == b'\x1b':
                        break   







if __name__ == "__main__":
    main()
