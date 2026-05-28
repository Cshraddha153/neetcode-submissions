class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
    def add(self, val: int) -> int:
        # tc=O(m*nlogn)  sc=O(m)   O(n)  sorting
        # self.minheap.append(val)  nlogn
        # self.minheap.sort()
        # return self.minheap[len(self.minheap)-self.k]


        heapq.heappush(self.minheap, val)
        if len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        ans = self.minheap[0]
        return ans


