class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False



        # # /tc=O(nlogn) sc=O(1)-->sorting
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False