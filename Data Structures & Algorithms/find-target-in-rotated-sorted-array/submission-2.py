class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: O(logn)   Space complexity: O(1)
        # left=0
        # right=len(nums)-1
        # while left<=right:
        #     mid = left + (right-left)//2
        #     if nums[mid]==target:
        #         return mid
            
        #     if nums[left] <= nums[mid]:
        #         if nums[mid] < target or target<nums[left]:
        #             left = mid+1
        #         else:
        #             right = mid -1

        #     else:
        #         if target < nums[mid] or nums[right]< target:
        #             right = mid-1
        #         else:
        #             left = mid+1
        # return -1

        # Time complexity: O(n)   Space complexity: O(1)

        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

