class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            diff = target - numbers[i]
            while l<r:
                m = (l+r)//2
                if diff == numbers[m]:
                    return [i+1, m+1]
                elif diff>numbers[m]:
                    l = m+1
                else:
                    r = m-1






        # two pointers
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1
