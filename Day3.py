user_prompt = "type add or show or exit"
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
## match is function
    match user_action:
        ## this is switch case
        case "add":
            todo = input("Enter a todo")
            todos.append(todo)
        case "show":
            ## this is for loop
            for item in todos:
                print(todo)
        case "exit":
            ## break statement will end the loop
            break
        case _:   # _ underscore represent a variable by convention
            print("unknown command")
print("Bye")

## add strip() method to make code more efficient i.e. if you
## type "a" or "a " it will stripe the white space