# SOLUTION
def rolling_right(dice):
    return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

def rolling_left(dice):
    return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

def rolling_up(dice):
    return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

def rolling_down(dice):
    return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

def solution(maps, moves, x, y, N, M):
    dice = ["0" for _ in range(6)]
    
    for m in moves:
        
        # 동쪽 이동
        if m == "1" and y < (M-1):
            dice = rolling_right(dice)
            y += 1
            
        # 서쪽 이동
        elif m == "2" and y > 0:
            dice = rolling_left(dice)
            y -= 1
        
        # 북쪽 이동
        elif m == "3" and x > 0:
            dice = rolling_up(dice)
            x -= 1
        
        # 남쪽 이동
        elif m == "4" and x < (N-1):
            dice = rolling_down(dice)
            x += 1
        
        else:
            continue
        
        print(dice[0])
        
        if maps[x][y] == "0":
            maps[x][y] = dice[-1]
        else:
            dice[-1], maps[x][y] = maps[x][y], "0"

N, M, x, y, k = map(int, input().split())
maps = [input().split() for _ in range(N)]
moves = input().split()
solution(maps, moves, x, y, N, M)