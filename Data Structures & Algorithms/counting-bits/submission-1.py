class Solution:
    def countBits(self, n: int) -> List[int]:
        # t.c-->O(n)    sc--->O(1)
        # dp = [0]*(n+1) 
        # offset = 1 
        # for i in range(1, n+1): 
        #     if offset*2 == i: 
        #         offset = i 
        #     dp[i] = 1 + dp[i - offset]  
        # return dp 

        return [bin(i).count('1') for i in range(n+1)]
        
