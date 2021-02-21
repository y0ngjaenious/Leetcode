# question link: https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        idx = -1
        l = len(nums)
        for n in nums:
            if n == prev:
                l -= 1
            else:
                idx += 1
                nums[idx] = n
                prev = n
        return l 
