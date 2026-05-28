class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}
        for i in range(len(s)):
            map1[s[i]] = 1 + map1.get(s[i], 0)
            map2[t[i]] = 1 + map2.get(t[i], 0)

        for val in map2:
            if map1.get(val, 0) != map2[val]:
                return False
        return True


            
