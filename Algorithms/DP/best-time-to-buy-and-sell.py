# question link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin = 100000
        curmax = -1
        curPro = 0
        for i in prices:
            if i < curmin:
                curmin = i
                curmax = i
                continue
            if i > curmax:
                curmax = i
                if curmax - curmin > curPro:
                    curPro = curmax - curmin
        return curPro 
