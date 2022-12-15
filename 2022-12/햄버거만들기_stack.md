# 프로그래머스 - 햄버거 만들기

문제 링크 : [링크](https://school.programmers.co.kr/learn/courses/30/lessons/133502)<br>


### **Input**
- 재료의 정보를 나타내는 정수 배열 ingredient

### **Output**
- 상수가 포장하는 햄버거의 개수를 return

### **입력과 출력 예**
| ingredient | result |
|---|----------|
| [2, 1, 1, 2, 3, 1, 2, 3, 1] | 2 |
| [1, 3, 2, 1, 2, 1, 3, 1, 2] | 0 |


### **나의 풀이 코드**
통과 (7943.94ms, 18.5MB)
```python
def solution(ingredient):
    i = 0
    l = len(ingredient)
    res = 0
    
    while l>3 and i<l:
        if ingredient[i:i+4]==[1, 2, 3, 1]:
            for _ in range(4):
                ingredient.pop(i)
            res += 1
            l -= 4
            i -= 3
        else:
            i += 1
            
    return res
```
- $O(N + 8H)$<br>
  - N : ingredient의 길이
  - H : return 값, 만든 햄버거의 갯수
  - 사실상 $N+H$지만, 아래 코드와 비교하기 위해서 이렇게 표기했다. 
- 풀긴 풀었는데 너무 오래걸린다. 선형복잡도인 것 같은데 왜그런지 모르겠다. 
  
### **더 빠른 풀이 코드**
통과 (197.95ms, 26.7MB)
```python
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt

```
- $O(N+H)$<br>
- 내 코드는 리스트를 순서대로 탐색하기 때문에 햄버거를 하나 만들면, 다시 앞으로 돌아가서 재탐색을 해야했다. 
- 하지만, 이 코드는 stack을 이용해서 이 계산을 절약했다. 
- 그동안 코테 문제에서 stack을 제대로 써본 적이 없었는데 이런 경우에 쓰면 좋을 수 있겠구나 라고 깨달았다. 
