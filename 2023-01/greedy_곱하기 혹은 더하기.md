# 곱하기 혹은 더하기

### **Input**
- 각 자리가 숫자(0~9)로만 이루어진 문자열 S

### **Output**
- 모든 숫자 사이에 '$\times$' 혹은 '+' 연산자를 넣어 계산하여 결과적으로 만들어질 수 있는 가장 큰 수 
- 단, 모든 연산은 왼쪽부터 순서대로 이루어짐

### **입력과 출력 예**
| S | result |
|---|--------|
| 02984	| 576 |
| 567 | 210 |

### **나의 풀이 코드**
```python
def solution(S):
    res = int(S[0])
    for s in S[1:]:
        p = res + int(s)
        m = res * int(s)
        res = max(p, m)
    return res
```
- $O(N)$
  - $N$ : 문자열 S의 길이 
- 왼쪽부터 당장의 계산까지만 했을 때, 큰 계산을 선택하면 그게 최적의 선택이니까.
- 왜냐하면 a<b일때, x>=0 \
a + x < b + x\
a * x < b * x 이기 때문에, \
다음 계산까지 생각했을 때 계산 결과의 경우가 a+x, a\*x, b+x, b\*x 있다고 할때, 가장 큰 수는 b로 계산한 수이기 때문에 지금까지 계산이 큰 경우만 봐도 된다. 
  
### **더 빠른 풀이 코드**
```python
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
```
- $O(N)$<br>
- 덧셈이 곱셈보다 클 경우는 두 인자 중 하나가 0이거나 1일때 뿐이므로, 모두 계산하지 않고 그때만 계산하는 게 더 효율적