# 프로그래머스 - 게임 맵 최단거리

문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844
<br>


### **Input**
- 게임 맵의 상태 maps가 매개변수로 주어짐
- maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열
- 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
- n과 m은 각각 1 이상 100 이하의 자연수
- n과 m은 서로 같을 수도, 다를 수도 있다.
- n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
- maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냄
- 

### **Output**
-  캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return
-  상대 팀 진영에 도착할 수 없을 때는 -1
 

### **입력과 출력 예**
| maps | answer |
|------|--------|
| [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] | 11 |
| [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] | -1 |


### **나의 풀이 코드**
통과 (23.92ms, 11.3MB)
```python
from collections import deque

def bfs(graph:list, start_node:tuple, n, m):
    visit = set()
    queue = deque()
    dist = deque()
    
    queue.append(start_node)
    dist.append(1)
    
    while queue:
        node = queue.popleft()
        d = dist.popleft()
        
        if node==(n-1, m-1):
            return d
        
        if node in visit:
            continue
        
        visit.add(node)
        for i,j in [(1,0), (0,1), (-1,0), (0,-1)]:
            next_node = (node[0]+i, node[1]+j)
            if 0<=next_node[0]<n and 0<=next_node[1]<m and graph[next_node[0]][next_node[1]]==1:
                queue.append(next_node)
                dist.append(d+1)

    return -1

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return bfs(maps, (0,0), n, m)
```
- 시간복잡도 : $O(n \times m)$ ($n, m$: graph 사이즈)