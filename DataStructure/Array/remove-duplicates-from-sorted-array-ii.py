# question link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        idx = -1
        l = len(nums)
        for i in nums:
            if dic[i] >= 2:
                l -= 1
            else:
                idx += 1
                nums[idx] = i
                dic[i] += 1
                
        return l
