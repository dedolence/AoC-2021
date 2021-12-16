"""
horizontal, depth, aim

forward X = increases horizontal by X, increases depth by X*aim
down X = increases aim by X
up X = decreases aim by X

horizontal = sum(forward)
depth = sum(forward * aim)
aim = sum(down - up)
"""
""" 
input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
    ] """

input = open("day02_input.txt").readlines()

horizontal = depth = aim = 0

directions = map(lambda line: {line.split()[0]: int(line.split()[1])}, input)

totals = {'forward': 0, 'up': 0, 'down': 0}

for line in directions:
    key = list(line.keys())[0]
    if key == 'forward':
        horizontal += line['forward']
        depth += line['forward'] * aim
    elif key == 'down':
        aim += line['down']
    elif key == 'up':
        aim -= line['up']

print(horizontal * depth)