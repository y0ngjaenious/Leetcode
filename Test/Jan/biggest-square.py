# question link: https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    x = len(board)
    y = len(board[0])
    
    if x == 1 or y == 1:
        for i in range(x):
            for j in range(y):
                if board[i][j] == 1:
                    return 1
        return 0
    sol = 0
    for i in range(1, x):
        for j in range(1 , y):
            if board[i][j] > 0:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
                sol = max(sol, board[i][j])
            
    return sol ** 2
