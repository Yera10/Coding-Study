# INPUT
susik = input()

# SOLUTION
from collections import deque
def solution(susik):
    susik = list(susik)
    nums = deque()
    oprs = deque()    

    while susik:
        n = ''
        while susik:
            x = susik.pop(0)
            if x!="+" and x!="-":
                n += x
            else:
                break        
        if susik:
            nums.append(int(n))
            oprs.append(x)
        else:
            nums.append(int(n))    
    
    res = nums.popleft()
    
    for i in range(len(nums)):
        n, o = nums.popleft(), oprs.popleft()
        if o == "+":
            res += n
        else:
            res -= n
            res -= sum(nums)
            break
    
    return res

    
# OUT
print(solution(susik))