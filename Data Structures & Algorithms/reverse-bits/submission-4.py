class Solution:
    def reverseBits(self, n: int) -> int:
        digit = 0
        for i in range(32):
            digit = digit<<1
            digit |= n & 1
            n = n>>1
        return digit