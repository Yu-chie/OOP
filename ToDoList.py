### To Do List ###

#Import necessary libraries (optional, if using color or formatting)

import time
import os
from colorama import Fore, Style, init

#Initialize colorama
init()

#Load Starting Text
#print(Fore.CYAN + "Hi! Welcome to the simple To-Do List" + Style.RESET_ALL)
#username = input("Enter a Username: ").strip()
#print(Fore.GREEN + f"Welcome, {username}! Let's Get Started!" + Style.RESET_ALL)

tasks = []       # List to store tasks

#Clear the console screen
def clear_console():     
    os.system("cls" if os.name == "nt" else "clear")

#Status Color
def get_status_color(status):
    color_map = {
        "Not Started": Fore.LIGHTWHITE_EX,
        "In Progress": Fore.BLUE,
        "On Hold": Fore.YELLOW,
        "Completed": Fore.GREEN,
        "Waiting for Review": Fore.MAGENTA,
        "Needs Revision": Fore.RED
    }
    return color_map.get(status, Fore.WHITE)

#Display Progress
def task_progress():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["status"] == "Completed")
    if total_tasks == 0:
        print()
        return

    percent_done = int((completed_tasks / total_tasks) * 100)
    progress_bar = "█" * (percent_done // 10) + "░" * (10 - (percent_done // 10))
    print(Fore.GREEN + f"Progress: [{progress_bar}] {percent_done}% completed!" + Style.RESET_ALL)

#Display Tasks
def display_task():     
    if not tasks:
        print(Fore.RED + "\n No tasks available" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + Style.BRIGHT + "\n================= Task List =================" + Style.RESET_ALL)
        for index, task in enumerate(tasks, start=1):
            status_color = get_status_color(task["status"])
            print(f"{index}. {task['name']}     |    Status: {status_color}{task['status']}{Style.RESET_ALL}    |   Due: {task['due_date']}")
        print(Fore.CYAN + Style.BRIGHT + "===========================================" + Style.RESET_ALL)

# Main Menu (Task List + Menu)
## - Display all task in a neat format with status and due date.
## - Show menu options directly below the task list.
##   - 1. Add Task
##   - 2. Delete Task
##   - 3. Edit Task
##   - 4. Update Task Status
##   - 0. Exit
def display_menu():     #Display task list and status along with menu options
    clear_console()
    task_progress()
    display_task()
    print(Fore.CYAN + Style.BRIGHT + "\n========== To-Do List Menu ==========" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "1." + Style.RESET_ALL + " Add Task")
    print(Fore.GREEN + Style.BRIGHT + "2." + Style.RESET_ALL + " Delete Task")
    print(Fore.GREEN + Style.BRIGHT + "3." + Style.RESET_ALL + " Edit Task")
    print(Fore.GREEN + Style.BRIGHT + "4." + Style.RESET_ALL + " Update Task Status")
    print(Fore.RED + Style.BRIGHT + "0." + Style.RESET_ALL + " Exit")
    print(Fore.CYAN + Style.BRIGHT + "=====================================" + Style.RESET_ALL)

#Adding Task
## - Ask user for Task name
## - Ask user for Task Due Date (Optional)
## - Ask user for Task Details (optional)
## - Add Task to the list with default status
def add_task():
    print("\nAdding a task...")
    try:
        n_task = int(input("How many tasks do you wish to add?: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    for i in range(n_task):
        name = input("\nEnter task name: ").strip()       #Get Task from User
        due_date = input("Enter due date (or press Enter to skip): ") or "No due date"
        
        task = {
            "name": name,
            "status": "Not Started",  # Default status
            "due_date": due_date
        }
        tasks.append(task)  # Add to list
        print(f"Task '{name}' added successfully!")

    time.sleep(1)

#Deleting Task
## - Ask user for task name to remove
## - Ask user for confirmation
## - If task exists, remove it from the list.
## - If not found, show an error message.
def delete_task():
    clear_console()
    print("\nDeleting a task...")
    if not tasks:
        print("No task available to delete")
        time.sleep(1)
        return

    display_task()

    while True:
        try:
            task_num = int(input("Enter a task number to delete or 0 to cancel: ")) - 1

            if task_num == -1:
                print("Task Deletion Cancelled")
                time.sleep(1)
                return

            if 0 <= task_num < len(tasks):
                confirm = input(f"Are you sure you want to delete '{tasks[task_num]['name']}'? (y/n): ").lower()
                if confirm == 'y':
                    deleted_task = tasks.pop(task_num)
                    print(f"Task '{deleted_task['name']}' deleted successfully!")
                    time.sleep(1)
                    return
                else:
                    print("Task deletion cancelled.")
                    time.sleep(1)
                    return
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid input! Enter a number")
            continue

    time.sleep(1)

# Editing Task Name
## - Ask user which task they want to rename.
## - Allow user to enter a new name.
## - Update the task name in the list.
def edit_task():
    clear_console()
    print("\nEditing a task...")

    if not tasks:
        print("No task available to edit")
        time.sleep(1)
        return

    display_task()

    try:
        task_num = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):          
            while True:
                print("\nWhat would you like to edit?")
                print(Fore.CYAN + "1." + Style.RESET_ALL + "Edit Task Name")
                print(Fore.CYAN + "2." + Style.RESET_ALL + "Task Due Date" )
                print(Fore.RED + "0." + Style.RESET_ALL + "Cancel")
                
                try:
                    option = int(input("\nEnter your choice: "))        # Convert input to an integer
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
                    time.sleep(1)
                    continue        # Restart the loop if input is invalid

                if option == 1:
                    new_name = input("Enter new task name: ").strip()
                    if new_name:
                        tasks[task_num]["name"] = new_name
                        print("Task name updated successfully!")
                        break
                    else:
                        print(Fore.RED + "Task Name Cannot Be Empty" + Style.RESET_ALL)
                        continue #Test
                if option == 2:
                    new_due = input("Enter a new Due Date: ").strip()
                    tasks[task_num]["due_date"] = new_due
                    print("Due Date updated sucessfully!")
                    break
                if option == 0:
                    print(Fore.YELLOW + "Edit Cancelled" + Style.RESET_ALL)
                    time.sleep(1)
                    break
            time.sleep(1)
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Enter a number.")      

    time.sleep(1)


#Task Status
##   🔹 Not Started – Default status when a task is added.
##   🔹 In Progress – Task is currently being worked on.
##   🔹 On Hold – Task is temporarily paused.
##   🔹 Completed – Task is fully done.
##   🔹 Waiting for Review – Task is done but needs checking.
##   🔹 Needs Revision – Task requires changes before completion.
status_options = [
    "Not Started", "In Progress", "On Hold", "Completed", 
    "Waiting for Review", "Needs Revision"
]

#Loading Animation
import sys

def loading_animation(message="Processing"):
    print(Fore.YELLOW + message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(Style.RESET_ALL)

# Updating Task Status
## - Ask user which task to update.
## - Show list of possible statuses.
## - Update status if task exists.
## - Show Display Tasks with updated status
## - Allow user to return to menu
def task_status():
    clear_console()
    print("\nUpdating task status...")
    if not tasks:
        print("No tasks available to update.")
        time.sleep(1)
        return

    display_task()
    
    while True:
        try:
            task_num = int(input("Enter the task number to update status (or 0 to cancel): ")) - 1
            
            if task_num == -1:      #If 0 is entered
                print(Fore.YELLOW + "Task status update cancelled" + Style.RESET_ALL)
                time.sleep(1)
                return

            if 0 <= task_num < len(tasks):      #Valid task selected
                while True:
                    print("\nSelect a new status:")
                    for i, status in enumerate(status_options, start=1):
                        print(f"{Fore.CYAN}{i}.{Style.RESET_ALL} {status}")
                
                    try:
                        status_choice = int(input("Enter status number (or 0 to cancel): ")) - 1
                        
                        if status_choice == -1:
                            print(Fore.YELLOW + "Task status update cancelled" + Style.RESET_ALL)
                            time.sleep(1)
                            return
                        if 0 <= status_choice < len(status_options):
                            tasks[task_num]["status"] = status_options[status_choice]
                            loading_animation()
                            print("Task status updated successfully!")
                            time.sleep(1)
                            return
                        else:
                            print("Invalid status number!")
                    except ValueError:
                        print(Fore.RED + "Invalid Input! Please enter a number." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid task number!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input! Enter a number." + Style.RESET_ALL)
        time.sleep(1)

# Create the main loop
## - Keep showing the menu until the user chooses to exit.
## - Call the appropriate function based on user input.
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))        # Convert input to an integer
        except ValueError:
            print("Invalid input! Please enter a number.")
            time.sleep(1)
            continue        # Restart the loop if input is invalid

        if choice == 1:
            add_task()       # Code to add task
            time.sleep(1)
            continue

        if choice == 2:
            delete_task()    # Code to delete task
            time.sleep(1)
            continue
        
        if choice == 3:
            edit_task()      # Code to Edit Task
            time.sleep(1)
            continue

        if choice == 4:
            task_status()    # Code to Update Task
            time.sleep(1)
            continue

        if choice == 0:
            print("Bye Bye!")
            break

        else:
            print("Invalid Choice. Please enter a valid option")
            time.sleep(1)

if __name__ == "__main__":
    main()
