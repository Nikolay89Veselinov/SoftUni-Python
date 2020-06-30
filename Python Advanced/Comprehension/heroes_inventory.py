# Using comprehension write a program that receives some hero names, items that need to be added in their
# inventory (item name and item cost) and then prints for each hero the total amount of items and the total cost of
# them.

names = input().split(', ')
command = input()
heroes = {hero: {} for hero in names}

while command != 'End':
    name, item, cost = command.split('-')
    if name in heroes:
        if item not in heroes[name]:
            heroes[name][item] = int(cost)
            
    command = input()

[print(f'{hero} -> Items: {len(heroes[hero])}, Cost: {sum(heroes[hero].values())}') for hero in heroes]

# input

# Peter, George
# Peter-Sword-20
# Peter-Shield-10
# George-Gem-100
# Peter-Sword-15
# George-Sword-20
# End