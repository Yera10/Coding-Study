# 프로그래머스 - 숫자 짝꿍

문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131128
<br>

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)

### **Input**
- 두 정수 X, Y
- 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
- X, Y는 0으로 시작하지 않습니다.
- X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.


### **Output**
-  X, Y의 짝꿍을 return
 

### **입력과 출력 예**
| X | Y | result |
|---|---|--------|
| "100"	| "2345" | "-1" |
| "100"	| "203045" | "0" |
| "100" | "123450"	| "10" |
| "12321" | "42531"	| "321" |
| "5525" | "1255"	| "552" |



### **나의 풀이 코드**
(310.84ms, 27.7MB)
```python
from collections import Counter

def solution(X, Y):
    cntx = Counter(X)
    cnty = Counter(Y)
    dg_cnt = cntx & cnty
    
    res = ''
    for i in range(9, 0, -1):
        res += str(i)*dg_cnt[str(i)]
    
    if res:
        res += '0' * dg_cnt['0']
    
    elif dg_cnt['0']:
        res = '0'
    
    else:
        res = '-1'
    
    return res
```
- $O(N_x+N_y)$<br>
$N_x$ : X의 길이, $N_y$ : Y의 길이