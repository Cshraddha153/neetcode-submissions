class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        nums.sort()
        def dfs(i, total):
            if target==total:
                return res.append(sub.copy())
            
            for j in range(i, len(nums)):
                if j> i and nums[j]==nums[j-1]:
                    continue
                if total + nums[j]>target:
                    break
                sub.append(nums[j])
                dfs(j+1, total+nums[j])
                sub.pop()

        dfs(0, 0)
        return res
