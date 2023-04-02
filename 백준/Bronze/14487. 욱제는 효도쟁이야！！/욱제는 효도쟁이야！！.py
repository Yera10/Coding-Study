_ = input()
data = list(map(int, input().split()))

res = sum(data) - max(data)

print(res)