numbers = [1, 50, 3, 9999, -1000000, -2, 42]

positive_numbers = []
for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print(positive_numbers)