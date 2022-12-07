# 프로그래머스 - 삼각 달팽이

문제 링크 : [링크](https://school.programmers.co.kr/learn/courses/30/lessons/68645)<br>


### **Input**

### **Output**

### **입력과 출력 예**
| intput1 | intput2 | result |
|---|---|--------|
| value | value	| result_value |


### **나의 풀이 코드**
통과 (170.89ms, 42MB)
```python
def solution(n):
    tri = [[] for _ in range(n)]
    num = 1
    
    # 삼각달팽이 만들기
    for k in range(n):
        # 왼변
        if k%3==0:
            for i in range(2*k//3, n-k//3):
                tri[i].insert(k//3, num)
                num += 1
        # 아랫변
        if k%3==1:
            for j in range(1+k//3, n-2*k//3):
                tri[n-1-k//3].insert(j, num)
                num += 1
        # 오른변
        if k%3==2:
            for i in range(n-1-1-k//3, k//3*2, -1):
                tri[i].insert(1+k//3, num)
                num += 1
    
    # 삼각달팽이 펼치기
    res = []
    for t in tri:
        res.extend(t)
    
    return res
```
- $O(n^2)$<br>\
$\dfrac{n(1+n)}{2} \times 2 + n$ 
- 그냥 문제 설명을 코드로 옮기니까 됐다. 
- 경우를 나누는 것, 반복 수행을 일반화 하는 게 관건이었던 것 같다. 