from itertools import pairwise

from typing import List


class Solution:

    def isArraySpecial(self, nums: List[int]) -> bool:

        # Check if the array is 'special' by ensuring adjacent pairs

        # of elements have different parity (one is even, the other is odd)

        return all(a % 2 != b % 2 for a, b in pairwise(nums))