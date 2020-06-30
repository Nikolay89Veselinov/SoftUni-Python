items = {'food': {'pizza': {'quality': 10, 'quantity': 5}, 'burger': {'quality': 110, 'quantity': 5}}}

([print(items[x][y]['quality']) for x in items for y in items[x]])

categories = input().split(', ')

bunker = {category: {} for category in categories}

n = int(input())

for i in range(n):
    tokens = input().split(' - ')
    category = tokens[0]
    item = tokens[1]
    items_info = tokens[2].split(';')
    quantity = int(items_info[0].split(':')[1])
    quality = int(items_info[1].split(':')[1])

    print(quantity)
    print(quality)

# food, water, materials, metal
# 5
# food - pizza - quantity:10;quality:5
# water - mineral - quantity:5;quality:10
# materials - wood - quantity:2;quality:5
# metal - copper - quantity:3;quality:10
# food - burgers - quantity:5;quality:2
