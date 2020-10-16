import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Complete the plusMinus function below.
def plusMinus(arr):
    zero = 0
    pos = 0
    neg = 0
    for e in arr:
        if e == 0:
            zero +=1
        elif e > 0:
            pos += 1
        else:
            neg +=1
    res_p = round((pos / n), 6)
    res_n = round((neg / n), 6)
    res_z = round((zero / n), 6)
    print(res_p)
    print(res_n)
    print(res_z)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

