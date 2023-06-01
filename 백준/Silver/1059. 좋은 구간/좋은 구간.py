# SOLUTION
def solution(S, n):
    a, b = 0, 1001

    for s in S:
        if a < s < n:
            a = s
        elif n < s < b:
            b = s
        elif s == n:
            return 0

    return (n-a) * (b-n) -1

# INPUT
L = input()
S = map(int, input().split())
n = int(input())

print(solution(S, n))