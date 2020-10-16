import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    final = list()
    n = len(arr)
    for i in range(n):
        my = [arr[k] for k in range(n) if k != i]
        final.append(sum(my))
        final.sort()
    print(str(final[0])+" "+str(final[n-1]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
