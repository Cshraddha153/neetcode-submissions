class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, j):
            if i==len(nums):
                return 0

            LIS = dfs(i+1, j) # not include

            if j==-1 or nums[j]<nums[i]:
                LIS = max(LIS, 1 + dfs(i+1, i))
            return LIS

        return dfs(0, -1)

        # ans=0
        # for i in range(len(nums)-1, -1, -1):
        #     length=1
        #     ele = nums[i]
        #     print("ele", ele)
        #     for j in range(i-1, -1, -1):
        #         if nums[j]<ele:
        #             print("nums[j]", nums[j], j)
        #             length+=1
        #             ele = nums[j]
        #             print(ele)
        #     ans = max(ans, length)
        # return ans