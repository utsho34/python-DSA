class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        i = 0
        diff = 0
        for n in nums:
            res = max(res, n * diff)
            i = max(i, n)
            diff = max(diff, i - n)
        return res
