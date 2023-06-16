# SOLUTION
def binary_search(arr, t, s, e):
    if s > e:
        return -1

    m = (s+e)//2

    if arr[m] < t:
        return binary_search(arr, t, m+1, e)
    elif arr[m] > t:
        return binary_search(arr, t, s, m-1)
    else:
        return m


def solution(arr, targets, N):
    arr.sort()

    for t in targets:
        if binary_search(arr, t, 0, N-1)!=-1:
            print(1)
        else:
            print(0)



# TEST

# INPUT
import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
targets = list(map(int, input().rstrip().split()))

solution(arr, targets, N)
