N = int(input())
A = list(map(int, input().split()))

Aidx = list(range(N))
Aidx.sort(key=lambda x: A[x])

P = list(range(N))
P.sort(key=lambda x:Aidx[x])

print(" ".join(map(str, P)))