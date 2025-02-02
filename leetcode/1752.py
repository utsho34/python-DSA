from typing import List


class Solution:

    def check(self, nums: List[int]) -> bool:
        decrease_count = 0
        for i, value in enumerate(nums):
            if nums[i - 1] > value:
                decrease_count += 1
        return decrease_count <= 1