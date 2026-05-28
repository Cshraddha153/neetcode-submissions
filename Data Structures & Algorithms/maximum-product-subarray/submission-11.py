class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_max_prod = -1000000
        current_prod = 1
        for i in range(len(nums)):
            current_prod = nums[i]
            for j in range(i+1, len(nums)):
                current_prod = current_prod*nums[j]
                final_max_prod = max(current_prod, final_max_prod, nums[i], nums[j])
        return max(final_max_prod, nums[0]) 