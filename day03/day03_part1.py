import math
"""
    find power consumption = gamma * epsilon
    gamma = most common bit in each column of input
    epsilon = least common bit in each column

    logic:
    this problem relies on finding the most common digit in a column of binary numbers.
    the fact that it's binary means that if, after adding up all the numbers in a column,
    it is greater than half the total number of numbers in that column, then that means 
    the most common number was 1.

    after that it's just a matter of converting between string, binary, and integer, which
    is pretty straightforward in python.
"""

""" 
    input = ["00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"]
 """
input = open("day03_input.txt").readlines()

# number of lines
lines = len(input)

# number of columns per line
columns = len(input[0][:-1])    
# if using the real input, add [:-1] to ignore last (newline) character

# if i shorten this to something like a = b = c = 0, that association persists... they aren't all set to 0, but they become
# linked to each other so changes to one variable later affect the other variables. python quirk, i guess.
column_totals = [0 for i in range(columns)]
gamma_final = [0 for i in range(columns)]
epsilon_final = [0 for i in range(columns)]

# produces a list of the sum of each column, e.g. [123, 456, 678, 901, ...]
for line in input:
    for i in range(columns):
        column_totals[i] += int(line[i])


# reduce the column totals down to the most/least common digits, depending on whether the total for that column is > or < half the number of lines
# e.g. ['1', '0', '0', '1', '1']
for i in range(columns):
    gamma_final[i] = '1' if column_totals[i] > lines/2 else '0'
    epsilon_final[i] = '0' if column_totals[i] > lines/2 else '1'

# join columns to string
gamma_string = ''.join(gamma_final)
epsilon_string = ''.join(epsilon_final)

# convert strings to decimal
gamma_int = int(gamma_string, 2)
epsilon_int = int(epsilon_string, 2)

# produce final answer by multiplying the integers
print(gamma_int * epsilon_int)