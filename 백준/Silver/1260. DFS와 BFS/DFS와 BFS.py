# INPUT
import sys
input = sys.stdin.readline
N, M, V = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().rstrip().split())
    graph[i].append(j)
    graph[j].append(i)

# Solution
from collections import deque

visited = [0 for _ in range(N+1)]
def dfs(graph, start, visited):
    
    if not visited[start]:
        print(start, end=' ')
        visited[start] = 1
        
        for v in graph[start]:
            dfs(graph, v, visited)
    
def bfs(graph, start, n):
    visited = [0 for _ in range(n+1)]
    q = deque([start])
    visited[start] = 1
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        for nv in graph[v]:
            if visited[nv]:
                continue
            q.append(nv)
            visited[nv] = 1

# OUTPUT
for i in range(1, N+1):
    graph[i].sort()
    
dfs(graph, V, visited)
print()
bfs(graph, V, N)