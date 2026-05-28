class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n)--tc   O(1)--sc
        # left=0
        # right=len(heights)-1
        # ans=0
        # area=0
        # while left<right:
        #     area = min(heights[left], heights[right]) * (right-left)
        #     if heights[left]>heights[right]:
        #         right-=1
        #     else:
        #         left+=1

        #     ans = max(ans, area)
        # return ans
        area = 0
        ans = 0    
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                ans = max(ans, area)
        return ans
