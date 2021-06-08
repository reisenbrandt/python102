# # write a program that simulates a visit to Santa

# # ask what user wants for Christmas
# user_wants = input('What would you like for Christmas this year? ')

# # ask if they have been good or bad
# user_year_behave = input('Have you been good or bad this year? ')

# # create new list to add their wants into
# user_gets = []

# # create a function that determines what they get
# def christmasGifts():
#     # if they answer good
#     if user_year_behave == 'good':
#         # add wants to the empty list and return the new sentence
#         user_gets.append(user_wants)
#         print('Congrats! This is what you are getting: ')
#         for gets in user_gets:
#             print(gets, end = '')
#     # if they answer bad
#     elif user_year_behave == 'bad':
#         # return new sentence
#         print('A big lump of coal for you this year, bucko.')
#     else:
#         # or if they can't answer at all
#         print("You can't even answer a simple question, so coal it is.")
#     # return the new sentence
#     return user_gets



user_gets = []

print('Welcome to the North Pole!')
while True:
    print("""
    Choose an option:
    
    1. Tell Santa what you want.
    2. Tell Santa about your year.
    3. Ask what you will be getting.
    0. Leave.
    """)
    user_choice = input('')

    if user_choice == '1':
        user_wants = input('Well, what do you want then? ')
        user_gets.append(user_wants)
        addition = input('Do you want to ask for more? Y/N ').lower()
        while addition == 'y':
            user_wants2 = input('What more do you want? ')
            user_gets.append(user_wants2)
            addition = input('Do you want to ask for more? Y/N ')
        else:
            print("Thanks for your request. Pick another option.")

    elif user_choice == '2':
        user_year = input('Were you good or bad this year though? ').lower()
        print("We will take that into consideration.")

    elif user_choice == '3':
        user_yes_or_no = input('So you want to know what you will get this year? ').lower()
        if user_yes_or_no == 'y' or user_yes_or_no == 'yes' and user_year == 'good':
            print("Since you have been good this year, you will receive: ")
            for wants in user_gets:
                print(wants, end = ', ')
        elif user_yes_or_no == 'y' or user_yes_or_no == 'yes' and user_year == 'bad':
            print("Yikes, looks like you are getting coal. Better luck next year.")
        elif user_yes_or_no == 'n' or user_yes_or_no == 'no':
            print("No worries! Back to the menu you go.")

    elif user_choice == '0':
        print("Be good.")
        break

