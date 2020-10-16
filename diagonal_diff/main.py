#!/bin/python3

import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lr = 0
    rl = 0
    for i in range(0, n):
        lr += arr[i][i]
        rl += arr[i][n - 1 - i]
    return abs(lr - rl)


# 00 11 22 ;
# 02 11 20 ;


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result))
