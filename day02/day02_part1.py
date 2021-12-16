""" input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
    ]
 """
input = open("day02_input.txt").readlines()

directions = map(lambda line: {line.split()[0]: int(line.split()[1])}, input)

totals = {'forward': 0, 'up': 0, 'down': 0}

for line in directions:
    key = list(line.keys())[0]
    totals[key] += line[key]

horizontal = totals['forward']
depth = totals['down'] - totals['up']
print(horizontal * depth)