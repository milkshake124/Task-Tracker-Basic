import json
import datetime
import os

def load_tasks(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "tasks.json")
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_tasks(tasks, path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "tasks.json")
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()    
    new_id = max([task["id"] for task in tasks], default=0) + 1
    stat = "not yet chosen"

    now = datetime.datetime.now().isoformat()
    chooseStat = int(input("Enter the number which corresponds to the status of your task:\n1. In progress\n2. done\n3. To Do\n"))
    if chooseStat == 1:
        stat = "in progress"
        print("Status of task: In progress")
    elif chooseStat == 2:
        stat = "Done"
        print("Status of task: Done")
    elif chooseStat == 3:
        stat = "todo"
        print("Status of task: To Do")
    else:
        print("Invalid number entered")

    new_task = {
        "id": new_id,
        "description": description,
        "status": stat,
        "createdAt": now, 
        "updatedAt": now
    }

    tasks.append(new_task) 
    save_tasks(tasks)
    print(f"Task added: {new_task}")

def update_tasks_description():
    inputID = int(input("What is the ID of the task you would like to update?\n"))
    tasks = load_tasks()
    now = datetime.datetime.now().isoformat()
    for task in tasks:
        if inputID == task["id"]:
            task["description"] = input("What is the new description of the task?\n")
            task["updatedAt"] = now
            save_tasks(tasks)
            print("Task updated succesfully")
    else:
        print("task ID not found")

def update_tasks_status():
    inputID = int(input("What is the ID of the task you would like to update?\n"))
    tasks = load_tasks()
    now = datetime.datetime.now().isoformat()

    for task in tasks:
        if inputID == task["id"]:
            chooseStat = int(input("Enter the number which corresponds to the status of your task:\n1. In progress\n2. Done\n3. To Do\n"))
            
            if chooseStat == 1:
                task["status"] = "in progress"
                print("Status of task: In progress")
            elif chooseStat == 2:
                task["status"] = "Done"
                print("Status of task: Done")
            elif chooseStat == 3:
                task["status"] = "todo"
                print("Status of task: To Do")
            else:
                print("Invalid number entered")
                return  # exit early if invalid input
            
            task["updatedAt"] = now
            save_tasks(tasks)
            print("Task updated successfully")
            break
    else:
        print("Task ID not found")
            

def delete_task():
    inputID = int(input("What is the ID of the task you would like to delete?\n"))
    tasks = load_tasks()
    for task in tasks:
        if inputID == task["id"]:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted succesfully")
            break
    else:
        print("task ID not found")

def list_comp_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "Done":
            print(f"[{task['id']}] {task['description']} (Status: {task['status']})")

def list_IP_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "in progress":
            print(f"[{task['id']}] {task['description']} (Status: {task['status']})")

def list_ND_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["status"] == "todo" or task["status"] == "in progress":
            print(f"[{task['id']}] {task['description']} (Status: {task['status']})")

def list_all_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("Here are all your tasks:\n")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print("-" * 30)  # adds a line separator for readability


while True:
    userChoice = int(input("Enter the number which corresponds to what you would like to do today\n 1. Add a task\n2. Update a task\n3. Delete a task\n4.List all tasks\n5. List all tasks that are done\n6. List all tasks that are not done\n7. List all tasks that are in progress\n0. To quit the program\n"))
    if userChoice == 1:
        add_task(input("What is the description of your new task?\n"))
    elif userChoice == 2:
        upd = int(input("Would you like to update the task's status or description or both\nenter 1 for status, 2 for description, 3 for both"))
        if upd == 1:
            update_tasks_status()
        elif upd == 2:
            update_tasks_description()
        elif upd == 3:
            update_tasks_description()
            update_tasks_status()
        else:
            print("Invalid number entered")
    elif userChoice == 3:
        delete_task()
    elif userChoice == 4:
         list_all_tasks()
    elif userChoice == 5:
        list_comp_tasks()
    elif userChoice == 6:
        list_ND_tasks()
    elif userChoice == 7:
        list_IP_tasks()
    elif userChoice == 0:
        break


    