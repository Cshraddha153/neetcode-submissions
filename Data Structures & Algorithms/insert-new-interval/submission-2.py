class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # greedy   tc=O(n)   sc=O(1) extra space and O(N) space for output list
        res = []
        for i in range(len(intervals)):
            # newinterval append ki wo sbse chota hai
            if intervals[i][0]>newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # kahi beech mei ayega
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res
