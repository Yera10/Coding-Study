# INPUT
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# SOLUTION
arr.sort(key=lambda x:x[1])
arr.sort()

# OUTPUT
for x, y in arr:
    print(x, y)