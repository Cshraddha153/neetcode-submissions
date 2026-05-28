class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # t.c-->O(n^2)  s.c--->O(n)
        # res = []        
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             prod = prod*nums[j]
        #     res.append(prod)
        # return res 


        # t.x-->O(n)    s.c--->O(n)
        res = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

