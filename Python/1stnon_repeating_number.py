def non_repeat(text):
    for ch in text:
        if text.count(ch)==1:
            return ch
print(non_repeat("bananabhejjhe"))