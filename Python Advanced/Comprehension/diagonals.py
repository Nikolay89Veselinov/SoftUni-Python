# Using nested list comprehension write a program that reads NxN matrix, finds its diagonals, prints them and their
# sum as shown below.

n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][- i -1] for i in range(n)]

print(f'First diagonal: {", ".join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}')

# input

# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9