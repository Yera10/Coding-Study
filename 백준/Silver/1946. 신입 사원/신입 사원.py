# SOLUTION
def solution(N, arr):
    rank_arr = [0 for _ in range(N+1)]
    
    for a in arr:
        rank_arr[a[0]] = a[1]
    
    cnt = 0
    last = N+1
    
    for r in rank_arr[1:]:
        if r < last:
            cnt += 1
            last = r
    
    return cnt

# INPUT
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, arr))
