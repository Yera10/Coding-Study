def solution(word):
    res = ""
    
    for i in range(2):
        w = word[:-2+i]
        mi, mw = 0, w[0]
        for i, c in enumerate(w):
            if w[i::-1] < mw:
                mi, mw = i, w[i::-1]
        res += mw
        word = word[mi+1:]
    
    res += word[::-1]

    return res

word = input()
print(solution(word))