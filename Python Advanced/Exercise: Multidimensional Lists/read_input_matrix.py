index = int(input())

matrix=[]
for row in range(index):
    row=[]
    for _ in range(index):
        row.append('*')
    matrix.append(row)
[print(x) for x in matrix]

def get_input(n):
    matrix = []
    for _ in range(n):
        line = input()
        matrix.append([x for x in line])
    return [print(x) for x in matrix]


n = int(input())

get_input(n)