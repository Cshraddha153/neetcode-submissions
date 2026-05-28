class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in range(len(s)):
            if s[i] in dic:
                if stack and stack[-1]==dic[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if len(stack)==0 else False
