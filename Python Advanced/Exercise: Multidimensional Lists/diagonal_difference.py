# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

size = int(input())
matrix = []
primary_diagonal = 0
second_diagonal = 0

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

for i in range(len(matrix)):
    primary_diagonal += matrix[i][i]
    second_diagonal += matrix[i][-i -1]

print(f'Primary diagonal: {primary_diagonal}\nSecondary diagonal: {second_diagonal}\nDifference:{primary_diagonal - second_diagonal}')

# input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12