class Solution:
    def rob(self, nums: List[int]) -> int:
        # rec + memo  (top-down approach)
        # dp = [-1]*(len(nums))
        # def solve(i):
        #     if i>=len(nums):
        #         return 0

        #     if dp[i]!=-1:
        #         return dp[i]

        #     dp[i] = max(nums[i]+solve(i+2), solve(i+1))
        #     return dp[i]

        # return solve(0)

        # bottom-up approach
        # if not nums:
        #     return 0
        # if len(nums)==1:
        #     return nums[0]
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        # return dp[-1]


        #space optimization
        prev1 = 0
        prev2 = 0
        for n in nums:
            temp = max(prev2, n+prev1)
            prev1 = prev2
            prev2 = temp          
        return prev2

