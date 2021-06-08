# def => DEFine a function
# functions get evaluated
# def <name of function>(<arguments>)
# print vs return
# print returns none and then prints the string None
# return just returns the value back into the program
# anything after a return statement does not get run

def add(num1, num2):
    return num1 + num2
    
# # call or invoke a function below
# add()

# # print a function
# print(add())

# # print the end result of a function
# print(add(10, 5))

# ***put defs at top of code normally***

# can loop functions into each other by calling them as arguments
def add5(num):
    return add(num, 5)

user_num = int(input('What number would you like to add 5 to? '))
print(add5(user_num))