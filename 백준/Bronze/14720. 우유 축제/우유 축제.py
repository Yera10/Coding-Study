_ = input()
milks = map(int, input().split())

t = 0
res = 0
for m in milks:
    if m==t:
        res += 1
        t = (t+1)%3

print(res)