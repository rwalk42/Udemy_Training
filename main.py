# This is my first program in the Udemy Python training package

#Lesson 14 creates a separate file in the folder "Functions" in the same directory. Two methods..
#from Functions import get_todos, write_todos
import Functions
import time

now = time.strftime("%b %d, %Y - %H:%M:%S")
print("The time is below:")
print("It is..", now)

user_prompt = "Type add (task), show (all tasks), edit (task number), complete (task number) or exit:   "
# todos = ['emma', 'rab', 'kyle', 'ross', 'sophie']



#Main Program:
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = Functions.get_todos()

        todos.append(todo + '\n')
        Functions.write_todos(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # list comprehension method - creates list on the fly
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            place = int(index) + 1
            row = f"{place}-{item}"
            print(row)
        print("This list is ", len(todos), " items long")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = Functions.get_todos()
            existing_todo = todos[number]
            print(existing_todo)

            new_todo = input("type a new entry  ")
            todos[number] = new_todo + '\n'

            Functions.write_todos(todos)

            #print(todos)
        except ValueError:
            print("Your command is not valid..")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = Functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            Functions.write_todos(todos)

            message = f"The To Do, {todo_to_remove}, was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number..")
            continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Hey you entered an unknown command ")

print("Goodbye")
