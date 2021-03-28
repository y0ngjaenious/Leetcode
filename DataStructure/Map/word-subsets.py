# question link: http://leetcode.com/problems/word-subsets/

from collections import Counter, defaultdict
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter = Counter()
        for b in B:
            counter |= Counter(b)         
        return [a for a in A if not counter - Counter(a)]
