class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goal = set()
        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                print(t[0], t[1], t[2])
                continue
            for i, v in enumerate(t):
                if target[i]==v:
                    goal.add(i)
        return len(goal)==3
            
            