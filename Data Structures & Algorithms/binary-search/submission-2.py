class Solution:
    def rec(self, l, r, num, target):
        if l>r:
            return -1
        m = (l+r)//2
        if num[m]==target:
            return m
        if num[m]<target:
            return self.rec(m+1, r, num, target)
        return self.rec(l, m-1, num, target)


    def search(self, nums: List[int], target: int) -> int:
        # Recursive Binary Search  T.c=O(logn)  S.c=O(logn)
        return self.rec(0, len(nums)-1, nums, target)













        #O(logn)=tc   s.c = O(1)  two pointer (Iterative)
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