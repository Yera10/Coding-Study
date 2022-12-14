# 프로그래머스 - 징검다리 건너기


문제 링크 : [링크](https://school.programmers.co.kr/learn/courses/30/lessons/64062)<br>


### **Input**
- 디딤돌에 적힌 숫자가 순서대로 담긴 배열 stones
- 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k
- 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
- 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
- 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다

### **Output**
- 최대 몇 명까지 징검다리를 건널 수 있는지 return

### **입력과 출력 예**
| stones | k | result |
|---|---|--------|
| [2, 4, 5, 3, 2, 1, 4, 2, 5, 1] | 3 | 3 |


### **나의 풀이 코드**
통과 (313.83ms, 18.6MB)
```python
def check(stones, k, mid):
    cnt = 0
    for stone in stones:
        if stone <= mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True

def binary_search(stones, k, s, e):
    while s <= e:
        mid = (s+e)//2
        if check(stones, k, mid):
            s = mid + 1
        else:
            e = mid - 1
    return s

def solution(stones, k):
    s = 1
    e = max(stones)
    
    return binary_search(stones, k, s, e)
```
- $O(?)$<br>
- 이게 왜 빠르지..? 
- 솔루션 보고 풀었다. 
- 이진탐색을 데이터를 탐색하는 데 쓴 것이 아닌 정답을 찾아가는 데 이진탐색을 썼다. 
- 정답이 mid보다 큰지 작은지 확인하고, s,e를 조정해가며 정답을 찾는 방법
- 함수
  - binary_search - 이진탐색 함수의 변형
  - check - mid명이 지나갈 수 있는지 확인하는 함수
- binary_search 에서 mid 값이 정답일때는 어떻게 되나 생각했는데,\
s = e 로 수렴하고, 마지막 loop에서 s + 1을 return 하게되면서 해결


### **더 빠른 풀이 코드**
통과 (19.82ms, 18.5MB)
```python
def solution(stones, k):
    cnt = 200000000
    pointer = 0
    change = 0
    while pointer < len(stones) - (k-1):
        pointer += stones[pointer:pointer+k].index(max(stones[pointer:pointer+k]))
        if cnt > stones[pointer]:
            cnt = stones[pointer]
            change+=1
        pointer += 1
        if change >= 15:
            break
    if change < 15:
        return cnt
    else:
        cnt = []
        pointer = 0
        while pointer < len(stones) - (k-1):
            cnt.append(max(stones[pointer:pointer+k]))
            pointer += k
        return min(cnt)
```
- $O(S \times k)$<br>
  - $S$ : stones의 길이
  - $k$ : input k
- 처음에 생각했던 방법과 비슷하지만, 효율성에서 통과하지 못했던 것
- 이 코드는 조금 더 불필요한 계산들을 쳐낸 듯
- 좀 더 공부해야 함!

----

# 이진탐색

## 이진탐색이 적용가능한 경우
- 단조증가 함수일때
- 한 점에서만 변하는 조건함수를 정의할 수 있을 때\
$g(x) = 
\begin{cases} 
0, \;(x<0)\\
1, \;(x\geq 0)
\end{cases}$
  
## 이진탐색 조건 설정하기
- low, high 불변의 법칙? 
- $g(low)=0$, $g(high)=1$ 를 항상 만족하도록 하면 됨. \
(반대일 경우라도)
- low, high 를 계속 수정해 나갈때에 위 조건을 만족하도록 low 또는 high를 수정하면 됨. 