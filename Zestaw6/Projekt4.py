import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
string = ''
for i in range(m):
    for j in range(n):
        string += matrix[j][i]

beginning = re.findall("^[(!@#$%&\s]*[a-zA-Z0-9]", string)
find = re.findall("[a-zA-Z0-9]+", string)
ending = re.findall("[(!@#$%&\s]*$", string)

final = ''
for i in beginning:
    final += i[:-1]
final += ' '.join(find)
for i in ending:
    final += i
print(final)