#!/bin/python3

import math
import os
import random
import re
import sys
import requests

sys.stdin = open('input_.txt', 'r')
sys.stdout = open('output_.txt', 'w')


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def getTotalByPage(url, page):
    number_page = 0
    url = url + "&page=" + str(page)
    rsp = requests.get(url).json()
    data = rsp["data"]
    #number_page += sum(x.get('team1goals') == x.get('team1goals') for x in data)
    number_page += len(data)
    return number_page


def getNumDraws(year):
    number = 0
    for j in range(11):
        url = "https://jsonmock.hackerrank.com/api/football_matches?team1goals="+str(j)+"&team2goals="+str(j)+"&year="+str(year)
        first_call = requests.get(url).json()
        number += first_call["total"]
    return number


if __name__ == '__main__':
    year = int(input().strip())
    result = getNumDraws(year)
    print(result)
