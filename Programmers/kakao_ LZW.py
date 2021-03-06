# question link: https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {}
    cnt = 0
    for i in abc:
        cnt += 1
        dic[i] = cnt
    while msg:
        m = ""
        for i in range(len(msg)):
            if m + msg[i] not in dic:
                answer.append(dic[m])
                cnt += 1
                dic[m + msg[i]] = cnt
                msg = msg[i:]
                m = ""
                break
            else:
                m = m + msg[i]
        if m:
            answer.append(dic[m])
            break
    return answer
