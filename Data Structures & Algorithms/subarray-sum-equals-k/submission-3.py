class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap
        res = curr_sum = 0
        prefix_sum = {0:1}
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += prefix_sum.get(diff, 0)
            prefix_sum[curr_sum]=1+prefix_sum.get(curr_sum, 0)
        return res

        # # brute force soln  --> tc=O(n2) sc=O(1)
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum==k:
        #             res+=1
        # return res