todos = ['pet the cat', 'go to work', 'shop for groceries', 'go home', 'feed the cat']

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
        count = 1
        for todo in todos:
            print(f"{count}: {todo}")
            count += 1

    elif user_choice == '2':
        # add new item
        new_item = input('What do you want to add to the list? ')
        todos.append(new_item)

    elif user_choice == '3':
        # removes an item
        index = 0
        for todo in todos:
            print(f"{index}: {todo}")
            index += 1

        delete_index = int(input('Which item would you like to remove? '))
        # del => keyword for delete by index
        del todos[delete_index]

    elif user_choice == '0':
        # exit the program loop
        print('Goodbye')
        break 