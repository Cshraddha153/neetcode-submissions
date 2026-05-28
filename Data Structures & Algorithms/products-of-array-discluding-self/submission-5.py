class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force   tc=O(n^2)   sc=O(1)
        res = [0]*len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                prod*=nums[j]
            res[i]=prod
        return res



        # TC=O(N)   sc=O(N) space for o/p array 
        # res = [1]*(len(nums))
        # pre = 1
        # for i in range(len(nums)):
        #     res[i] = pre
        #     pre*=nums[i]
        
        # post = 1
        # for i in range(len(nums)-1, -1, -1):
        #     res[i]*=post
        #     post*=nums[i]
        # print(res)
        # return res