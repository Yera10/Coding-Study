a, b, n = map(int, input().split())

x = (a % b)*10

for _ in range(int(n)):
    q = x//b
    x = x % b * 10

print(q)