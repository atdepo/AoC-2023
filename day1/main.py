import os
import re

# Part 1

"""
The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
to form a single two-digit number
"""

filename = os.path.join(os.path.dirname(os.getcwd()), 'day1/puzzle_input.txt')
# Read input file
with open(filename, 'r') as f:
    input = f.read().split('\n')
    sum = 0
    for elem in input:
        test = re.findall(r'\d', elem)
        sum += int(test[0]+test[-1])
    print(sum)

# Part 2

"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
Equipped with this new information, you now need to find the real first and last digit on each line.
"""

digits = [
    ('one', 'o1ne'),
    ('two', 't2wo'),
    ('three', 't3hree'),
    ('four', 'f4our'),
    ('five', 'f5ive'),
    ('six', 's6ix'),
    ('seven', 's7even'),
    ('eight', 'e8ight'),
    ('nine', 'n9ine'),

]
with open(filename, 'r') as f:
    input = f.read().split('\n')
    sum = 0

    for element in input:

        for old, new in digits:
            element = element.replace(old, new)
        test = re.findall(r'\d', element)
        number = int(test[0]+test[-1])
        sum += number
    print(sum)
