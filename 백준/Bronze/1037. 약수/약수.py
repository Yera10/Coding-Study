N = int(input())
divisors = [int(x) for x in input().split()]
divisors.sort()

if N%2==1:
    res = divisors[len(divisors)//2]**2
else:
    res = divisors[0] * divisors[-1]

print(res)