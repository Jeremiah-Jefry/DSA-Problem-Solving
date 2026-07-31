class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = maximum = 0

        for num in nums:
            current = current + 1 if num == 1 else 0
            maximum = max(maximum, current)

        return maximum