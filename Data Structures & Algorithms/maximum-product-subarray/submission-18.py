class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            res = max(res, nums[i])
            curr=1
            for j in range(i, len(nums)):
                curr*=nums[j]
                res = max(res, curr)
        return res

        # tc=O(N)   sc=O(1)   kadane's algo
        maxP=1
        minP=1
        res = float('-inf')
        for n in nums:
            temp = maxP
            maxP = max(n, minP*n, maxP*n)
            minP = min(n, temp*n, minP*n)
            res = max(res, maxP)
        return res