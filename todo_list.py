import json
import os

FILE_NAME = "tasks.json"
tasks = []

# Nice separator
def separator():
    print("\n------------------------------------------------\n")

# Load tasks from file (Safe)
def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
        except:
            tasks = []
    else:
        tasks = []

# Save tasks
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Edit Task")
    print("5. Delete Specific Task (by number or name)")
    print("6. Delete All Tasks")
    print("7. Exit")

# Add Task (Single + Multiple)
def add_task():
    separator()
    user_input = input("Enter task (for multiple tasks use commas): ").strip()

    if not user_input:
        print("Task cannot be empty!")
        separator()
        return

    items = [t.strip() for t in user_input.split(",") if t.strip()]

    for task in items:
        tasks.append({"task": task, "status": "Pending"})

    save_tasks()

    if len(items) == 1:
        print("Task added successfully!")
    else:
        print(f"{len(items)} tasks added successfully!")
    separator()

# View Tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t['task']} - {t['status']}")

# ============================
# MARK COMPLETED (NUMBER + NAME)
# ============================
def mark_completed():
    separator()
    view_tasks()
    if not tasks:
        separator()
        return

    user_input = input(
        "Enter task NUMBER(s) or NAME(s) to mark completed (comma supported): "
    ).strip()
    
    items = [x.strip() for x in user_input.split(",") if x.strip()]
    completed_count = 0

    for item in items:
        if item.isdigit():
            idx = int(item)
            if 1 <= idx <= len(tasks):
                if tasks[idx - 1]["status"] != "Completed":
                    tasks[idx - 1]["status"] = "Completed"
                    completed_count += 1
            else:
                print("Invalid task number!")
                print("Please enter a valid task number!")
        else:
            found = False
            for t in tasks:
                if t["task"].lower() == item.lower():
                    if t["status"] != "Completed":
                        t["status"] = "Completed"
                        completed_count += 1
                    found = True
                    break
            if not found:
                print("Invalid task name!")
                print("Please enter a valid task name!")

    if completed_count > 0:
        save_tasks()

        if completed_count == 1:
            print("Selected task is marked as completed!")
        else:
            print("Selected tasks are marked as completed!")

        print("\nUpdated Task Status:")
        view_tasks()
    separator()

# ============================
# EDIT TASK (NUMBER + NAME)
# ============================
def edit_task():
    separator()
    view_tasks()
    if not tasks:
        separator()
        return

    choice = input("Enter task NUMBER or TASK NAME to edit: ").strip()

    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task name: ").strip()
            if new_task:
                tasks[num - 1]["task"] = new_task
                save_tasks()
                print("Task updated successfully!")
            else:
                print("Task cannot be empty!")
        else:
            print("Invalid task number!")
            print("Please enter a valid task number!")
    else:
        name = choice.lower()
        found = False
        for t in tasks:
            if t["task"].lower() == name:
                new_task = input("Enter new task name: ").strip()
                if new_task:
                    t["task"] = new_task
                    save_tasks()
                    print("Task updated successfully!")
                else:
                    print("Task cannot be empty!")
                found = True
                break
        if not found:
            print("Invalid task name!")
            print("Please enter a valid task name!")
    separator()

# ============================
# DELETE TASK (NUMBER + NAME)
# ============================
def delete_task():
    separator()
    view_tasks()
    if not tasks:
        separator()
        return

    choice = input("\nEnter task NUMBER or TASK NAME to delete: ").strip()

    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_tasks()
            print(f'Task "{deleted["task"]}" deleted successfully!')
        else:
            print("Invalid task number!")
            print("Please enter a valid task number!")
    else:
        name = choice.lower()
        found = False
        for t in tasks:
            if t["task"].lower() == name:
                tasks.remove(t)
                save_tasks()
                print(f'Task "{t["task"]}" deleted successfully!')
                found = True
                break
        if not found:
            print("Invalid task name!")
            print("Please enter a valid task name!")
    separator()

# Delete All
def delete_all_tasks():
    separator()
    confirm = input("Are you SURE you want to delete ALL tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks()
        print("All tasks deleted successfully!")
    else:
        print("Deletion cancelled. Tasks are safe.")
    separator()

# Main Program
print("\n=== Welcome to Your To-Do Manager ===")
load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        separator()
        view_tasks()
        separator()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        edit_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        delete_all_tasks()
    elif choice == "7":
        separator()
        print("Thank you! Exiting program...")
        separator()
        break
    else:
        separator()
        print("Invalid choice! Please select between 1-7.")
        separator()
