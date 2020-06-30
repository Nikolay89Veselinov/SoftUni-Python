# Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be
# given two ranges in the format: &quot;{first_start},{first_end}-{second_start},{second_end}&quot;. Find the
# intersection of these two ranges and save the longest one of all N intersections. At the end print the numbers that
# are included in the longest intersection and its length in the format: &quot;Longest intersection is
# {longest_intersection} with length {length_longest_intersection}&quot;

command = int(input())
best_intersection = []

for _ in range(command):
    ranges = input().split('-')
    first_range = [int(x) for x in ranges[0].split(',')]
    second_range = [int(x) for x in ranges[1].split(',')]
    first_set = set([x for x in range(first_range[0], first_range[1] + 1)])
    second_set = set([x for x in range(second_range[0], second_range[1] + 1)])
    intersection = first_set & second_set

    if len(intersection) > len(best_intersection):
        best_intersection = intersection
print(f'Longest intersection is {best_intersection} with length {len(best_intersection)}')

# input

# 5
# 0,10-2,5
# 3,8-1,7
# 1,8-2,4
# 4,7-2,5
# 1,10-2,11