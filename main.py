from task_manager import TaskManager

tm = TaskManager()

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tm.add_task(task)

    elif choice == "2":
        tm.show_tasks()

    elif choice == "3":
        tm.show_tasks()
        idx = int(input("Task number: ")) - 1
        tm.complete_task(idx)

    elif choice == "4":
        tm.show_tasks()
        idx = int(input("Task number: ")) - 1
        tm.delete_task(idx)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
