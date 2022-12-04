# 프로그래머스 - 쿼드압축 후 개수 세기

문제 링크 : [링크](https://school.programmers.co.kr/learn/courses/30/lessons/68936)<br>


### **Input**
- 0과 1로 이루어진 $2^n$ x $2^n$ 크기의 2차원 정수 배열 arr
- 이 arr을 쿼드 트리와 같은 방식으로 압축

압축방법
1. 당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
2. 만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
3. 그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.

<img src=".\image\쿼드압축.png" height='200x'><br>

### **Output**
- 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return

### **입력과 출력 예**
| arr | result |
|---|--------|
| [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	 | [4,9] |
| [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]	 | [10,15] |


### **나의 풀이 코드**
통과 (525.42ms, 40.4MB)
```python
from collections import Counter

# SOLUTION
def nemo_merge(x):
    l = len(x)
    for i in range(l//2):
        for j in range(l//2):
            nemo = x[i].pop(j) + x[i].pop(j) + x[i+1].pop(0) + x[i+1].pop(0)
            nemo = [sum(nemo[::2]), sum(nemo[1::2])]
            if nemo == [4, 0]: nemo = [1, 0]
            elif nemo == [0, 4]: nemo = [0, 1]
            x[i].insert(j, nemo)
        x.pop(i+1)
        
    if len(x)==1:
        return x[0][0]
    else:
        return nemo_merge(x)
            

def solution(arr):
    l = len(arr)
    res = []
    
    for i in range(l//2):
        row = []
        for j in range(l//2):
            nemo = arr[2*i][2*j:2*j+2] + arr[2*i+1][2*j:2*j+2]
            nemo_cnt = [0, 0]
            for n in nemo:
                nemo_cnt[n] += 1
            if nemo_cnt == [4, 0]: nemo_cnt = [1, 0]
            elif nemo_cnt == [0, 4]: nemo_cnt = [0, 1]
            row.append(nemo_cnt)
        res.append(row)
    
    return nemo_merge(res)
```
- $O(N^2)$<br>
  - $N$ : arr의 행의 개수 ( $=2^n$ )
  - 시간복잡도 이거 맞아???? 
  - 일단 내가 계산한 방법은\
$N^2 + (N/2)^2 + (N/4)^2 + \dots + (N/N)^2$\
$=\large \sum_{k=0}^{n} \dfrac{N^2}{(2^k)^2}$\
$=\sum_{k=0}^n \dfrac{N^2}{4^k}$\
$=\dfrac {N^2 \times \bigg(1-\dfrac{1}{4^{n+1}}\bigg)}{1-\dfrac{1}{4}}$\
$=\dfrac{4}{3} \times N^2 \times \bigg(1-\dfrac{1}{4^{n+1}}\bigg)$\
$=\dfrac{N^2}{3} \times \bigg(4-\dfrac{1}{4^{n}}\bigg)$\
$=\dfrac{N^2}{3} \times \bigg(4-\dfrac{1}{N^2}\bigg)$\
$=\dfrac{1}{3} \times (4N^2-1)\, = \, \dfrac{4N^2-1}{3}$\
$\Rightarrow O(N^2)$
  - 누구라도 내가 잘못 계산했다면 알려주면 좋겠다..
- 처음에는 문제 설명처럼 \
큰 네모 탐색 => 같지 않으면 4개로 쪼개기 => 다음으로 작은 네모 탐색 => 같지 않으면 4개로 쪼개기 ...\
같은 순서로 생각했는데, 그러면 탐색했던 부분을 또 탐색하는 낭비가 많이 발생하고, 시간복잡도가 $O(log_2N\times N^2)$가 된다.\
너무너무 낭비인 것 같아서 작은 네모부터 탐색해서 합쳐가는 방식으로 바꿨는데, 나아진 게 없는 건가..? 

