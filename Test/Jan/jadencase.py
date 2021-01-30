# question link: https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    first = True
    answer = ''
    for i in s:
        if i == " ":
            answer += i
            first = True
            continue
        if first:
            first = False
            if 97 <= ord(i) <= 122:
                answer += chr(ord(i) - 32)
            else:
                answer += i
        else:
            if 65 <= ord(i) <= 90:
                answer += chr(ord(i) + 32)
            else:
                answer += i
    return answer
