# 프로그래머스 - 불량 사용자

문제 링크 : [링크](https://school.programmers.co.kr/learn/courses/30/lessons/64064)<br>


### **Input**
- 이벤트 응모자 아이디 목록이 담긴 배열 user_id
- 불량 사용자 아이디 목록이 담긴 배열 banned_id
- banned_id에는 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달
- 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 아이디 당 최소 하나 이상의 '*' 문자를 사용

### **Output**
- 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return

### **입력과 출력 예**
| user_id | banned_id | result |
|---|---|--------|
| ["frodo", "fradi", "crodo", "abc123", "frodoc"]	 | ["fr*d*", "abc1**"]		| 2 |
| ["frodo", "fradi", "crodo", "abc123", "frodoc"]	 | ["*rodo", "*rodo", "******"]		| 2 |
| ["frodo", "fradi", "crodo", "abc123", "frodoc"]	 | ["fr*d*", "*rodo", "******", "******"]		| 3 |


### **나의 풀이 코드**
통과 (5367.86ms, 10.1MB)
```python
import re
from itertools import product

def solution(user_id, banned_id):
    ban_dict = [[u for u in user_id if re.fullmatch(b.replace('*', '.'), u)] for b in banned_id]
    
    res = []
    for ids in product(*ban_dict):
        if len(ids)==len(set(ids)) and set(ids) not in res:
            res.append(set(ids))
    
    return len(res)
```
- $O(?)$<br>
- 시간이 너무 오래걸린다. 다른 방법 구현해볼 필요가 있겠다.

### **더 빠른 풀이 코드**
통과 (57.41ms, 10.2MB)
```python
import re

def dfs(g, lv, visited = set(), res=list()):
    if not g[lv]:
        if visited not in res:
            res.append(visited)
    
    for next_node in g[lv]:
        if next_node not in visited:
            dfs(g, lv+1, visited.union({next_node}), res)
    
    res = len(res)
    return res

def solution(user_id, banned_id):
    ban_list = [[u for u in user_id if re.fullmatch(b.replace('*', '.'), u)] for b in banned_id]
    ban_list.append([])
    
    return dfs(ban_list, 0)
```
- $O(?)$<br>
- dfs로 구현
- 탐색 횟수는 똑같은 것 같은데, product를 쓰지 않아 더 빨라진 걸까? 