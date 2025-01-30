#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#
API_URL = "https://jsonmock.hackerrank.com/api/football_matches"


def getNumDraws(year):
    total = 0
    for goals in range(12):
        url = f"{API_URL}?year={year}&team1goals={goals}&team2goals={goals}"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            total += result.get("total", 0)
    return total


# getNumDraws
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
