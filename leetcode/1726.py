class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        productMap = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                mult = nums[i] * nums[j]
                productMap[mult] += 1
        for key in productMap:
            freq = productMap[key]
            if freq > 1:
                count += (freq * (freq - 1) // 2) * 8
        return count