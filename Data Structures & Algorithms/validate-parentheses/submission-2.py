class Solution:
    def isValid(self, s: str) -> bool:
        map1 = {']':'[', '}':'{', ')':'('}
        stack = []
        for val in s:
            if val in map1:
                if stack and stack[-1]==map1[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        return True if not stack else False
