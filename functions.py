def get_todos(filename="todos.txt"):
    """ Function to open the file containing our list of to-do items """
    try:
        with open(filename, "r") as file:
            todos = file.readlines()
        return todos
    except FileNotFoundError:
        pass

def write_todos(todos_local, filename="todos.txt"):
    """ Write list of to-dos to a specified file """
    with open(filename, "w") as file:
        file.writelines(todos_local)

# the following lines will not execute when loading this module in you script
if __name__ == "__main__":
    print("hello world")

