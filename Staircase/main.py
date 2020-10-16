import math
import os
import random
import re
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# Complete the staircase function below.
def staircase(n):
    for j in range(n):
        myList = list()
        for i in range(n):
            myList.append(" ")
        for k in range(n-j-1, n):
            myList[k] = "#"

        print("".join(myList))






if __name__ == '__main__':
    n = int(input())

    staircase(n)
