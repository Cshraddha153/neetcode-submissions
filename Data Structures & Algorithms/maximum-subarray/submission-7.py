class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        # t.c-->O(n^2)   s.c--->O(1)
        res = -10000
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            ans = nums[i]
            for j in range(i+1, len(nums)):
                ans = ans + nums[j]
                res = max(ans, res, nums[j], nums[i])
        return res


