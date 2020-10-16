# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def taskOfPairing(freq):
    j = 1

    total = 0
    r_list = list()
    for i in freq:
        total += int(i / 2)
        r = i % 2
        if r > 0:
            r_list.append(j)
        j += 1

    for i in range(0, len(r_list), 2):
        chunk = r_list[i:i + 2]
        if len(chunk) >= 2 and (chunk[1] - chunk[0] == 1):
            total += 1
    return total


if __name__ == '__main__':
    freq_count = int(input().strip())
    freq = []
    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq)
    print(result)
