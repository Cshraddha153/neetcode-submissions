class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [] 
        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1]=max(res[-1][1], interval[1])
        return res

























        # res = []
        # ans = []
        # for i in range(len(intervals)-1):
        #     a = intervals[i]
        #     b = intervals[i+1]
        #     for j in range(2):
        #         if a[j]==b[j] or a[j]==b[j-1]:
        #             ans.append(a[j])                       
        #         elif a[j]<b[j] or a[j]>b[j]:
        #             a[j]=max(a[j], b[j])
        #             ans.append(a[j])
        #         else:
        #             ans.append(intervals[i])
        #     res.append(ans) 
        # return res
                




