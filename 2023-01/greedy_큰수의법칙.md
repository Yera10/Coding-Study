# 큰 수의 법칙

### Input
- N : 2 $\leq$ N $\leq$ 1,000, 배열의 크기
- M : 1 $\leq$ M $\leq$ 10,000, 숫자가 더해지는 횟수
- K : 1 $\leq$ K $\leq$ 10,000, 특정 인덱스의 수가 연속해서 더해질 수 있는 횟수

### 큰 수의 법칙
- 배열의 숫자들을 M 번 더하여 가장 큰 수를 만드는 법칙
- 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다. 

### Output
- 큰 수의 법칙에 따른 결과

### Example
| N | M | K | array | result |
|---|---|---|-------|--------|
| 5 | 8 | 3 |2 4 5 4 6 | 46 |
| 5 | 7 | 2 |3 4 3 4 3 | 28 |

### **나의 풀이 코드**
```python
def solution(N, M, K, arr):
    m1 = max(arr)
    arr.remove(m1)
    m2 = max(arr)
    
    res = (M//(K+1)) * (K * m1 + m2) + sum(([m1] * K + [m2])[:M%(K+1)])
    return res
```
- python의 max 시간 복잡도 : $O(n)$
- python의 sort 시간 복잡도 : $O(n log n)$

### **더 좋은 풀이 코드**
```python
def solution(N, M, K, arr):
    m1 = max(arr)
    arr.remove(m1)
    m2 = max(arr)
    
    res = (M//(K+1)) * (K * m1 + m2) + (M%(K+1)) * m1
    return res
```

- 이게 greedy..?