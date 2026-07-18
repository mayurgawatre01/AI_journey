def consonent(text):
    total=0
    for ch in text:
        if ch.isalpha() and ch.lower() not in "aeiou" :
            
            total+=1
    return total
print(consonent("MayurGawatre"))