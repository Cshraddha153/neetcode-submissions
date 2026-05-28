class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        ans=0
        area=0
        while left<right:
            area = min(heights[left], heights[right]) * (right-left)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
            
            ans = max(ans, area)
        return ans
            
