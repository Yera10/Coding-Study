# SOL
def solution(n):
    if n==0:
        return '1 0'
    
    d = [0, 1] + [-1]*(n-1)

    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    
    return str(d[n-1]) + ' ' + str(d[n])
    

# INPUT
T = int(input())
for _ in range(T):
    N = int(input())
    print(solution(N))
