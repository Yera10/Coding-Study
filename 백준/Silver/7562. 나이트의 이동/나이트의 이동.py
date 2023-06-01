# SOLUTION
from collections import deque
dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
dys = [-1, 1, -2, 2, -2, 2, -1, 1]

def solution(I, start, target):
    board = [[0 for _ in range(I)] for _ in range(I)]
    board[start[0]][start[1]] = 1
    q = deque([start])
    qs = deque([0])
    
    while q:
        x, y = q.popleft()
        step = qs.popleft()
        
        if x==target[0] and y==target[1]:
            return step
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy 
            if 0<=nx<I and 0<=ny<I and (not board[nx][ny]):
                q.append([nx, ny])
                qs.append(step+1)
                board[nx][ny] = 1

# INPUT
T = int(input())
for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    print(solution(I, start, target))