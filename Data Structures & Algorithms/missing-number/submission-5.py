class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            j = i+1
            res = res ^ j ^ nums[i]
            print(res)
        return res