class Solution:
    def getSum(self, a: int, b: int) -> int:
        # TC=O(1)  sc=O(1)

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b!=0:
            carry = (a&b)<<1
            a = (a^b) & mask
            b = carry & mask
            print(a)
        return a if a<= max_int else ~(a^mask) 
