# INPUT
N = int(input())
waits = [int(x) for x in input().split()]
waits.sort(reverse=True)

s = 0
for a,w in zip(range(1, len(waits) + 1), waits):
    s += a*w

# OUTPUT
print(s)