class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)
        return stones[0] if stones else 0







        # tc=O(nlog n)  sc=O(1)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
       
        while len(stones) > 1:
            F = heapq.heappop(stones)
            S = heapq.heappop(stones) #O(log n)
            if F!=S:
                heapq.heappush(stones, F-S)
        
        stones.append(0)
        return -stones[0] 

