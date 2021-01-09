# qusetion link: https://leetcode.com/problems/maximum-subarray/

# Divide and Conquer
"""
class Solution:
    def maxSub(self, s, t):
        if s == t:
            return self.nums[s]
        m = int((s + t) / 2)
        sol_l = self.maxSub(s, m)
        sol_r = self.maxSub(m+1, t)
        subsol_l = -2 ** 31
        cur_sum = 0
        for i in range(m, s -1, -1):
            cur_sum += self.nums[i]
            if cur_sum > subsol_l:
                subsol_l = cur_sum
        subsol_r = -2 ** 31
        cur_sum = 0
        for i in range(m+1, t+1):
            cur_sum += self.nums[i]
            if cur_sum > subsol_r:
                subsol_r = cur_sum
        return max(sol_l, sol_r, subsol_l + subsol_r)
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums = nums
        return self.maxSub(0, len(nums) - 1)
"""

# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        opt = []
        sol = -2 ** 31
        for i in nums:
            if not opt:
                cur = i
            else:
                cur = max(opt[-1] + i, i)
            opt.append(cur)
            if cur > sol:
                sol = cur
        return sol
