# question link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[-float('inf'), 0]]
        for p in prices:
            app = []
            app.append(max(dp[-1][1] - p - fee, dp[-1][0]))
            app.append(max(dp[-1][0] + p, dp[-1][1]))
            dp.append(app)
        
        return max(dp[-1])
