#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countPairs(arr):
    # Write your code here
    p = lambda x: x > 0 and not (x & (x - 1))
    dic = defaultdict(int)
    for i in arr:
        dic[i] += 1
    dic = list(dic.items())
    sol = 0
    for j in range(len(dic)):
        x, x_count = dic[j]
        for k in range(j, len(dic)):
            y, y_count = dic[k]
            if p(x & y):
                if x == y:
                    sol += (x_count * (x_count - 1)) // 2
                else:
                    sol += x_count * y_count
    return sol


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
