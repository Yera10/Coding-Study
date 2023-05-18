# FUNCTIONS
def reverse_updown(arr):
    return [a for a in arr[::-1]]

def reverse_leftright(arr):
    return [a[::-1] for a in arr]

def rotate_clockwise(arr, N, M):
    return [[arr[N-1-j][i] for j in range(N)] for i in range(M)]

def rotate_anticlockwise(arr, N, M):
    return [[arr[j][M-1-i] for j in range(N)] for i in range(M)]

def relocate5(arr, N, M):
    return [arr[N//2+i][:M//2] + arr[i][:M//2] for i in range(N//2)] + [arr[N//2+i][M//2:] + arr[i][M//2:] for i in range(N//2)]

def relocate6(arr, N, M):
    return [arr[i][M//2:] + arr[N//2+i][M//2:] for i in range(N//2)] + [arr[i][:M//2] + arr[N//2+i][:M//2] for i in range(N//2)]

# INPUT
N, M, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append( [i for i in input().split()] )
oprs = input().split()

# SOLUTION
for o in oprs:
    if o == "1":
        arr = reverse_updown(arr)
    if o == "2":
        arr = reverse_leftright(arr)
    if o == "3":
        arr = rotate_clockwise(arr, N, M)
        N, M = M, N
    if o == "4":
        arr = rotate_anticlockwise(arr, N, M)
        N, M = M, N
    if o == "5":
        arr = relocate5(arr, N, M)
    if o == "6":
        arr = relocate6(arr, N, M)
        
# OUTPUT
for a in arr:
    print(" ".join(a))