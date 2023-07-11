# 최단 경로

- 가장 짧은 경로를 찾는 알고리즘, <u>"길찾기" 문제</u>라고도 불림.
- 최단 경로 알고리즘 유형에도 다양한 종류가 있음. 
  - 예를 들어 '한 지점에서 다른 특정 지점까지의 최단 경로 구하기'
  - 또는 '모든 지점에서 다른 모든 지점까지의 최단 경로 구하기' 등..
- 최단 경로 문제는 <u>보통 그래프를 이용해 표현</u>하며, 그래프는 "노드"와 "간선"으로 구성된다. 

### 최단 거리 알고리즘
1. 다익스트라 최단 경로
2. 플로이드 워셜
3. 벨만 포드 알고리즘

(최단 거리 알고리즘은 그리디, 다이나믹 프로그래밍 알고리즘의 한 유형이다.)

### 다익스트라 최단 경로
- 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- '음의 간선'이 없을 때 정상적으로 동작됨\
('음의 간선': 0보다 작은 값을 가지는 간선)
- 현실세계의 길은 음의 간선으로 표현되지 않기 때문에 <u>실제로 GPS 소프트웨어 기본 알고리즘</u>으로 채택됨
- 그리디 알고리즘으로 분류

### 다익스트라 최단 경로의 순서
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3,4번을 반복

### 다익스트라 최단 경로 알고리즘의 특징
- 최단 경로를 구하는 과정에서 <u>'각 노드에 대한 현재까지의 최단 거리' 정보를 항상 1차원 리스트에 저장</u>하며 리스트를 계속 갱신
- 매번 현재 처리하고 있는 노드를 기준으로 주변 간선 확인
- 데이크스트라와 같은 알고리즘
- **방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택하는 과정을 반복**
  - 위 과정에서 선택된 노드는 '최단거리'가 완전히 선택된 노드이므로, 더 이상 알고리즘을 반복해도 최단 거리가 줄어들지 않는다.
  - \>\>한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음. 
  - \> 그렇기 때문에 사실 마지막 노드에 대해서는 해당 노드를 거쳐 다른 노드로 가는 경우를 확인할 필요가 없다. 

내가 짠 다익스트라 소스코드
```python
INF = int(1e9)

def Dijkstra(g, N, start):
    distance = [INF] * N
    distance[start] = 0
    not_visited = {i for i in range(N)}
    
    while not_visited:
        # 최단거리가 가장 짧은 노드 선택
        v = -1       
        min_d = INF
        for nv in not_visited:
            if distance[nv] < min_d:
                v = nv
                min_d = distance[nv]
        not_visited.remove(v)
        
        # 최단거리 테이블 갱신
        for i,d in enumerate(g[v]):
            if (d != -1) and (min_d + d < distance[i]):
                distance[i] = min_d + d
    
    return distance

# TEST
N = 6
g = [
    [0, 2, 5, 1, -1, -1],
    [-1, 0, 3, 2, -1, -1], 
    [-1, 3, 0, -1, -1, 5], 
    [-1, -1, 3, 0, 1, -1], 
    [-1, -1, 1, -1, 0, 2],
    [-1, -1, -1, -1, -1, 0]
]
start = 0
print(Dijkstra(g, N, start))
```

간단한 다익스트라 알고리즘 소스코드
```python
INF = int(1e9)

def get_smallest_node(N, visited, distance):
    """방문하지 않은 노드들 중 가장 가까운 노드 번호를 반환하는 함수"""
    min_d = INF
    idx = 0

    for i in range(N):
        if (not visited[i]) and (distance[i] < min_d):
            idx = i
            min_d = distance[i]

    return idx

def dijkstra(N, g, start):
    """다익스트라 알고리즘을 사용하여 start 노드로 부터 모든 노드로 최단 거리를 구하는 함수"""
    distance = [INF] * N
    visited = [0] * N
    distance[start] = 0
    visited[start] = 1

    for _ in range(N-1):
        now = get_smallest_node(N, visited, distance)
        visited[now] = 1
        
        for nv, nd in g[now]:
            if distance[nv] > distance[now] + nd:
                distance[nv] = distance[now] + nd
        
        print(distance)
        
    return distance

# TEST
N = 6
graph = [
    [[1, 2], [2, 5], [3, 1]],
    [[2, 3], [3, 2]], 
    [[1, 3], [5, 5]], 
    [[2, 3], [4, 1]], 
    [[2, 1], [5, 2]],
    []
]
start = 0
print(dijkstra(N, graph, start))
```
- 시간 복잡도는 $O(N^2)$, $N$은 노드의 개수
- 노드의 개수가 5,000개 이하라면 위 코드로 문제를 풀 수 있음. 
- 하지만, 10,000개를 넘어가면 위 코드로 해결하기 어려움

### 다익스트라 알고리즘 개선
- 시간 복잡도 $O(ElogN)$,\
$N$은 노드의 개수, $E$는 간선의 개수
- 최단 거리가 가장 짧은 노드를 찾을 때 (get_smallest_node함수를 사용할 때), 힙 자료구조를 사용하여 더 빠르게 개선시킨다. 

[힙 자료구조](./Heap.md)