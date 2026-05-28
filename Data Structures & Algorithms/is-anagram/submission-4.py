class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # tc = O(n)   sc=O(N)
        if len(s) != len(t):
            return False
        counts, countt = {}, {}
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)
        
        for c in countt:
            if countt[c] != counts.get(c, 0):
                return False
        return True