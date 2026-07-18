def space_count(text):
    count=0
    for ch in text:
        if ch==" ":
            count+=1
    return count

print(space_count("Mayur Gawa Tre"))



def opti(text):
    return text.count(" ")
print(opti("May ur Gawatre AI "))        