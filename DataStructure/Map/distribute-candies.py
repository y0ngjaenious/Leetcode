# question link: https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dic = {}
        t = 0
        for c in candyType:
            if c not in dic:
                dic[c] = 1
                t += 1
                
        return min(t, int(len(candyType) / 2))
