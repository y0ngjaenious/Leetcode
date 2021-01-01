# question link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# ver1: with python itertools
"""
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        if len(digits) == 1:
            return [i for i in dic[int(digits[0])]]
        
        it = [dic[int(i)] for i in digits]
        
        return ["".join(k) for k in product(*it)]
"""

# ver2: with recursion
class Solution:
    def __init__(self):
        self.dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        if len(digits) == 1:
            return [i for i in self.dic[int(digits[0])]]
        
        prev = self.letterCombinations(digits[:-1])
        add = [i for i in self.dic[int(digits[-1])]]
        
        return [p + c for p in prev for c in add]
