class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k %= n
        def reverse(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)



        # n=len(nums)
        # tmp = [0]*n
        # for i in range(n):
        #     tmp[(i+k)%n] = nums[i]
        # nums[:] = tmp



        
        # n = len(nums)
        # k %= n
        # while k:
        #     tmp = nums[n - 1]
        #     for i in range(n - 1, 0, -1):
        #         nums[i] = nums[i - 1]
            
        #     nums[0] = tmp
        #     print(k, nums)
        #     k -= 1

        