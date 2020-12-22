# question link: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        _a = 100000
        for i in range(len(nums)):
            a = nums.pop(0)
            if a == _a:
                continue
            dic = {}
            donot = {}
            for k in nums:
                if (-a - k) not in dic:
                    dic[k] = 1
                elif k not in donot:
                    result.append([a, k, -a -k])
                    dic.pop(-a - k)
                    donot[-a - k] = 1
                    donot[k] = 1
            _a = a
        return result
