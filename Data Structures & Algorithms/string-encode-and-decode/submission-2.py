class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        i=0
        res = []
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i: j])
            print(length)
            res.append(s[j+1: j+length+1])
            i=j+length+1            

        return res
