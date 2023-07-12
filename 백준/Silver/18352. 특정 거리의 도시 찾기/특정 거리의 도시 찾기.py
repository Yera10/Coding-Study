# INPUT
import sys
input = sys.stdin.readline
N, M, K, Start = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    f, t = map(int, input().rstrip().split())
    graph[f].append(t)

# SOLUTION
import heapq
INF = int(1e9)

def get_nearest_node(distance_heap, visited):
    _, node = heapq.heappop(distance_heap)
    while visited[node]:
        _, node = heapq.heappop(distance_heap)

    return node

def dijkstra(g, start, N):
    distance = [INF] * (N+1)
    distance[start] = 0
    visited = [False] * (N+1)
    distance_heap = [(0,start)]

    while distance_heap:
        now = get_nearest_node(distance_heap, visited)
        visited[now] = True

        for nx in g[now]:
            if distance[nx] > distance[now]+1:
                distance[nx] = distance[now]+1
                heapq.heappush(distance_heap, (distance[nx], nx))
    
    return distance

# OUTPUT
distance = dijkstra(graph, Start, N)
res = [i for i,d in enumerate(distance) if d==K]
if res:
    for r in res:
        print(r)
else:
    print(-1)