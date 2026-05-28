class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        ans = 0
        b = 0
        for i in range(len(prices)):
            a = prices[i]
            for j in range(i+1, len(prices)):
                b = max(a, prices[j])
                res = max(res, b-a)
            # ans = max(0,res)
        return res