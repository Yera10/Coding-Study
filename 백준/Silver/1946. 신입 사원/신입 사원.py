# SOLUTION
def solution(N, arr):
    arr.sort()
    
    cnt = 0
    last = N+1
    
    for a, b in arr:
        if b < last:
            cnt += 1
            last = b
    
    return cnt

# INPUT
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, arr))
