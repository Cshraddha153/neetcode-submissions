class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2)<---t.c  O(1)<<--s.c
        # res = 0
        # b = 0
        # for i in range(len(prices)):  
        #     a = prices[i]
        #     for j in range(i+1, len(prices)):
        #         b = max(a, prices[j])
        #         res = max(res, b-a)          
        # return res

        # O(n)<---t.c  O(1)<<--s.c
        left, right = 0, 1
        maxProfit = 0
        while right<len(prices):
            if (prices[left]<prices[right]):
                maxProfit=max(maxProfit,prices[right]-prices[left])
            else:
                left = right
            right+=1
        return maxProfit


