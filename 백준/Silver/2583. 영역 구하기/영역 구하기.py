# INPUT
import sys
input = sys.stdin.readline
M, N, K = map(int, input().rstrip().split())
rtgs = [list(map(int, input().rstrip().split())) for _ in range(K)]


# SOLUTION
from collections import deque

def bfs(graph, start, n, m):
    q = deque([start])
    graph[start[1]][start[0]] = 0
    nv = [[1,0], [0,1], [-1,0], [0,-1]]
    N = 0
    while q:
        x, y = q.popleft()
        N += 1
        for dx, dy in nv:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0<= ny < m and graph[ny][nx] == 1:
                q.append([nx, ny])
                graph[ny][nx] = 0
    return N

def solution(n, m, rtgs):
    graph = [[1 for _ in range(n)] for _ in range(m)]
    for lx, ly, rx, ry in rtgs:
        for i in range(ly, ry):
            graph[i][lx:rx] = [0]*(rx-lx)
    
    N = 0
    areas = []
    
    for y in range(m):
        for x in range(n):
            if graph[y][x] == 1:
                areas.append(bfs(graph, [x, y], n, m))
                N += 1
    
    areas.sort()
    
    print(N)
    for a in areas:
        print(a, end=' ')

# OUTPUT
solution(N, M, rtgs)