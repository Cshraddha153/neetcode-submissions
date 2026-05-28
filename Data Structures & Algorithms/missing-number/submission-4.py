class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # t.c --> O(n^2)  O(1)
        # for i in range(len(nums)+1):
        #     if i in nums:
        #         continue
        #     return i
        
        n = len(nums)
        exp_sum = n*(n+1)//2
        act_sum = sum(nums)
        return exp_sum - act_sum