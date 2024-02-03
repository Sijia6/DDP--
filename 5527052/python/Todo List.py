todo_list = []

while True:
    print("Todo List:")
    for i, task in enumerate(todo_list):
        print(f"{i + 1}. {task}")
    
    choice = input("Choose an action (add/delete/quit): ")
    
    if choice == "add":
        task = input("Enter a task: ")
        todo_list.append(task)
    elif choice == "delete":
        index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= index < len(todo_list):
            del todo_list[index]
        else:
            print("Invalid task number")
    elif choice == "quit":
        break
    else:
        print("Invalid choice")
