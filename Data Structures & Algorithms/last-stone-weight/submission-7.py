class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
       
        while len(stones) > 1:
            F = heapq.heappop(stones)
            S = heapq.heappop(stones)
            if F!=S:
                heapq.heappush(stones, F-S)
        
        stones.append(0)
        return -stones[0] 

