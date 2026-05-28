class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        for i in range(1, len(nums)):
            mini = min(mini, nums[i])
        return mini