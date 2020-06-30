numbers = [int(x) for x in input().split(', ')]

positive = [x for x in numbers if x >= 0]
negative = [x for x in numbers if x < 0]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 == 1]

print(
    f'Positive: {", ".join(map(str, positive))}\
    \nNegative: {", ".join(map(str, negative))}\
    \nEven: {", ".join(map(str, even))}\
    \nOdd: {", ".join(map(str, odd))}'
    )

# input

# -2134
# -2135

# 12435
# 12436