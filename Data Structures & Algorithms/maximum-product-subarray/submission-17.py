class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP=1
        minP=1
        res = float('-inf')
        for n in nums:
            temp = maxP
            maxP = max(n, minP*n, maxP*n)
            minP = min(n, temp*n, minP*n)
            res = max(res, maxP)
        return res