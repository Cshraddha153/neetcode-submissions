class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brure force tc=O(N^2)   sc=O(1)
        res = 0
        for i in range(len(heights)):
            for j in range(1+1, len(heights)):
                res = max(res, min(heights[i], heights[j])*(j-i))


        # tc=O(n)  sc=O(1) two pointer
        area = 0
        l, r = 0, len(heights)-1
        while l<r:
            area = max(area, min(heights[l], heights[r])*(r-l))
            print(area, l, r)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return area
        