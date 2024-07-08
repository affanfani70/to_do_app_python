task_list = []


def add_task(task):
    task_name = input("Enter the task name: ")
    task = {"name": task_name, "completed": False}
    task_list.append(task)
    print(f"Task '{task_name}' added.")


def view_tasks():
    if not task_list:
        print("--> No tasks to show.")
        return

    print("\nCurrent Tasks:")
    for sr, task in enumerate(task_list, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{sr}. {task['name']} - {status}")


def mark_task_completed():
    view_tasks()
    if not task_list:
        return

    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if task_num <= len(task_list) and task_num > 0:
            task_list[task_num - 1]["completed"] = True
            print(f"Task '{task_list[task_num - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()
    if not task_list:
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if task_num <= len(task_list) and task_num > 0:
            removed_task = task_list.pop(task_num - 1)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    while True:
        print("\nTo-Do App Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting the to-do app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
