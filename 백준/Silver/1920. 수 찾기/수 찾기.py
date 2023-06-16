# SOLUTION
def solution(arr, targets, N):
    arr = set(arr)
    for t in targets:
        print(1 if t in arr else 0)



# TEST

# INPUT
import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
targets = list(map(int, input().rstrip().split()))

solution(arr, targets, N)
