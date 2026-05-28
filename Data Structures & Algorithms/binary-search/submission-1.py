class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #O(logn)=tc   s.c = O(1)  two pointer
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        return -1




        #O(N)t.c   s.c=O(1)  for loop
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1