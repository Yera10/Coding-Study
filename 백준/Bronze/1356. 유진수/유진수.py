# INPUT
N = input()

# FUNCTIONS
def product(N:str):
    res = 1
    for n in N:
        res *= int(n)
    return res

# SOLUTION
def solution(N):
    
    if len(N)==1:
        return "NO"
    
    a = int(N[0])
    b = product(N[1:])
    if a == b:
        return "YES"
    
    for i in range(1, len(N)-1):
        a *= int(N[i])
        if N[i]!="0":
            b //= int(N[i])
        else:
            b = product(N[i+1:])
        if a == b:
            return "YES"
    
    return "NO"
    
# OUTPUT
print(solution(N))