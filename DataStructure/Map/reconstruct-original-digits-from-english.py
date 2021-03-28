# question link: http://leetcode.com/problems/reconstruct-original-digits-from-english

from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        answer = ""
        numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        order = ["zero", "six", "eight", "two", "seven", "five", "four", "three", "nine", "one"]
        dic = {v: str(i) for i, v in enumerate(numbers)}
        identifier = ["z", "x", "g", "w", "s", "v", "f", "h", "i", "o"]
        for o in range(len(order)):
            i = counter[identifier[o]]
            answer += dic[order[o]] * i
            counter -= {c: i for c in order[o]}
        print(answer)
        return "".join(sorted(answer))
