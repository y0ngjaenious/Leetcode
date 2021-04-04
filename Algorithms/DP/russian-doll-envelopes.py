# question link: http://leetcode.com/problems/russian-doll-envelopes

# think about [[3, 7], [4, 5], [5, 6]]
# the answer should be 2
# maybe DP..
from functools import cmp_to_key
def compare(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] > y[1]:
            return -1
        elif x[1] < y[1]:
            return 1
        else:
            return 0
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=cmp_to_key(compare))
        nums, lis = [j for _, j in envelopes], []
        for current in nums:
            idx = bisect.bisect_left(lis, current)
            lis[idx:idx+1] = [current]
            print(lis)
        return len(lis)
