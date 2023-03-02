# INPUT
N = int(input())
words = [input() for _ in range(N)]
words_by_len = [[] for _ in range(51)]

# FUNCTIONS
def is_same(word1, word2):
    if word1 in word2*2:
        return True
    return False

def is_in(word, word_list):
    for w in word_list:
        if is_same(word, w):
            return True
    return False

# SOLUTIONS
for word in words:
    l = len(word)
    
    if is_in(word, words_by_len[l]):
        continue
    else:
        words_by_len[l].append(word)

# OUTPUT
print(sum([len(l) for l in words_by_len]))