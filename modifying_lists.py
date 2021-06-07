# list of positive and negative numbers
numbers = [78, -1, -1000, 9001, 201]

# create a new empty list so we can add things to it
positive_numbers = []
# loop over each number in the list
for num in numbers:
    # if number is positive
    if num > 0:
        # add to new list
        positive_numbers.append(num)

print(positive_numbers)

list_with_strings = ['things', 'stuff', 'others']
list_with_numbers = [1, 2, 3, 4, 5]
list_with_booleans = [True, False, True, False]
list_with_lots = ['string', 3, True, []]

