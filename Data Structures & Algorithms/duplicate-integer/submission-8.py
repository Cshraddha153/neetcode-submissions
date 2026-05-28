class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # tc-->O(n) sc--->O(n)
        # map1 = {}
        # for i, ele in enumerate(nums):
        #     if ele not in map1:
        #         map1[ele]=1
        #     else:
        #         map1[ele]+=1
        #     if map1[ele]>1:
        #         return True       
        # return False

        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            map[nums[i]] = i
        return False

