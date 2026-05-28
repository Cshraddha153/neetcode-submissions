class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output



        
        # tc=O(n logn)   sc=O(N)
        intervals.sort()
        print(intervals)
        q = deque([intervals[0]])
        for i in range(len(intervals)):
            if q:
                if q[-1][1]>=intervals[i][0]:
                    start, end = q.pop()
                    q.append([min(start, intervals[i][0]), max(end, intervals[i][1]) ])
                else:
                    q.append(intervals[i])
        res = []
        while q:
            res.append(q.popleft())
        return res