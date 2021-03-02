# question link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        
        for s, e, p in jobs:
            idx = bisect.bisect(dp, [s + 1]) - 1
            cur = dp[idx][1] + p
            if cur > dp[-1][1]:
                dp.append([e, cur])
        
        return dp[-1][1]
