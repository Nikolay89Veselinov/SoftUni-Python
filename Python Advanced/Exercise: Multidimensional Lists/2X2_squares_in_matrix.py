# Find the count of 2 x 2 squares of equal chars in a matrix.

(rows_count, column_counts) = [int(x) for x in input().split()]
matrix = []
sub_matrix = []
counter = 0
for _ in range(rows_count):
    matrix.append(input().split())

for row in range(rows_count -1):
    for col in range(column_counts -1):
        index = [
        matrix[row][col], 
        matrix[row][col + 1],
        matrix[row + 1][col],
        matrix[row + 1][col +1]   
        ]
        equal = all(number==index[0] for number in index)
        if equal:
           sub_matrix.append(index)
           counter += 1
print(counter)

# input

# 3 4
# A B B D
# E B B B
# I J B B