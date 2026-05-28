class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        
        hashmap = Counter(hand)
        for num in hand:
            start = num
            while hashmap[start-1]:
                start-=1
            while start<=num:
                while hashmap[start]:
                    for i in range(start, start+groupSize):
                        if not hashmap[i]:
                            return False
                        hashmap[i]-=1
                start+=1
        return True



























        # Sorting  tc=O(Nlogn)  sc=O(N)
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True





        # Hash Map  tc=sc=O(N)
        if len(hand)%groupSize !=0:
            return False
        
        count = Counter(hand)
        for num in hand:
            start = num
            while count[start-1]:
                start-=1

            while start <= num:
                while count[start]:
                    for i in range(start, start+groupSize):
                        if not count[i]:
                            return False
                        count[i]-=1
                start+=1        
        return True

























