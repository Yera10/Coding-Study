N, K = map(int, input().split())

import math
bottles = []
for _ in range(K):
    b = 2**int(math.log2(N))
    bottles.append(b)
    N -= b
    if N==0:
        N = bottles[-1]
        break
print(bottles[-1] - N)