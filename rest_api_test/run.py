import math
import os
import random
import re
import sys
import requests

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
def getTotalByPage(url, page, team1goals):
    goals_page = 0
    url = url + "&page=" + str(page)
    rsp = requests.get(url).json()
    data = rsp["data"]
    for r in data:
        goals_page += int(r[team1goals])
    return goals_page


def getGoalByMatchType(team, year, match_type="visit"):
    goal = 0
    base_url = "https://jsonmock.hackerrank.com/api/football_matches"
    if match_type == 'home':
        url = base_url + "?year=" + str(year) + "&team1=" + team
        type_goal = "team1goals"
    else:
        url = base_url + "?year=" + str(year) + "&team2=" + team
        type_goal = "team2goals"
    first_call = requests.get(url).json()
    data = first_call["data"]
    max_pages = first_call["total_pages"]
    for r in data:
        goal += int(r[type_goal])

    for i in range(2, max_pages + 1):
        goal += getTotalByPage(url, i, type_goal)
    return goal


def getTotalGoals(team, year):
    return getGoalByMatchType(team, year, "home") + getGoalByMatchType(team, year)


if __name__ == '__main__':
    team = input()
    year = int(input().strip())
    result = getTotalGoals(team, year)
    print(result)
