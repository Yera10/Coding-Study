# INPUT
N, L = map(int, input().split())

# SOL
def solution(N, L):
    l = L

    while l<=100:
        if (2*N + l - l**2) % (2*l) == 0:
            s = (2*N + l - l**2) // (2*l)
            if s >= 0:
                for i in range(l):
                    print(s+i, end=' ')
                return
        l += 1

    print(-1)

# OUTPUT
solution(N, L)
