# Write a program that counts in a given list of float values and prints the number of occurrences of each value.

text = input()
result = {}

for elements in text:
    if elements not  in result:
        result[elements] = 0
    result[elements] += 1

for key, val in sorted(result.items()):
    print(f'{key}: {val} time/s')

# input

# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3