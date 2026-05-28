class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]



        # tc = O(N)   sc=O(N)
        nums = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            nums.append([dist, x, y])

        heapq.heapify(nums)

        while k: 
            dist, x, y = heapq.heappop(nums)  # TC =  k*logN
            res.append([x, y])
            k-=1
        
        return res