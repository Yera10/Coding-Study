n = int(input())

def solution(x1, y1, r1, x2, y2, r2):
    d = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
    n1 = r1 + r2
    n2 = abs(r1 - r2)

    if(d == 0) :
        if(n2 == 0) :
            r = -1
        else :
            r = 0

    elif (d == n1 or d == n2):
        r = 1

    elif (n2 < d and d < n1) :
        r = 2

    else: 
        r = 0
    return r


for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solution(x1, y1, r1, x2, y2, r2))