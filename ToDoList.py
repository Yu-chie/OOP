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

task = []       # List to store tasks

def display_menu():
    def display_task():
        if not task:
            print("\n No tasks available")
        else:
            print("\n==== Task List ====")
            for index, task in enumerate(task, start=1):
                print(f"{index}. {task}")
            print("===================")

    print("\n==== To-Do List Menu ====")
    print("1. Add task")
    print("2. Delete Task")
    print("3. Edit Task")
    print("4. Update Task Status")
    print("0. Exit")
    print("=========================")

def add_task():
     print("Adding a task...")
            print()
            n_task = int(input("How many task do you wish to add?: "))

            for i in range(n_task):
                task = input("Enter Task name: ")       #Get Task from User
                task.append(task)       #Add to list
                print(f"Task '{task}' added successfully")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice"))        # Convert input to an integer
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue        # Restart the loop if input is invalid

        if choice == 1:
            add_task()      # Code to add task
            pass

        if choice == 2:
            print("Deleting a task...")
            # Code to delete task
            pass
        
        if choice == 3:
            print("Editing a task...")
            # Code to Edit Task
            pass

        if choice == 4:
            pint("Uptating task status...")
            # Code to Update Task
            pass

        if choice == 0:
            print("Bye Bye!")
            break

        else:
            print("Invalid Choice. Please enter a valid option")

if __name__ == "__main__":
    main()


#Define Task Status Class
## - Each task should have a name and a status
## - Default status should be "Not Started"
## - Include a method to update the status



#Define the To Do List class
## - Store Task in a List
## - Includes Methods for
##   - Adding Task
##   - Deleting Task
##   - Editing Task (Optional)
##   - Updating Task Status
##   - Displaying All Task (Always show with menu)
##   - Filtering Tasks by Status or Due Date (Optional)

# Error Handling
## - Prevent invalid menu choices.
## - Prevent duplicate task names (Optional).
## - Show error message if task doesn’t exist.

# Aesthetic Formatting
## - Use separators (————) to make menus clearer.
## - Add small delays (time.sleep) before refreshing the menu.

#Adding Task
## - Ask user for Task name
## - Ask user for Task Due Date (Optional)
## - Ask user for Task Details (optional)
## - Add Task to the list with default status

#Deleting Task
## - Ask user for task name to remove
## - Ask user for confirmation
## - If task exists, remove it from the list.
## - If not found, show an error message.

# Editing Task Name (Optional)
## - Ask user which task they want to rename.
## - Allow user to enter a new name.
## - Update the task name in the list.

#Updating Task Status
## - Ask user which task to update.
## - Show list of possible statuses.
## - Update status if task exists.
## - Show Display Tasks with updated status
## - Allow user to return to menu

# Updating Due Date (Optional)
## - Ask which task to update
## - Let the user enter a new due date
## - Update and display changes

#Create the main loop
## - Keep showing the menu until the user chooses to exit.
## - Call the appropriate function based on user input.
## - Make sure there’s an option to return to the menu.

