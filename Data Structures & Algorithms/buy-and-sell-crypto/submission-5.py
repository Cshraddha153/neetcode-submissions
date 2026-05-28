class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2)<---t.c  O(1)<<--s.c
        res = 0
        b = 0
        for i in range(len(prices)):  
            a = prices[i]
            for j in range(i+1, len(prices)):
                b = max(a, prices[j])
                res = max(res, b-a)          
        return res