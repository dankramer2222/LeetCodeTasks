class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MaxSub = nums[0]
        CurSum = 0
        for n in nums:
            if (CurSum<0):
                CurSum=0
            CurSum += n
            MaxSub = max(MaxSub,CurSum)
        return MaxSub