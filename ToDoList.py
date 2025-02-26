### To Do List ###

#Import necessary libraries (optional, if using color or formatting)

#Define Task Status
## - Each task should have a name and a status
## - Default status should be "Not Started"
## - Include a method to update the status
class Task:
    def __init__(self, name, status="Not Started"):
        """Initialize task with a name and default status."""
        self.name = name
        self.status = status
    
    def update_status(self, new_status):
        """Update the task status."""
        self.status = new_status

#Define the To Do List class
## - Store Task in a List
## - Includes Methods for
##   - Adding Task
##   - Deleting Task
##   - Editing Task (Optional)
##   - Updating Task Status
##   - Displaying All Task (Always show with menu)
##   - Filtering Tasks by Status or Due Date (Optional)
class ToDoList:
    def __init__(self):
        """Initialize an empty task list."""
        self.tasks = []

    def display_tasks(self):
        """Display all tasks in a neat format."""
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.name} - Status: {task.status}")

if __name__ == "__main__":
    todo_list = ToDoList()

    # Manually adding test tasks
    task1 = Task("Study Python")
    task2 = Task("Buy Groceries", "In Progress")

    # Adding tasks to the list
    todo_list.tasks.append(task1)
    todo_list.tasks.append(task2)

    # Display tasks
    todo_list.display_tasks()


# Combined Display Function (Task List + Menu)
## - Show all task in a neat format with status and due date.
## - Include task status:
##   🔹 Not Started – Default status when a task is added.
##   🔹 In Progress – Task is currently being worked on.
##   🔹 On Hold – Task is temporarily paused.
##   🔹 Completed – Task is fully done.
##   🔹 Cancelled – Task is no longer needed.
##   🔹 Waiting for Review – Task is done but needs checking.
##   🔹 Needs Revision – Task requires changes before completion.
## - Show menu options directly below the task list.
##   - Add Task
##   - Delete Task
##   - Edit Task (Optional)
##   - Update Task Status
##   - Exit

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

