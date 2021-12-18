data = open("day01_input.txt").readlines()
input = [int(line) for line in data]
# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


a = []
for i in range(len(input)):
    if i < len(input) - 2:
        a.append((input[i], input[i+1], input[i+2]))
        
b = [sum(group) for group in a]

c = zip(b, b[1:])
print(sum([b > a for a, b in c]))