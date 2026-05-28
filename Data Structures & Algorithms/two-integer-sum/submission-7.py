class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # num=[] #list
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             num.append(i) # list append
        #             num.append(j)
        #             return num
                
                # T.C---> O(n^2)

        # Map
        mapp = {}
        for i, number in enumerate(nums):
            difference = target - number
            if difference in mapp:
                return [mapp[difference], i]
            mapp[number] = i


                
