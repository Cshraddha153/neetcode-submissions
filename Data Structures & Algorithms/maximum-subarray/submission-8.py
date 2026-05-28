class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        # t.c-->O(n^2)   s.c--->O(1)
        # res = -10000
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     ans = nums[i]
        #     for j in range(i+1, len(nums)):
        #         ans = ans + nums[j]
        #         res = max(ans, res, nums[j], nums[i])
        # return res

        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum


        
