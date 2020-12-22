question link: https://leetcode.com/problems/palindrome-number

## First Solution - Not that bad

"""
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        length = math.floor(math.log(x, 10))
        

        for i in range(length // 2 + 1):
            if i == length - i:
                continue
            j = length - i
            a = x % (10 ** (i + 1)) // (10 ** i)
            b = x % (10 ** (j + 1)) // (10 ** j)
            if a != b:
                return False
            
        return True
"""

## Second - faster, without math library

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
            
        return x == rev or x == rev // 10
