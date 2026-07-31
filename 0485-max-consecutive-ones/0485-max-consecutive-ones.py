class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        c1 = 0
        for i in range (len(nums)):
            if nums[i] == 1:
                c+=1
            else:
                c = 0
            c1 = max(c1,c)
        return c1