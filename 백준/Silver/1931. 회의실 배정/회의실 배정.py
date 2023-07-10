# INPUT
import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

# SOLUTION
def solution(N, arr):
    arr.sort(key=lambda x:x[0])
    arr.sort(key=lambda x:x[1])
    
    N = 0
    max_e = 0
    
    for s,e in arr:
        if s >= max_e:
            N += 1
            max_e = e
                
    print(N)

# OUTPUT
solution(N, arr)