#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

sys.stdin = open('input_1.txt', 'r')
sys.stdout = open('output_1.txt', 'w')


#
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING givenString as parameter.
#

def shortestSubstring(givenString):
    j = 0
    index = 0
    l = list(givenString)
    s = set(l)
    for c in l:
        if len(s) == 0:
            break
        if c in s:
            s.remove(c)
        index += 1
    string_to_optimize = givenString[:index]
    if string_to_optimize.count(string_to_optimize[j]) > 1:
        s = string_to_optimize.replace(string_to_optimize[j], "", 1)
        return len(s)
    return len(string_to_optimize)


def max_distinct_char(str, n):
    NO_OF_CHARS = 256
    # Initialize all character's
    # count with 0
    count = [0] * NO_OF_CHARS

    # Increase the count in array
    # if a character is found
    for i in range(n):
        count[ord(str[i])] += 1

    max_distinct = 0
    for i in range(NO_OF_CHARS):
        if (count[i] != 0):
            max_distinct += 1

    return max_distinct


def fun(str):
    n = len(str)
    max_distinct = max_distinct_char(str, n)
    minl = n
    for i in range(n):
        for j in range(n):
            subs = str[i:j]
            subs_lenght = len(subs)
            sub_distinct_char = max_distinct_char(subs,
                                                  subs_lenght)

            # We have to check here both conditions together
            # 1. substring's distinct characters is equal
            # to maximum distinct characters
            # 2. substing's length should be minimum
            if (subs_lenght < minl and
                    max_distinct == sub_distinct_char):
                minl = subs_lenght

    return minl


# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
# for testing in:dabbcabcd out:4
def findSubString(strr):
    n = len(strr)

    # Count all distinct characters.
    unique_element = len(set([x for x in strr]))

    helper = defaultdict(lambda: 0)
    count = 0
    start = 0
    min_len = n

    # Now follow the algorithm discussed in below
    # post. We basically maintain a window of characters
    # that contains all characters of given string.
    for j in range(n):
        helper[strr[j]] += 1

        # If any distinct character matched,
        # then increment count
        if helper[strr[j]] == 1:
            count += 1

        # Try to minimize the window i.e., check if
        # any character is occurring more no. of times
        # than its occurrence in pattern, if yes
        # then remove it from starting and also remove
        # the useless characters.
        if count == unique_element:
            while helper[strr[start]] > 1:
                if helper[strr[start]] > 1:
                    helper[strr[start]] -= 1
                start += 1
            # Update window size
            len_window = j - start + 1
            print(len_window)
            if min_len > len_window:

                min_len = len_window
                start_index = start

                # Return substring starting from start_index
    # and length min_len """
    end_endex = start_index + min_len
    print(end_endex)
    return str(strr[start_index: end_endex])


if __name__ == '__main__':
    givenString = input()
    result = findSubString(givenString)
    print(result)
