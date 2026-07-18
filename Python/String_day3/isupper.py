def isupper(text):
    count=0
    for ch in text:
        if ch.isalpha() and ch.isupper():
            print(ch)
            count+=1
    return count
print(isupper("MayurGawatreAI"))