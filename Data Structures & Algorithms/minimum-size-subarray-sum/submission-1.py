class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)
        l=0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total>=target:
                res = min(res, r-l+1)
                total-=nums[l]
                l+=1
        return 0 if res==float("inf") else res




        # for i in range(n):
        #     cur_sum = 0
        #     for j in range(i, n):
        #         cur_sum += nums[j]
        #         if cur_sum >= target:
        #             res = min(res, j-i+1)
        #             break
        # return 0 if res==float('inf') else res