# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix  is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
#
# Function description
#
# Complete the  function in the editor below.
#
# diagonalDifference takes the following parameter:
#
# int arr[n][m]: an array of integers
# Return
#
# int: the absolute diagonal difference
# Input Format
#
# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .
#
# Constraints
#
# Output Format
#
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
#
# Inputcopy	Outputcopy
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# 15
# Explanation
#
# The primary diagonal is:
#
# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4
#
# The secondary diagonal is:
#
#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15
#
# Note: |x| is the absolute value of x
#
# Sponsor

def diagonalDifference(matrix):
    dig_1 = 0
    dig_2 = 0
    l = len(matrix[0])
    for i in range(l):
        dig_1 += matrix[i][i]
        dig_2 += matrix[i][(l - i - 1)]
    return abs(dig_1 - dig_2)


n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(array)
print(result)
