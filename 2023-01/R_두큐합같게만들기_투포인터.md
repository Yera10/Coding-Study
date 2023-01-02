# 프로그래머스 - 두 큐 합 같게 만들기

문제 링크 : [링크](https://school.programmers.co.kr/learn/courses/30/lessons/118667)<br>


### **Input**
- 길이가 같은 두 개의 큐

### **Output**
- 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 한다.
- 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주할 때, 필요한 작업의 최소 횟수 return 

### **입력과 출력 예**
| queue1 | queue2 | result |
|---|---|--------|
| [3, 2, 7, 2] | [4, 6, 5, 1] | 2 |
| [1, 2, 1, 2] | [1, 10, 1, 2] | 7 |
| [1, 1] | [1, 5] | -1 |


### **나의 풀이 코드**
통과 (200.29ms, 42.3MB)
```python
from collections import deque 

def solution(queue1, queue2): 
    # Variables
    l = len(queue1) 
    S = sum(queue1) + sum(queue2)
    hS = S//2
    # 실패 미리 판별
    if S%2==1: return -1
    
    q = queue1 + queue2
    s,e = 0, 0
    qs = q[0]
    res = -1
    while s>=0 and e<2*l:
        if qs < hS:
            if e == (2*l-1): return -1
            e += 1
            qs += q[e]
        elif qs > hS:
            qs -= q[s]
            s += 1
        elif e >= (l-1):
            res = s + (e-(l-1))
            break
        else:
            res = e+1 + l + s 
            break
    
    q = queue2 + queue1
    s,e = 0, 0
    qs = q[0]
    while s>=0 and e<2*l:
        if qs < hS:
            if e == (2*l-1): return -1
            e += 1
            qs += q[e]
        elif qs > hS:
            qs -= q[s]
            s += 1
        elif e >= (l-1):
            if res > (s + (e-(l-1))):
                return s + (e-(l-1))
            else:
                return res
        else:
            if res > (e+1 + l + s):
                return (e+1 + l + s)
            else:
                return res
    
    return -1
```
- $O(N)$\
  - $N$ : queue의 길이<br>
- 문제 내용을 구현하려고 했지만, 그게 결국 투포인터로 푸는 것과 같았다. 
- 일단 testcase를 통과하려고 비효율적으로 푼 것 같은데, 조금 더 고칠 필요가 있을 것 같다. 
- 투포인터와 greedy도 공부해야겠다. 
  
### **더 빠른 풀이 코드**
통과 (소요시간, 소모메모리)
```python
solution_code
```
- $O(시간복잡도)$<br>
- 설명 및 느낀점, 알게된 것