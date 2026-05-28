class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        length=0
        l=0
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] = 1 + count.get(ord(s[r]) - ord('a') , 0)
            print(count)

            while count[ord(s[r]) - ord('a')]>1:              
                count[ord(s[l]) - ord('a')] -=1
                l+=1
            
            if r-l+1 > length:
                length = r-l+1
         
        return length
            