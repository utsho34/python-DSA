class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        input_list = {}
        for i, n in enumerate(numbers):
            comp = target - n
            if comp in input_list:
                return [input_list[comp], i]
            input_list[n] = i
