with open("p042_words.txt") as f:
    WORDS = f.read().replace("\"","").split(",")
    
def get_triangle_word_count():
    count = 0
    for word in WORDS:
        t = sum(ord(L)-64 for L in word)
        n = (-1+(1+8*t)**0.5)/2
        if int(n) == n:
            count += 1
    return count

print(get_triangle_word_count())