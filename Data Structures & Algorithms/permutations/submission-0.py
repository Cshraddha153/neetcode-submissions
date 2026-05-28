class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0) 
            perms = self.permute(nums)
            print("perms=",perms, "nums=", nums)
            for perm in perms:
                perm.append(n)
                print("perm", perm,"perms=",perms)
            print("i =", i, "n=",n ,"perms=",perms)
            result.extend(perms)
            print("res", result)
            nums.append(n)
        return result
