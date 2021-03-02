# question link: https://leetcode.com/problems/set-mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sol = 2 ** len(nums) - 1
        ret = [0, 0]
        for i in range(len(nums)):
            n = abs(nums[i])
            ret[1] ^= (i + 1) ^ n
            if nums[n -1] < 0:
                ret[0] = n
            else:
                nums[n - 1] *= -1
        ret[1] ^= ret[0]
        return ret
