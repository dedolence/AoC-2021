"""
    the problem:
        verify life support rating = oxygen generation rating * CO2 scrubbing rating

    the method:
        from list of input numbers, go through each column selecting only numbers that meet
        a criteria for that column.

        oxygen rating = keep numbers with the most common digit in that position
        co2 rating = keep numbers with the least common digit in that position
        if a tie, keep numbers with 1 in that position. 
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

def findMostCommonBit(bitArray):
    length = len(bitArray)
    total = sum(int(digit) for digit in bitArray)
    return '1' if total > length/2 else '0'

def transformInput(a):
    line_length = len(a[0])
    for i in range(line_length):
        bit_place = 0