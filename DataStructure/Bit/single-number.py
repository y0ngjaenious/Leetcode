# question link : https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = 0
        for i in nums:
            sol ^= i
        return sol
