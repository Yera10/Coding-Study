# INPUT
N = int(input())
M = int(input())

# SOL
def solution(n, m):
    d = [[1]*(m+1)] + [[0]*(m+1) for _ in range(n-1)]

    for i in range(1, n):
        for j in range(m+1):
            d[i][j] = d[i-1][j] + (d[i][j-1] if j!=0 else 0)
    
    return d[n-1][m]

    
# OUTPUT
print(solution(N, M-N))
