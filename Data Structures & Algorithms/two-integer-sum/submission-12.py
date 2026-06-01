class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i, num in enumerate(nums):
            if target-num in map1:
                return [map1[target-num], i]
            map1[num] = i
        return []