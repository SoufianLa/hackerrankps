import sys
import math
import os
import random
import re
import operator
import heapq

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# n element
# k operation: divide by 2 and insert
#  so u can find the min sum

def minSum(num, k):
    num_heap = [-n for n in num]
    heapq.heapify(num_heap)
    for i in range(k):
        max = heapq.heappop(num_heap)
        heapq.heappush(num_heap, math.floor(max / 2))
    return -sum(num_heap)



if __name__ == '__main__':
    num_count = int(input().strip())
    num = []
    for _ in range(num_count):
        num_item = int(input().strip())
        num.append(num_item)

    k = int(input().strip())
    result = minSum(num, k)
    print(result)
