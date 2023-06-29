# INPUT
x = int(input())

# Solution
d = [0] * (x+1)

for i in range(2, x+1):
    dmin = d[i-1]

    if i%2==0:
        dmin = min(dmin, d[i//2])
    if i%3==0:
        dmin = min(dmin, d[i//3])
    
    d[i] = dmin + 1

# OUTPUT
print(d[x])