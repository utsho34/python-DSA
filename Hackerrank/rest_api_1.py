#!/bin/python3

import requests
import os

def getTotalGoals(team, year):
    total_goals = 0

    # Fetch goals where team is team1
    response = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1').json()
    total_pages = response['total_pages']

    for page in range(1, total_pages + 1):
        response = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}').json()
        for match in response['data']:
            total_goals += int(match['team1goals'])

    # Fetch goals where team is team2
    response = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1').json()
    total_pages = response['total_pages']

    for page in range(1, total_pages + 1):
        response = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}').json()
        for match in response['data']:
            total_goals += int(match['team2goals'])

    return total_goals

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input().strip()
    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')
    fptr.close()
