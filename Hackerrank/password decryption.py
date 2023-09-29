#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    # Write your code here
    s = list(s)
    i = 0
    while i < len(s) and s[i].isdigit() and s[i] != "0":
        i = i + 1
    for j, k in enumerate([m for m in range(i, len(s)) if s[m] == "0"]):
        s[k] = s[i - j - 1]
    for j in range(i, len(s)):
        if s[j] == "*":
            s[j - 1], s[j - 2] = s[j - 2], s[j - 1]
    return "".join(s[i:]).replace("*", "")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()
