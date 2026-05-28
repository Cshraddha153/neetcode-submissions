class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        temp=0
        for i in range(len(nums)):
            if temp<0:
                temp=0
            temp = temp+nums[i]
            ans = max(ans, temp)
            print("ans=", ans)
        return ans