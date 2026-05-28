class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            digit = bin(i)
            one = digit.count('1')
            res.append(one)
        return res



        