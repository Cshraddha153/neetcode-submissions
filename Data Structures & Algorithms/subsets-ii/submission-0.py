class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def dfs(i, sublist):
            if i==len(nums):
                return res.add(tuple(sublist))
            sublist.append(nums[i])
            dfs(i+1, sublist)
            sublist.pop()
            dfs(i+1, sublist)
        
        dfs(0, [])
        return [list(s) for s in res]
        
