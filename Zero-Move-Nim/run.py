import os
import sys
from functools import reduce

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def zeroMoveNim(p):
    p = [i - 1 + 2 * (i % 2) for i in p]
    return 'W' if reduce((lambda x, y: x ^ y), p) else 'L'


if __name__ == '__main__':
    g = int(input())
    for g_itr in range(g):
        n = int(input())
        p = list(map(int, input().rstrip().split()))
        result = zeroMoveNim(p)
        print(result)
