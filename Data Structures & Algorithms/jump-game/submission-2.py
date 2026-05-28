class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # if nums[0]==0:
        #     return True

        def dfs(i):
            if i>=len(nums)-1:
                return True
            l=0
            r=nums[i]
            for j in range(1, r+1):
                if dfs(i+j):
                    return True
            return False
        
        return dfs(0)




















