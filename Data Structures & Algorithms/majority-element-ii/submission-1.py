class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
            if len(count)<=2:
                continue
            
            new_count = defaultdict(int)
            for num, c in count.items():
                if c>1:
                    new_count[num] = c-1
            count = new_count
        
        res = []
        for num in count:
            if nums.count(num) > len(nums)//3:
                res.append(num)
        return res



        # tc=O(N)  sc=O(N)
        count = Counter(nums)
        res = []
        for key in count:
            if count[key]> len(nums)//3:
                res.append(key)
        return res

        # tc=O(N^2) sc=O(N)
        res = set()
        for num in nums:
            count = sum(1 for i in nums if i==num)
            if count>len(nums)//3:
                res.add(num)
        return list(res)