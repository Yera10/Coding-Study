# 프로그래머스 - 귤 고르기

문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/138476
<br>


### **Input**
- 경화가 한 상자에 담으려는 귤의 개수 k
- 귤의 크기를 담은 배열 tangerine
- 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
- 1 ≤ tangerine의 원소 ≤ 10,000,000

### **Output**
- 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return

### **입력과 출력 예**
| k | tangerine | result |
|---|---|--------|
| 6 | [1, 3, 2, 5, 4, 5, 2, 3]	| 3 |
| 4 | [1, 3, 2, 5, 4, 5, 2, 3]	| 2 |
| 2 | [1, 1, 1, 1, 2, 2, 2, 3]	| 1 |



### **나의 풀이 코드**
통과 (145.04ms, 25.7MB)
```python
from collections import Counter
import heapq

def solution(k, tangerine):
    cnt = Counter(tangerine)
    cnt = [(-v, k) for k,v in cnt.items()]
    heapq.heapify(cnt)
    
    res = 0
    
    while k>0:
        n, s = heapq.heappop(cnt)
        k += n
        res += 1
    
    return res
```
- $O(N + log_2M)$<br>
$N$ : tangerine의 길이, $M$ : cnt의 길이
  - M은 항상 N보다 작으니 $O(N)$이라고 해야하나? 
  - M이 최대일 경우, N과 같아질 수 있지만, <br>$O(N + log_2N) = O(N)$ 이니까 $O(N)$ 인가? 
- 처음에 Counter의 most_common을 사용했는데, 시간초과로 통과하지 못했다. Counter의 most_common 함수는 heap보다 시간복잡도가 큰 알고리즘을 사용하나보다. 
  
### **더 빠른 풀이 코드**
통과 (21.72ms, 21.7MB)
```python
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
```
- $O(NlogN)$
- python의 sorted는 병합정렬을 사용해 $O(NlogN)$의 복잡도를 가진다고 한다. 
- key를 몰라도 되기 때문에 list의 sort를 사용했다. 
- 시간복잡도로는 더 복잡한데, 훨씬 더 빠른 이유가 뭔지 모르겠다. 
- key를 사용하지 않는 list라는 데서 장점이 큰가? 