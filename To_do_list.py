import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to a file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display the task list."""
    if not tasks:
        print("\nNo tasks found! Add some tasks first.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task."""
    task = input("\nEnter a new task: ").strip()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def mark_task_done(tasks):
    """Mark a task as done."""
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num] += " ✔ (Done)"
                save_tasks(tasks)
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                deleted_task = tasks.pop(task_num)
                save_tasks(tasks)
                print(f"Deleted task: {deleted_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting... Your tasks are saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
