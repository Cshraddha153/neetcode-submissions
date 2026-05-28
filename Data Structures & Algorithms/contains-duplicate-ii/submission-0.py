class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp and i-mp[nums[i]]<=k:
                return True
            mp[nums[i]]=i
        return False


        for L in range(len(nums)):
            for R in range(L+1, min(len(nums), L+k+1)):
                if nums[L]==nums[R]:
                    return True
        return False