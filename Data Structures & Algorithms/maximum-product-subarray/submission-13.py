class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # T.C-->O(n^2)    S.C--->O(1)
        # final_max_prod = -1000000
        # current_prod = 1
        # for i in range(len(nums)):
        #     current_prod = nums[i]
        #     for j in range(i+1, len(nums)):
        #         current_prod = current_prod*nums[j]
        #         final_max_prod = max(current_prod, final_max_prod, nums[i], nums[j])
        # return max(final_max_prod, nums[0]) 

        # T.C-->O(n^2)    S.C--->O(1)
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num<0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(nums[i], max_prod*nums[i])
            min_prod = min(nums[i], min_prod*nums[i])

            res = max(max_prod, res)
        return res





