data = open("day01_input.txt").readlines()
input = [int(line) for line in data]
# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

first_line = input[0]
i = 0
for line in input:
    i += 1 if line > first_line else 0
    first_line = line

print(i)