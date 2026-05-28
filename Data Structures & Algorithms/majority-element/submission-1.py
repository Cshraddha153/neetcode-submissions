class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        res, max_count = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > max_count else res
            max_count = max(max_count, count[n])
        return res


        # res = count = 0
        # for num in nums:
        #     if count==0:
        #         res = num
        #     count += (1 if num == res else -1)
        # return res