n = int(input())

cnts = [n//5, (n%5)//2, (n%5)%2]

if cnts[2] and cnts[0]:
    cnts[0] -= 1
    cnts[2] -= 1
    cnts[1] += 3

if cnts[2]:
    print(-1)
else:
    print(sum(cnts))