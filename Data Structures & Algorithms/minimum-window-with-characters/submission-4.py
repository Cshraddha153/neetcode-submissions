class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        countt, counts = {}, {}
        for char in t:
            countt[char] = 1 + countt.get(char, 0)
        print("countt", countt)
        have, need = 0, len(countt)
        print(need)
        res = [-1, -1]
        minlen = float("infinity")
        l=0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            if s[r] in countt and countt[s[r]]==counts[s[r]]:
                have+=1
            while have==need:
                if minlen>(r-l+1):
                    res = [l, r]
                    minlen = min(minlen, r-l+1)
                counts[s[l]]-=1
                if s[l] in countt and counts[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l:r+1] if minlen != float("infinity") else ""


