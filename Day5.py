## adding EDIT functionality
# Day 5 we want to add serialize numbering of list
# using enumerate and f strings

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
            for index, item in enumerate(todos, 1):
                # print(index,'-' ,item)
                row = f"{index}-{item}"
                print(row)
        case "edit":
            number = int(input("number of todo to edit"))
            number -= 1
            new_todo = input("enter new todo: ")
            todos[number] = new_todo

        # Adding completed an item or delete
        case "complete":
            # you can use remove or pop
            x = input()
            print(todos.remove(x))
            print(todos)
        case "exit":
            ## break statement will end the loop
            break
        case _:  # _ underscore represent a variable by convention
            print("unknown command")
print("Bye")