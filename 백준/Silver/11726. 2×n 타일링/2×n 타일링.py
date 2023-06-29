# INPUT
N = int(input())

# SOL
def solution(n):    
    d = [1, 2] + [0]*(n-2)

    for i in range(2, n):
        d[i] = (d[i-1] + d[i-2]) % 10007
    
    return d[n-1]
    
# OUTPUT
print(solution(N))
