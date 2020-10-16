#!/bin/python3

import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    res = [0, 0]
    for al, bb in zip(a, b):
        if int(al) > int(bb):
            res[0] += 1
        elif int(al) < int(bb):
            res[1] += 1
    return res


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))
