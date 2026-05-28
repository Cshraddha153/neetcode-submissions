class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # tc=O(N)  sc=O(M)
        # Two Pointers (Greedy)
        dic = {}
        for i, c in enumerate(s):
            dic[c] = i

        size=0
        res = []
        end=0
        for i, c in enumerate(s):
            size+=1
            end=max(end, dic[c])
            if i==end:
                res.append(size)
                size=0
        return res