class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
            
        def helper(nums):
            one = 0
            two = 0
            for n in nums:
                temp = max(n+one, two)
                one = two
                two = temp
            return two

        return max(helper(nums[1:]), helper(nums[:-1]))