class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search
        l, r = max(weights), sum(weights)
        res = r
        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships+=1
                    if ships>days:
                        return False
                    currCap = cap
                currCap -= w
            return True
        
        while l<=r:
            cap = (l+r)//2
            if canShip(cap):
                res = min(res, cap)
                r = cap-1
            else:
                l = cap+1
        return res



        # linear search tle
        # res = max(weights)
        # while True:
        #     ships = 1
        #     cap = res
        #     for w in weights:
        #         if cap - w <0:
        #             ships += 1
        #             cap = res
        #         cap-=w
            
        #     if ships<=days:
        #         return  res
            
        #     res+=1