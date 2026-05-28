class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        length=0
        for i in range(len(s)):
            l, r = i, i
            while r<len(s) and l>=0 and s[l]==s[r]:
                
                if length<(r-l+1):
                    start = l
                    length = r-l+1
                l-=1
                r+=1
            
            l = i
            r = i+1 
            while r<len(s) and l>=0 and s[l]==s[r]:
                if length<(r-l+1):
                    start = l
                    length = r-l+1
                l-=1
                r+=1
            
        return s[start: start + length]
