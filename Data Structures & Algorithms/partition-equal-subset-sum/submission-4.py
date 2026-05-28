class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        













        # Recursion  tc=O(2^n)  sc=O(N)
        if sum(nums)%2:
            return False
        
        def dfs(i, target):
            if i>=len(nums):
                return target==0
            if target<0:
                return False
            return dfs(i+1, target) or dfs(i+1, target-nums[i])

        return dfs(0, sum(nums)//2)

















        # Time complexity: O(n*target)  sc=O(n∗target)  dp + hashet
        total = sum(nums)
        if total % 2: # odd
            return False
        half = total//2
        subset = set()
        subset.add(0)

        for i in range(len(nums)):
            temp=set()
            for ele in subset:
                temp.add(ele + nums[i])
            subset.update(temp)
            if half in subset:
                return True
        return half in subset
        