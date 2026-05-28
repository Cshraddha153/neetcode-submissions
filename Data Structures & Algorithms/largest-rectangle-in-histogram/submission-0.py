class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, value in enumerate(heights):
            start = i
            while stack and stack[-1][1]>heights[i]:
                ind, val = stack.pop()
                area = max(area, (i-ind)*val)
                start = ind            
            stack.append([start, value])
        print(stack)
        while stack:
            index, val = stack.pop()
            area = max(area, (len(heights)-index)*val)
        return area