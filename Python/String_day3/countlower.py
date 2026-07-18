def count_lowercase(text):
    count=0
    for ch in text:
        if ch.islower():
            print(ch)
            count+=1
    return count
print(count_lowercase("MayurGawatre"))
    