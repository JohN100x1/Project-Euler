with open("problem042_words.txt") as f:
    WORDS = f.read().replace("\"","").split(",")
    
def count_triangle_words():
    count = 0
    for word in WORDS:
        t = sum(ord(L)-64 for L in word)
        n = (-1+(1+8*t)**0.5)/2
        if int(n) == n:
            count += 1
    return count
            
print(count_triangle_words())