class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i, total):
            if total == target:
                return res.append(subset.copy())  #O(N)

            for j in range(i, len(nums)):
                if target<total + nums[j]:
                    return
                subset.append(nums[j])
                dfs(j, total + nums[j])
                subset.pop()
            

        dfs(0, 0)
        return res



        # tc nd sc = O(t/m)
        res = []
        subset = []
        def dfs(i, total):
            if i>=len(nums) or target<total:
                return
            if total == target:
                return res.append(subset.copy())  #O(N)
            
            subset.append(nums[i])
            dfs(i, total+nums[i])
            subset.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return res
