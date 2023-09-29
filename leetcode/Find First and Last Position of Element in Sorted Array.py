class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        N = len(nums)
        start, end = -1, -1
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if left < N and nums[left] == target: start = left
        left, right = 0, N
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

            if nums[right - 1] == target: end = right - 1

        return [start, end]