import sys
from collections import Counter
input = sys.stdin.readline

# SOLUTION
def solution(arr, N):
    
    avg = round(sum(arr)/N)
    print(avg)
    
    arr.sort()
    median = arr[N//2]
    print(median)

    arr_cnt = Counter(arr)
    most = []
    c = arr_cnt.most_common(1)[0][1]
    while True:
        k, v = arr_cnt.most_common(1)[0]
        if v < c:
            break
        arr_cnt[k] = 0
        most.append(k)
    most.sort()
    if len(most) > 1:
        print(most[1])
    else:
        print(most[0])

    print(arr[-1] - arr[0])

# INPUT
N = int(input())
arr = [int(input()) for _ in range(N)]
solution(arr, N)