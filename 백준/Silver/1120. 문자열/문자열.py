# INPUT
A, B = input().split()
len_a = len(A)
len_b = len(B)

# FUNCTIONS
def diff(w1, w2):
    return sum([i!=j for i,j in zip(w1, w2)])

# SOLUTIONS
res = 50
for i in range(len_b-len_a+1):
    d = diff(A, B[i:i+len_a])
    if d < res:
        res = d

# OUTPUT
print(res)