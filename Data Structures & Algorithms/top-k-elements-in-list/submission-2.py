class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap   tc=O(nlogk)  sc=O(n+k)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        
        # tc=O(n)=sc
        # count = {}
        # freq = [[] for i in range(len(nums)+1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # for num, cnt in count.items():
        #     freq[cnt].append(num)
        
        # res = []
        # for i in range(len(freq)-1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res)==k:
        #             return res
