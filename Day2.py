user_prompt = "Enter a todo"
# here we are using while loop which will get executed infinite
# times because 2 is always greater than 1
# while 2 > 1:
## todo = input(user_prompt)
## print(todo)
## print("next..")

# python have better ways of using infinite loop is by setting
# it to True, and it will execute infinite times
# True is boolean datatypes

# while True:
#     todo = input(user_prompt)
#     print(todo)
#     print("next..")

## =========== Methods =================
# method are linked with object like string list etc
todos = []
while True:
    todo = input(user_prompt)
    ## todos = [todo] if place this line here it will overwrite the list
    todos.append(todo) # here append is a method not a function
    print(todos)
