#!/bin/python3

import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(str(result))
