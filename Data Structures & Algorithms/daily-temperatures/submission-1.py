class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        res = [0]*(len(temperatures))
        for i, temp in enumerate(temperatures):
            # start = i
            while stack and stack[-1][0]<temp:
                temp1, index1 = stack.pop()
                res[index1] = i - index1
                # start = i
            stack.append([temp, i])
        return res
