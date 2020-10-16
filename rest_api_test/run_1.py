import math
import os
import random
import re
import sys
import requests

sys.stdin = open('input_1.txt', 'r')
sys.stdout = open('output_1.txt', 'w')


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#

def getWinnerOfCompet(competition, year):
    c_url = "https://jsonmock.hackerrank.com/api/football_competitions?name=" + competition + "&year=" + str(year)
    c_rsp = requests.get(c_url).json()
    return c_rsp["data"][0]["winner"]

def getTotalGoalsByPage(url, page, teamgoals):
    p_goals = 0
    url = url + "&page=" + str(page)
    rsp = requests.get(url).json()
    p_goals += sum([int(x[teamgoals]) for x in rsp["data"]])
    return p_goals

def getTotalGoalsByType(compet, team, year, m_type=1):
    goals = 0
    b_url = "https://jsonmock.hackerrank.com/api/football_matches?competition="+compet
    if m_type == 1:
        url = b_url + "&year=" + str(year) + "&team1=" + team
        type_goal = "team1goals"
    else:
        url = b_url + "&year=" + str(year) + "&team2=" + team
        type_goal = "team2goals"
    init_call = requests.get(url).json()
    data = init_call["data"]
    max_pages = init_call["total_pages"]
    goals += sum([int(r[type_goal]) for r in data])
    for k in data:
        print(k)
    for i in range(2, max_pages + 1):
        goals += getTotalGoalsByPage(url, i, type_goal)
    return goals

def getWinnerTotalGoals(competition, year):
    team = getWinnerOfCompet(competition, year)
    return getTotalGoalsByType(competition, team, year) + getTotalGoalsByType(competition, team, year, m_type=0)


if __name__ == '__main__':
    competition = input()
    year = int(input().strip())
    result = getWinnerTotalGoals(competition, year)
    print(result)
