# 프로그래머스 - 할인 행사

문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131127
<br>


### **Input**
- want : 원하는 제품을 나타내는 문자열 배열 
- number : 원하는 제품의 수량을 나타내는 정수 배열
- discount : 마트에서 할인하는 제품을 나타내는 문자열 배열
- want의 길이 = number의 길이 
- number의 원소의 합은 10


### **Output**
- 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여
- 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다. 
- 할인하는 제품은 하루에 하나씩만 구매 가능
- 회원등록시 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 
- 가능한 날이 없으면 0을 return
 

### **입력과 출력 예**
| want | number | discount | result |
|---|---|---|--------|
| ["banana", "apple", "rice", "pork", "pot"] | [3, 2, 2, 2, 1] | ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"] | 3 |
| ["apple"]	| [10] | ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"] | 0 |


### **나의 풀이 코드**
통과 (65.11ms, 17.2MB)
```python
from collections import Counter

def same_cnt(x, y):
    """같은 Counter인지 확인하는 함수"""
    for k,v in x.items():
        if y[k]!=v:
            return False
    return True

def solution(want, number, discount):
    # 원하는 품목 Counter
    wants = Counter()
    for w,n in zip(want, number):
        wants[w] = n
    
    # 원하는 품목과 일치하는 날짜 수 계산
    res = 0
    tendays = Counter(discount[:10])
    if wants==tendays:
        res += 1
    for i in range(len(discount)-10):
        tendays[discount[i]] -= 1
        tendays[discount[10+i]] += 1
        if same_cnt(wants, tendays):
            res += 1
    return res
```
- $O(N)$<br>
$N$ : discount의 길이 