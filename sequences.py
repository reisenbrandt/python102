#  strings
'example string'
empty_string = ''

# integers
7

# floats
7.7

# booleans
True
False

# list => indicated by square brackets
languages = ['python', 'javascript', 'html', 'css']
empty_list = []
# lists use a zero based index => ALWAYS starts at 0
# lists have two indexes => a positive index and a negative index

# accessing items at certain index
print(languages[2])
# console prints html ^

# accessing an index that doesnt exist like languages[6]
# makes console throw IndexError

# accesses list from end and go towards to the beginning
print(languages[-1])
# console prints css ^


print(languages[1:3])
# will print another array with those indexes
# always goes left to right

print(languages[1:3:1])

print(languages[::-1])
# prints the list backwards

print(languages.index('css'))
# prints the index of the item in the list

string = 'example'
print(string[3])
# prints the letter m because example is a sequence in the variable 
# in the form of a string

# 
# 
# 
# 

index = 0
while index < len(languages):
    print (f'No, {languages[index]} is the best language')
    index += 1


for lang in languages:
    print('No, ' + lang + ' is the best language.')