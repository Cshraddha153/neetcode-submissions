class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ans = nums[0]
        while 0<=i<len(nums) and 0<=j<len(nums):
            if nums[i] < nums[j]:
                ans = min(ans, nums[i])
            elif nums[i]>nums[j]:
                ans=min(ans, nums[j])
            else:
                ans = min(ans, nums[i])
                break
            i+=1
            j-=1
        return ans
            