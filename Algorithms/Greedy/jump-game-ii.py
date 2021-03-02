# question link: https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, curEnd, curMax = 0, 0, 0
        for i in range(len(nums)):
            if curEnd >= len(nums) - 1:
                    break
            curMax = max(curMax, nums[i] + i)
            if i == curEnd:
                jumps += 1
                curEnd = curMax
                
        return jumps
