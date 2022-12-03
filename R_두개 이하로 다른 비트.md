# 프로그래머스 - 숫자 짝꿍

문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77885
<br>

### **Input**
- numbers : 정수들이 담긴 배열


### **Output**
- numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return
- f(x) = x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
  
### example
- f(2) = 3 
- f(7) = 11


| 수 | 비트 | 다른 비트의 개수 |
|---|---|--------|
| 7	| 000...0111 |  |
| 8	| 000...1000 | 4 |
| 9 | 000...1001 | 3 |
| 10 | 000...1010 | 3 |
| 11 | 000...1011 | 2 |

### **입력과 출력 예**
| numbers | result |
|------|--------|
| [2,7]	 | [3,11] |



### **나의 풀이 코드**
통과 (298.56ms, 23.8MB)
```python
# 주어진 f함수 
def f(n):
    # 2진수로 변환
    nbin = bin(n)[2:]
    
    # 끝자리가 0일 경우, +1 return 
    if nbin[-1] == '0':
        return n+1
    
    # 중간에 "01"이 있을 경우, "10"으로 바꿔서 return 
    for i in range(len(nbin)-2, -1, -1):
        if nbin[i] == '0':
            res = nbin[:i]+'10'+nbin[i+2:]
            return int('0b'+res, 2)
    
    # 모두 1로 이루어져있을 경우, 1011... return 
    return int('0b10' + nbin[1:], 2)

def solution(numbers):
    answer = [f(n) for n in numbers]
    return answer
```
- $O(log_2n)$<br>
- n의 2진수 자리수만큼 탐색하므로 

### **좋은 풀이 코드**
통과 (25.02ms, 22.9MB)
```python
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer
```
- 아직 이거 이해 못한 상태