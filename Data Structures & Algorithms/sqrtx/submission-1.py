class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        if x==0:
            return 0
        
        res=1
        for i in range(1, x+1):
            if i*i>x:
                return res
            res = i
        return res


        # binary search
        # l, r = 0, x
        # res = 0
        # while l<=r:
        #     m = (l+r)//2
        #     if m*m <x:
        #         l = m+1
        #         res = m
        #     elif m*m > x:
        #         r=m-1
        #     else:
        #         return m
        # return res