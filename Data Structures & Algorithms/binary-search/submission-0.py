class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #O(N)t.c   s.c=O(1)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1