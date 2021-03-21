# question link: https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        up = 1
        down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
                down = down
            elif nums[i] < nums[i - 1]:
                down = up + 1
                up = up
            
        return max(up, down)
