#Lesson 14 - this creates a module with custom functions....

FILEPATH = "todos.txt"

#Building Custom Functions (Lesson 11 & 12):
#Lesson 13 makes the filename a default parameter and not required to be passed to the custom functions
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the To Do items to a list in a TXT file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
