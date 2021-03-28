# question link: http://leetcode.com/problems/3sum-with-multiplicity

from collections import defaultdict, Counter
from itertools import combinations_with_replacement

def c2(n):
    return n * (n - 1) / 2

def c3(n):
    return n * (n - 1) * (n - 2) / 6

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = Counter(sorted(arr))
        sol = 0
        for i, j in combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k:
                sol += c3(c[i])
            elif i == j != k:
                sol += c2(c[i]) * c[k]
            elif j < k:
                sol += c[i] * c[j] * c[k]
        return int(sol) % (10 ** 9 + 7)
