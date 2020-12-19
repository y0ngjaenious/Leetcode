# question link: https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findKth(self, nums1, nums2, k):
        n, m = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        
        while idx1 + idx2 < k - 1:
            step = (k - idx1 - idx2) // 2
            cand1 = idx1 + step
            cand2 = idx2 + step
            if (n > cand1 - 1) and (m <= cand2 - 1 or nums1[cand1 - 1] < nums2[cand2 - 1]):
                idx1 = cand1
            else:
                idx2 = cand2
            
        if (n > idx1) and (m <= idx2 or nums1[idx1] < nums2[idx2]):
            return nums1[idx1]
        else:
            return nums2[idx2]
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M = len(nums1) + len(nums2)
        if M % 2 == 0:
            a = self.findKth(nums1, nums2, M // 2)
            b = self.findKth(nums1, nums2, M // 2 + 1)
            return (a + b) / 2
        else:
            return self.findKth(nums1, nums2, M // 2 + 1)
