class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i,val in enumerate(nums):
            temp = target - val
            if temp in mapp:
                return {i,mapp[temp]}
            mapp[val]=i
        
