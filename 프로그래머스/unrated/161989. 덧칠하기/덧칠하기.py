from collections import deque

def solution(n, m, section):
    section = deque(section)
    res = 1
    t = section.popleft() + m
    
    while section:
        s = section.popleft()
        if s >= t:
            res += 1
            t = s + m
    
    return res