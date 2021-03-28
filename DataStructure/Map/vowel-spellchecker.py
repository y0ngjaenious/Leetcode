# question link: https://leetcode.com/problems/vowel-spellchecker/

from collections import defaultdict

def helper(string, idx, rep):
    return "".join((string[:idx],rep,string[idx+1:]))

def vowel_convert(string):
    for i in range(len(string)):
        if string[i] in set(["a", "e", "i", "o", "u"]):
            string = helper(string, i, "#")
    return string

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = {}
        cap = {}
        vow = {}
        answer = []
        
        for word in wordlist:
            exact[word] = word
            cap.setdefault(word.lower(), [])
            cap[word.lower()].append(word)
            v = vowel_convert(word.lower())
            vow.setdefault(v, [])
            vow[v].append(word)
        
        for q in queries:
            if q in exact:
                answer.append(q)
                continue
            elif q.lower() in cap:
                answer.append(cap[q.lower()][0])
                continue
            v = vowel_convert(q.lower())
            print(v)
            if v in vow:
                answer.append(vow[v][0])
            else:
                answer.append("")
        
        return answer
