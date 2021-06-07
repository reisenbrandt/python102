numbers = [1, 50, 3, 9999, 10000, 2, 42]

lowest = number[0]
for num in numbers:
    if num < lowest:
        lowest = num

print(lowest)