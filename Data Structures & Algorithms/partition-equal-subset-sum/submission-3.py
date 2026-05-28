class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
        