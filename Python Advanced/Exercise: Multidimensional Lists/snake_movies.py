# You are walking in the park and you encounter a snake! You are terrified, and you start running zigzag, so the snake
# starts following you.
# You have a task to visualize the snake&#39;s path in a square form. A snake is represented by a string. The isle is a
# rectangular matrix of size NxM. A snake starts going down from the top-left corner and slithers its way down. The
# first cell is filled with the first symbol of the snake, the second cell is filled with the second symbol, etc. The snake is
# as long as it takes in order to fill the stairs completely - if you reach the end of the string representing the snake,
# start again at the beginning. After you fill the matrix with the snake&#39;s path, you should print it.

from collections import deque

(rows_count, columns_count) = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for _ in range(rows_count):
    matrix.append(['' for _ in range(columns_count)])

for row in range(rows_count):
    if row % 2 == 0:
        for col in range(columns_count):
            matrix[row][col] += text[0]
            text.append(text[0])
            text.popleft()
    else:
        for col in range(columns_count -1, -1, -1):
            matrix[row][col] += text[0]
            text.append(text[0])
            text.popleft()

for row in range(rows_count):
    print(''.join(matrix[row]))

# input

# 5 6
# SoftUni