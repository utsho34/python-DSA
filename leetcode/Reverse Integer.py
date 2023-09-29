class Solution(object):
    def reverse(self, x):
        result = 0
        negative = 1
        if x < 0:
            x = x * -1
            negative = - 1
        while (x != 0):
            result = result * 10 + x%10
            x = x//10
        if (-2**31) <= result <= (2**31 - 1):
                return result * negative
        return 0