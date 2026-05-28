class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x : x[1])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if start < end:  # Overlapping interval found
                count += 1
            else:
                end = intervals[i][1]  # Update the end of the non-overlapping interval
        return count
        
            
