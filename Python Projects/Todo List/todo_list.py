def load_tasks():
    try:
        with open("todo_list.txt", 'r') as file:
            return [lines.strip() for lines in file.readlines()]
    except:
        return []

def save_tasks(tasks):
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
        print("\nTask Saved\n")

def show_all_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Task: {task}")

def add_task(tasks):
    task = input("Enter Your Tasks: ")
    tasks.append(task)
    save_tasks(tasks)

def check_mark_task(tasks):
    show_all_tasks(tasks)
    check = int(input("Which Task i Check Mark: "))

    if 1 <= check <= len(tasks):
        tasks[check-1] = f"{tasks[check-1]} (complete)"
        save_tasks(tasks)
    else:
        print("Invalid Input")

def remove_task(tasks):
    show_all_tasks(tasks)
    check = int(input("Which Task i Remove: "))

    if 1 <= check <= len(tasks):
        del tasks[check-1]
        save_tasks(tasks)
    else:
        print("Invalid Input")


def main():
    tasks = load_tasks()

    while True:
        print("\nTodo List App\n")
        print("1. Show all Tasks")
        print("2. Add the Task")
        print("3. Check Mark the Task")
        print("4. Remove the Task")
        print("5. Exit the App")
        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                show_all_tasks(tasks)
            case "2":
                add_task(tasks)
            case "3":
                check_mark_task(tasks)
            case "4":
                remove_task(tasks)
            case "5":
                print("\nSuccessfuly Exit the App")
                break
            case _:
                print("\nInvalid Input")

if __name__ == "__main__":
    main()