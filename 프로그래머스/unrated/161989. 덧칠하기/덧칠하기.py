def solution(n, m, section):
    res = 1
    t = section.pop(0) + m
    
    while section:
        s = section.pop(0)
        if s >= t:
            res += 1
            t = s + m
    
    return res