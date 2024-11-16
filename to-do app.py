# Simple To-Do List App
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task['completed'] else "❌"
            print(f"{i}. {task['task']} [{status}]")


def add_task(tasks):
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty.")


def mark_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []  # List to store tasks
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nExiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")


# Run the app
if __name__ == "__main__":
    main()
