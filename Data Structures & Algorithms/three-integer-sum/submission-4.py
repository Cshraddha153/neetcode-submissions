class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # t.c --> O(n^2)  Pointers
        # res = []
        # nums.sort()
        # for i, a in enumerate(nums):
        #     if a>0:
        #         break

        #     if i>0 and a==nums[i-1]:
        #         continue
            
        #     left=i+1
        #     right=len(nums)-1
        #     while left<right:
        #         sum = nums[left]+nums[right]+a
        #         if sum>0:
        #             right-=1
        #         elif sum<0:
        #             left+=1
        #         else:
        #             res.append([a, nums[left], nums[right]])
        #             left+=1
        #             right-=1
        #             while nums[left]==nums[left-1] and left<right:
        #                 left+=1
        # return res

        # hashmap
        
        nums.sort()
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1

        for i in range(len(nums)):
            count[nums[i]]-=1
            if nums[i]==nums[i-1] and i>0:
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]]-=1
                if nums[j]==nums[j-1] and j-1>i:
                    continue

                target = -(nums[i]+nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):
                count[nums[j]]+=1
        return res















