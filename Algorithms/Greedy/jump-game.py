# question link: https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        valid = 0
        for i in range(len(nums)):
            if valid >= len(nums) - 1:
                return True
            if valid < i:
                return False
            valid = max(valid, nums[i] + i)
            
        return True
