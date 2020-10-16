import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def birthdayCakeCandles(candles):
    max_e = max(candles)
    return candles.count(max_e)


# Write your code here

if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
