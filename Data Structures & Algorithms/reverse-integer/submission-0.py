class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1
        
        ans=0
        while x: 
            digit = int(math.fmod(x, 10)) # for floating-point numbers and can behave differently with negative numbers.
            x= int(x/10)

            if ans>MAX//10 or (ans==MAX//10 and digit>MAX%10):
                return 0
            if ans<MIN//10 or (ans==MIN//10 and digit<MIN%10):
                return 0
            ans = (ans*10) + digit
        return ans
            
