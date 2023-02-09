a, b = input().split()

mini = int(a.replace('6', '5')) + int(b.replace('6', '5'))
maxi = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(mini, maxi)