import sqlite3
import os
import shutil
from colorama import Fore, Style
from msvcrt import getch

def initialize_database():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)')
    conn.commit()
    conn.close()

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

        menu_options = ["Add a new task", "Edit a prexisting task", "Delete a task", "List all current tasks", "Mark task as done", "Exit out of PyOrganize"
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