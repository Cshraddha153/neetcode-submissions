class Solution:
    def partition(self, nums, left, right):
        mid = (left+right)>>1
        nums[mid], nums[left+1] = nums[left+1], nums[mid]

        if nums[left]>nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left+1] > nums[right]:
            nums[left+1], nums[right] = nums[right], nums[left+1]
        if nums[left]>nums[left+1]:
            nums[left], nums[left+1] = nums[left+1], nums[left]
        
        pivot = nums[left+1]
        i = left+1
        j=right
        while True:
            while True:
                i+=1
                if not nums[i]<pivot:
                    break
            while True:
                j-=1
                if not nums[j]>pivot:
                    break
            if i>j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left+1], nums[j] = nums[j], nums[left+1]
        return j
    
    def quickSort(self, nums, left, right):
        if right<=left+1:
            if right==left+1 and nums[right]<nums[left]:
                nums[left], nums[right] = nums[right], nums[left]
            return
        
        j = self.partition(nums, left, right)
        self.quickSort(nums, left, j-1)
        self.quickSort(nums, j+1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        # quick sort    tc=O(nlog) sc=O(logn)
        self.quickSort(nums, 0, len(nums)-1)
        return nums



        # tc=O(nlogn) sc=O(N)
        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0
            while j<len(left) and k < len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                nums[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                nums[i]=right[k]
                k+=1
                i+=1

        def mergeSort(arr, l, r):
            if l==r:
                return arr
            m = (l+r)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        return mergeSort(nums, 0, len(nums)-1)



        # bubble sort tc=O(n^2)
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j]<nums[i]:
        #             nums[j], nums[i] = nums[i], nums[j]
        # return nums