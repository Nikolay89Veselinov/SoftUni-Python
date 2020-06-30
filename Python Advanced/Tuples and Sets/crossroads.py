
# Our favorite super-spy action hero Sam is back from his mission in the previous exam, and he has finally found some
# time to go on a holiday. He is taking his wife somewhere nice and they&#39;re going to have a really good time, but first,
# they have to get there. Even on his holiday trip, Sam is still going to run into some problems and the first one is, of

# © SoftUni – https://softuni.org. Copyrighted document. Unauthorized copy, reproduction or use is not permitted.
# Follow us: Page 10 of 10
# course, getting to the airport. Right now, he is stuck in a traffic jam at a very active crossroads where a lot of
# accidents happen.
# Your job is to keep track of traffic at the crossroads and report whether a crash happened or everyone passed the
# crossroads safely and our hero is one step closer to a much desired vacation.
# The road Sam is on has a single lane where cars queue up until the light goes green. When it does, they start passing
# one by one during the green light and the free window before the intersecting road&#39;s light goes green. During one
# second only one part of a car (a single character) passes the crossroads. If a car is still in the crossroads when the
# free window ends, it will get hit at the first character that is still in the crossroads.

from collections import deque

green_light = int(input())
window = int(input())

cars = deque()
cars_counter = 0
crashed = False

command = input()

while command != "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")

input

# 10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END

# 9
# 3
# Mercedes
# Hummer
# green
# Hummer
# Mercedes
# green
# END