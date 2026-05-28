class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l=1
        r=ans
        while l<=r:
            m = (l+r)//2
            hours=0
            for p in piles:
                hours += math.ceil(p/m)
                if hours>h:
                    l = m+1
                    break
            if hours<=h:
                ans = min(m, ans)
                r = m-1              

        return ans



















        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile / speed)
            
        #     if totalTime <= h:
        #         return speed
        #     speed += 1
        # return speed










        # TLE
        # ans = max(piles)
        # for i in range(1, max(piles)):
        #     b = i
        #     hours = 0
        #     for j in range(len(piles)):
        #         hours = hours + math.ceil(piles[j]/b)
        #         if hours>h:
        #             break
        #     if hours<=h:
        #         ans = min(ans, b)
                
        # return ans