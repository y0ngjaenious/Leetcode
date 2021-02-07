# question link: https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        sol = []
        cur_s = intervals[0][0]
        cur_e = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur_e:
                sol.append([cur_s, cur_e])
                cur_s = intervals[i][0]
                cur_e = intervals[i][1]
            else:
                cur_e = max(cur_e, intervals[i][1])
        
        sol.append([cur_s, cur_e])
        
        return sol
