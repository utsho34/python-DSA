class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        res = [0] * N
        for i in range(N):
            left = [i - j for j in range(i) if boxes[j] == "1"]
            right = [j - i for j in range(i + 1, N) if boxes[j] == "1"]
            res[i] = sum(left) + sum(right)
        return res