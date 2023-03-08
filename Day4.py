## adding EDIT functionality

user_prompt = "type add or show or edit or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    ## match is function
    match user_action:
        ## this is switch case
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            ## this is for loop
            for item in todos:
                print(todos)
        case "edit":
            # input function by default store everything as str
            # so, we used int() to convert str to int
            number = int(input("number of todo to edit"))
            # indexing start from 0 so we minus 1 from user input
            # to match it with index
            number -= 1
            # we are asking for new input from user
            new_todo = input("enter new todo: ")
            # now todos[index] = will replace with new_todo
            todos[number] = new_todo

        case "exit":
            ## break statement will end the loop
            break
        case _:  # _ underscore represent a variable by convention
            print("unknown command")
print("Bye")
