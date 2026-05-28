class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = {}
        for i, ele in enumerate(nums):
            if ele not in map1:
                map1[ele]=1
            else:
                map1[ele]+=1
            if map1[ele]>1:
                return True
        
        return False