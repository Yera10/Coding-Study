# SOLUTION
def solution(arr):
    arr.sort(key=lambda x:x[0])
    arr.sort(key=lambda x:x[3], reverse=True)
    arr.sort(key=lambda x:x[2])
    arr.sort(key=lambda x:x[1], reverse=True)
    
# INPUT
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    name, a, b, c = input().split()
    arr.append([name, int(a), int(b), int(c)])
solution(arr)
for a in arr:
    print(a[0])