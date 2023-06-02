# SOLUTION
def solution(alist, blist):
    aset = set(alist)
    bset = set(blist)
    
    res = list(aset.intersection(bset))
    res.sort()
    
    return res

# INPUT
N, M = map(int, input().split())
alist = [input() for _ in range(N)]
blist = [input() for _ in range(M)]

# OUTPUT
res = solution(alist, blist)
print(len(res))
for n in res:
    print(n)