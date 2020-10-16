import os
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# 1 -> 13
# 2 -> 14
# 3 -> 15
# 4 -> 16
# 5 -> 17
# 6 -> 18
# 7 -> 19
# 8 -> 20

def timeConversion(s):

    if s[-2:] == "AM":
        if s[:2] == '12':
            a = str('00' + s[2:8])
        else:
            a = s[:-2]
    else:
        if s[:2] == '12':
            a = s[:-2]
        else:
            a = str(int(s[:2]) + 12) + s[2:8]
    return a




#
# Write your code here.
#

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)

    print(result)
