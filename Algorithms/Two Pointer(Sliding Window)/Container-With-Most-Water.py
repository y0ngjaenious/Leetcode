# question link: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        a = 0
        b = len(height) - 1
        maxArea = (b - a) * min(height[b], height[a])
        
        while b > a:
            flag = height[a] < height[b]
            a += flag
            b -= (1 - flag)
            
            curArea = (b - a) * min(height[b], height[a])
            
            maxArea = max(maxArea, curArea)
        
        return maxArea
