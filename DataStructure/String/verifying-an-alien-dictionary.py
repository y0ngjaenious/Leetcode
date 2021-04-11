# question link: https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def compare(self, word1: str, word2: str, order: dict) -> bool:
        # word1 < word2
        l1 = len(word1)
        l2 = len(word2)
        for i in range(min(l1, l2)):
            if order[word1[i]] > order[word2[i]]:
                return False
            elif order[word1[i]] < order[word2[i]]:
                return True
        return l1 <= l2
            
        return True
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dic = {}
        for i in range(len(order)):
            order_dic[order[i]] = i
        
        for i in range(len(words) - 1):
            if not self.compare(words[i], words[i + 1], order_dic):
                return False
        return True
        
