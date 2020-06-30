clothes = [int(x) for x in input().split()]
rack = int(input())
rack_count = 0
total = 0

while clothes:
    current = clothes[-1]
    if rack >= total + current:
        total += clothes.pop()
    else:
        rack_count += 1
        total = 0

print(rack_count)

# input

# 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20