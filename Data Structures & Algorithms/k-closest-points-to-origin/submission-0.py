class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            nums.append([dist, x, y])
        print(nums)
        heapq.heapify(nums)
        print(nums)
        while  k:
            dist, x, y = heapq.heappop(nums)
            res.append([x, y])
            k-=1
        print(res)
        return res