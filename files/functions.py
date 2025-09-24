
from pathlib import Path



def setup():
    # Placing a placeholder for the location of the todo.txt file:
    #todos_path = "todos.txt"
    check_todo()
    # Placing a placeholder for the location of the completed.txt file:
    # completed_path = "completed.txt"
    check_completed()
    return todos_path,completed_path


def get_time(timestamp):
    while True:
        import time
        now = time.strftime("%b %d, %Y - (%H:%M:%S)")
        timestamp[0] = now
        return timestamp

def check_todo():
    global todos_path
    todos_path = "todos.txt"
    while True:
        """This takes the file path of the todo file and find out if the file exists"""
        try:
            get_todos(todos_path)
            break
        except FileNotFoundError:
            todos_path = "files/todos.txt"
            try:
                get_todos(todos_path)
                break
            except:
                app_directory = Path(__file__).parent / "files"
                app_directory.mkdir(exist_ok=True)
                with open("files/todos.txt","w") as file:
                    file.write("")
                setup()
                break


def check_completed():
    global completed_path
    """This takes the file path of the completed file and find out if the file exists"""
    completed_path = "files/completed.txt"
    while True:
        try:
            get_completed(completed_path)
            break
        except FileNotFoundError:
            completed_path = "completed.txt"
            try:
                get_completed(completed_path)
                break
            except:
                app_directory = Path(__file__).parent / "files"
                app_directory.mkdir(exist_ok=True)
                with open("files/completed.txt","w") as file:
                    file.write("")
                setup()
                break


def get_todos(todos_path):
    """This takes the filepath of the todo list and returns the todos in the list"""
    with open(todos_path, "r") as file:
        todos = file.readlines()
    return todos

def show_todos(todos_path):
    todos = get_todos(todos_path)
    app_todos = todos[1::2]
    if todos == []:
        return ["No item in todos:"]
    else:
            return [f"{i+1}. {todo.strip()}" for i, todo in enumerate(app_todos)]

def show_completed(completed_path):
    completed = get_completed(completed_path)
    app_completed = completed[1::2]
    if completed == []:
        return ["No to-do item has been completed yet"]
    else:
            return [f"{i+1}. {todo.strip()}" for i, todo in enumerate(app_completed)]

def get_completed(completed_path):
    """This takes the filepath of the completed list and returns the todos in the list"""
    with open(completed_path, "r") as finished:
        completed = finished.readlines()
    return completed


def save_todos(todos_path, todos_arg):
    """This takes the filepath of the todo list and a todo argument and saves the todos argument in the list"""
    with open(todos_path, "w") as save:
        save.writelines(todos_arg)


def save_todos_after_delete(todos_path,todos):
    """This takes the filepath of the todo list and saves the  todo list after some of it has been deleted"""
    with open(todos_path, "w") as save:
        save.writelines(todos)


def save_completed(completed_path, complete_arg):
    """This takes the filepath of the completed list and saves the completed argument in the completed list after some of it has been deleted"""
    with open(completed_path, "w") as finish:
        finish.writelines(complete_arg)


def save_completed_after_delete(completed_path,completed):
    """This takes the filepath of the completed list and saves the  completed list after some of it has been deleted"""
    with open(completed_path, "w") as save:
        save.writelines(completed)



def add_todos(todos,app_todos,todo,time_stamp):
    if todo == '':
        message = "Please type a to-do first"
        return message,todo
    else:
        app_todos = [item.strip() for item in app_todos]
        todo = todo.capitalize()
        if todo in app_todos:
            message = "To-do already exists"
            return message,todo
        else:
            date_time = get_time(time_stamp)[0]
            add = f"{date_time}:\n {todo.capitalize()}\n"
            todos.insert(0, add)
            save_todos(todos_path, todos)
            message = f"To-do added successfully"
            area = ""
            return message,area

def edit_todos(todo,todos,app_todos,index,indexes,time_stamp):
    if todos == []:
        message = "To-dos empty"
        return message,todo
    else:
        if index is None:
            message = "Please choose a To-do item to edit"
            return message,todo
        else:
            if todo == "":
                message = "Please input the change for the selected to-do"
                return message,todo
            elif len(indexes)>1:
                message = "Please choose only one item at a time to edit"
                return message,todo
            else:
                number = int(index)
                change = f"{todo.strip().lower().capitalize()}"
                time_stamp = get_time(time_stamp)
                date_time = time_stamp[0]
                if todo.strip().capitalize() == todos[number].strip():
                    message = "No changes detected"
                    return message,todo
                elif change in [item.strip().lower().capitalize() for item in app_todos]:
                    message = "Similar to-do already exists"
                    return message,todo
                else:
                    todos[number] = f" {change.capitalize()}\n"
                    todos[number-1] = f"{date_time}:\n"
                    save_todos(todos_path, todos)
                    area = ""
                    message = f"To-do edited successfully"
                    return message,area



def delete_todos(todos,indexes):
    if todos == []:
        message = "To-dos empty"
        return message
    else:
        if indexes == []:
            message = "Please choose a To-do item to delete"
            return message
        else:
            for index in sorted(indexes, reverse=True):
                number = int(index)
                todos.pop(number)
                todos.pop(number-1)
                save_todos(todos_path, todos)
            message = f"To-do deleted successfully"
            return message


def delete_completed(completed_path,completed,completed_indexes):
    completed_deleted_count = 0
    if completed == []:
        message = "To-dos empty"
        return message
    else:
        if completed_indexes == []:
            message = "Please choose a to-do item to delete"
            return message
        else:
            for index in sorted(completed_indexes, reverse=True):
                number = int(index)
                completed.pop(number)
                completed.pop(number-1)
                save_completed(completed_path, completed)
                completed_deleted_count += 1
            if completed_deleted_count == 1:
                message = "Completed to-do deleted successfully"
            else:
                message = f"{completed_deleted_count} completed to-dos successfully deleted"
            return message



def complete_todos(todos,completed,indexes,time_stamp):
    completed_count = 0
    if todos == []:
        message = "To-dos empty"
        return message
    else:
        if indexes == []:
            message = "Please choose a To-do item to complete"
            return message
        else:
            now = get_time(time_stamp)
            date_time = now[0]
            for item in sorted(indexes,reverse=True):
                number = int(item)
                completed_item = todos[number]
                completed.insert(0, " " + completed_item.strip().capitalize() + "\n")
                completed.insert(0, f"{date_time}:\n")
                save_completed(completed_path, completed)
                todos.pop(number)
                todos.pop(number-1)
                save_todos(todos_path, todos)
                completed_count += 1
            if completed_count == 1:
                message = "Congratulations, to-do successfully completed"
            else:
                message = f"Congratulations, {completed_count} to-dos successfully completed"
            return message

def reverse_completed(todos,completed,completed_indexes,time_stamp):
    skipped_count = 0
    reversed_count = 0
    if completed == []:
        message = "No to-do item completed yet"
        return message
    else:
        if completed_indexes == []:
            message = "Please choose an item to reverse"
            return message
        else:
            now = get_time(time_stamp)
            date_time = now[0]
            for item in sorted(completed_indexes,reverse=True):
                number = int(item)
                completed_item = completed[number]
                if completed_item in todos:
                    skipped_count+=1
                    continue
                else:
                    todos.insert(0, " " + completed_item.strip().capitalize() + "\n")
                    todos.insert(0, f"{date_time}:\n")
                    completed.pop(number)
                    completed.pop(number-1)
                    save_completed(completed_path, completed)
                    save_todos(todos_path, todos)
                    reversed_count+=1
            if len(completed_indexes)>1:
                if reversed_count > 0 and skipped_count > 0:
                    message = f"{reversed_count} items reversed, {skipped_count} skipped (already in to-dos)."
                elif reversed_count > 0:
                    message = f"{reversed_count} items successfully reversed."
                elif skipped_count > 0:
                    message = f"Skipped {skipped_count} items, they already exist in to-dos."
            else:
                if reversed_count > 0:
                    message = "item reversed successfully"
                else:
                    message = "Similar item exists in to-dos, consider deleting item"
            return message


def clear_todos(todos_path):
    todos = get_todos(todos_path)
    """This clears the todos list"""
    if todos == []:
        message = "To-dos already empty"
        return message
    else:
        try:
            todos.clear()
            with open(todos_path, "w") as done:
                done.writelines(todos)
                save_todos(todos_path, todos)
                print(todos)
            if todos == []:
                message = "To-dos list cleared successfully"
                return message
            else:
                message = "Could not clear the to-dos list todos not empty"
                return message
        except:
            message = "Could not clear the to-dos list"
            return message


def clear_completed(completed_path):
    completed = get_completed(completed_path)
    """this clears the completed list"""
    if completed == []:
        message = "Completed todos already empty"
        return(message)
    else:
        try:
            completed.clear()
            with open(completed_path, "w") as clear_completed:
                clear_completed.writelines(completed)
                save_completed(completed_path, completed)
            if completed == []:
                message = "Completed list cleared successfully"
                return message
            else:
                message = "Could not clear the completed list"
                return message
        except:
            message = "Could not clear the completed list"
            return message