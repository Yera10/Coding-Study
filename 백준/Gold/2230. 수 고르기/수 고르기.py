# SOLUTION
def solution(arr, N, M):
    if N==1 or M==0:
        return 0

    arr.sort()
    s, e = 0, 0
    min_diff = arr[-1] - arr[0]

    while e < N-1:
        diff = arr[e] - arr[s]

        while diff < M:
            if e == N-1:
                return min_diff
            e += 1
            diff = arr[e] - arr[s]
        
        while diff >= M:
            s += 1
            diff = arr[e] - arr[s]
        
        s -= 1
        diff = arr[e] - arr[s]

        if diff < min_diff:
            min_diff = diff
            if min_diff == M:
                return min_diff
        
        s += 1
        diff = arr[e] - arr[s]

    
    return min_diff


# INPUT
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
print(solution(arr, N, M))