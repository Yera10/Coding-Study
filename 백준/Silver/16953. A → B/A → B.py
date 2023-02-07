x, y = map(int, input().split())

cnt = 0
while y > x:
    if y%2 == 0:
        y //= 2
    elif y%10 == 1:
        y -= 1
        y //= 10
    else:
        break
    cnt += 1

if y == x:
    print(cnt + 1)
else:
    print(-1)