# INPUT
C = int(input())
cases = []
for _ in range(C):
    cases.append(list(map(int, input().split())))

# SOLUTION
def solution(case):
    avg = sum(case[1:]) / case[0]
    pct = sum([c>avg for c in case[1:]]) / case[0] * 100
    return f'{pct:.3f}%'

# OUT
for c in cases:
    print(solution(c))