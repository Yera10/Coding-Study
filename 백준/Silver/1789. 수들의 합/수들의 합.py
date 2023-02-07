S = int(input())

r = (2*S)**0.5
if r==int(r):
    print(int(r)-1)
elif int(r)*(int(r)+1)/2 <= S:
    print(int(r))
else:
    print(int(r)-1)