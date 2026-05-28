class Solution:
    def countBits(self, n: int) -> List[int]:
        #Dp
        dp = [0]*(n+1)
        offset=1
        for i in range(1, n+1):
            if offset*2==i:
                offset=i
            dp[i] = 1+dp[i-offset]
        return dp




        # Tc= O(nlogn)  sc=O(1)
        res = []
        for i in range(n+1):
            digit = bin(i) # O(logn)
            one = digit.count('1')
            res.append(one)
        return res



        