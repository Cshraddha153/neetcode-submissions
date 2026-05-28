class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num=[]
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i]+nums[j]==target):
                    num.append(i)
                    num.append(j)
                    return num
                else:
                    j+=1
                
