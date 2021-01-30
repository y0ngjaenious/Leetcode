# question link: https://leetcode.com/problems/trapping-rain-water/

## stack ver.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        sol = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                dist = i - stack[-1] - 1
                bound = min(height[i], height[stack[-1]]) - height[top]
                sol += dist * bound
            stack.append(i)
        return sol
"""

## two pointer ver.

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        sol = 0
        while left <= right:
            if l_max < r_max:
                if l_max < height[left]:
                    l_max = height[left]
                else:
                    sol += l_max - height[left]
                left += 1
            else:
                if r_max < height[right]:
                    r_max = height[right]
                else:
                    sol += r_max - height[right]
                right -= 1
        return sol
