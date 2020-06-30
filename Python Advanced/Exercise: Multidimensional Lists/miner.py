# We get as input the size of the field in which our miner moves. The field is always a square. After that we will
# receive the commands which represent the directions in which the miner should move. The miner starts from
# position - &#39;s&#39;. The commands will be: left, right, up and down. If the miner has reached a side edge of the field and
# the next command indicates that he has to get out of the field, he must remain on his current possition and ignore
# the current command. The possible characters that may appear on the screen are:

size = int(input())
commands = input().split()
miner_position = []
matrix = []
coals = 0
total_coals = 0
end = False

for i in range(size):
    row = input().split()
    matrix.append(row)
    if 's' in row:
        miner_position = [i, row.index("s")]
    total_coals += row.count('c')

for command in commands:
    next_miner_position = []
    if command == 'up':
        next_miner_position = [miner_position[0] -1, miner_position[1]]
    elif command == 'right':
        next_miner_position = [miner_position[0], miner_position[1] + 1]
    elif command == 'down':
        next_miner_position = [miner_position[0] +1, miner_position[1]]
    elif command == 'left':
        next_miner_position = [miner_position[0], miner_position[1] -1]

    if next_miner_position[0] >= 0 and next_miner_position[0] < len(matrix) and next_miner_position[1] >= 0 and next_miner_position[1] < len(matrix):
        row = next_miner_position[0]
        col = next_miner_position[1]

        if matrix[row][col] == '*':
            matrix[miner_position[0]][miner_position[1]] = '*'
            matrix[row][col] = 's'
            miner_position = next_miner_position
        elif matrix[row][col] == 'c':
            coals += 1
            if coals == total_coals:
                print(f'You collected all coals! ({row}, {col})')
                end = True
            matrix[miner_position[0]][miner_position[1]] = '*'
            matrix[row][col] = 's'
            miner_position = next_miner_position
        elif matrix[row][col] == 'e':
            print(f'Game over! ({row}, {col})')
            end = True
            break

if not end:
    print(f'{total_coals - coals} coals left. ({miner_position[0]}, {miner_position[1]})')

# input

# 5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *

# 6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *

