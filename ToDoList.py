### To Do List ###

#Import necessary libraries (optional, if using color or formatting)

# Combined Display Function (Task List + Menu) Main Menu
## - Display all task in a neat format with status and due date.
## - Include task status:
##   🔹 Not Started – Default status when a task is added.
##   🔹 In Progress – Task is currently being worked on.
##   🔹 On Hold – Task is temporarily paused.
##   🔹 Completed – Task is fully done.
##   🔹 Cancelled – Task is no longer needed.
##   🔹 Waiting for Review – Task is done but needs checking.
##   🔹 Needs Revision – Task requires changes before completion.
## - Show menu options directly below the task list.
##   - 1. Add Task
##   - 2. Delete Task
##   - 3. Edit Task (Optional)
##   - 4. Update Task Status
##   - 0. Exit

import time
import os

tasks = []       # List to store tasks

status_options = [
    "Not Started", "In Progress", "On Hold", "Completed", 
    "Waiting for Review", "Needs Revision"
]

def clear_console():        #Clear the console screen for better readability
    os.system("cls" if os.name == "nt" else "clear")

def display_task():     #Display all tasks with status and due date
    if not tasks:
        print("\n No tasks available")
    else:
        print("\n========== Task List ==========")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} | Status: {task['status']} | Due: {task['due_date']}")
        print("======================================")

def display_menu():     #Display task list and status along with menu options
    clear_console()
    display_task()
    print("\n========== To-Do List Menu ==========")
    print("1. Add task")
    print("2. Delete Task")
    print("3. Edit Task")
    print("4. Update Task Status")
    print("0. Exit")
    print("======================================")

#Define the To Do List class
## - Store Task in a List
## - Includes Methods for
##   - Adding Task
##   - Deleting Task
##   - Editing Task (Optional)
##   - Updating Task Status
##   - Displaying All Task (Always show with menu)
##   - Filtering Tasks by Status or Due Date (Optional)

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
        name = input("Enter task name: ").strip()       #Get Task from User
        due_date = input("Enter due date (or press Enter to skip)") or "No due date"
        
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
    print("\nDeleting a task...")
    if not tasks:
        print("No task available to delete")
        time.sleep(1)
        return
    try:
        task_num = int(input("Enter a task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            confirm = input(f"Are you sure you want to delete '{tasks[task_num]['name']}'? (y/n): ").lower()
            if confirm == 'y':
                deleted_task = tasks.pop(task_num)
                print(f"Task '{deleted_task['name']}' deleted successfully!")
            else:
                print("Task deletion cancelled.")
        else:
            print("Invalid task number")
    except ValueError:
        print("Invalid input! Enter a number")

time.sleep(1)

# Editing Task Name (Optional)
## - Ask user which task they want to rename.
## - Allow user to enter a new name.
## - Update the task name in the list.
def edit_task():
    print("\nEditing a task...")
    if not tasks:
        print("No task available to edit")
        time.sleep(1)
        return
    
    display_task()

    try:
        task_num = int(input("Enter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            new_name = input("Enter new task name: ").strip()
            tasks[task_num]["name"] = new_name
            print("Task name updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Enter a number.")      

time.sleep(1)

#Updating Task Status
## - Ask user which task to update.
## - Show list of possible statuses.
## - Update status if task exists.
## - Show Display Tasks with updated status
## - Allow user to return to menu
def task_status():
    print("\nUptating task status...")
    if not tasks:
        print("No tasks available to update.")
        time.sleep(1)
        return

    display_task()
    
    try:
        task_num = int(input("Enter the task number to update status: ")) - 1
        if 0 <= task_num < len(tasks):
            print("Select a new status:")
            for i, status in enumerate(status_options, start=1):
                print(f"{i}. {status}")
            
            status_choice = int(input("Enter status number: ")) - 1
            if 0 <= status_choice < len(status_options):
                tasks[task_num]["status"] = status_options[status_choice]
                print("Task status updated successfully!")
            else:
                print("Invalid status number!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Invalid input! Enter a number.")

time.sleep(1)

#Create the main loop
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
            continue

        else:
            print("Invalid Choice. Please enter a valid option")
            time.sleep(1)

if __name__ == "__main__":
    main()


