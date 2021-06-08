import json

with open('todos.json', 'r') as file_handle:
    data = json.load(file_handle)


def print_todos():
    print('~~~ To Do ~~~')
    count = 1
    for todo in data:
        print(f"{count}: {todo}")
        count += 1
    print('~~~~~~~~~~~~~')

while True:
    print("""
Choose an option:

1. Print Todos
2. Add Todo
3. Remove Todo
0. Quit
    """)
    user_choice = input('')

    # input is ALWAYS a string
    if user_choice == '1':
        # print current todos
        print_todos()

    elif user_choice == '2':
        # add new item
        new_item = input('What do you want to add to the list? ')
        data.append(new_item)

    elif user_choice == '3':
        # removes an item
        print_todos()

        delete_index = int(input('Which item would you like to remove? '))
        # del => keyword for delete by index
        del data[delete_index - 1]

    elif user_choice == '0':
        # exit the program loop
        print('Goodbye')
        break 

with open('todos.json', 'w') as file_handle:
    json.dump(data, file_handle)


