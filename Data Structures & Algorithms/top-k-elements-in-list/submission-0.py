class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        count = defaultdict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        for key, val in count.items():
            freq[val].append(key)
        print(freq)

        res = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        return []
