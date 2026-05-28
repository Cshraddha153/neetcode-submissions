class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for key in count:
            if count[key]> len(nums)//3:
                res.append(key)
        return res


        res = set()
        for num in nums:
            count = sum(1 for i in nums if i==num)
            if count>len(nums)//3:
                res.add(num)
        return list(res)