class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        length = 0
        for n in hashset:
            if n-1 not in hashset:
                longest=1
                while n + longest in hashset:
                    longest+=1
                length = max(length, longest)
        return length

