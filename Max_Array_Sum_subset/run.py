#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    dp = {}  # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        print(i)
        print(num)
        print("-----")
        dp[i] = max(dp[i - 1], dp[i - 2] + num, dp[i - 2], num)

    return dp[len(arr) - 1]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    print(str(res) + '\n')
