def count_d(text):
    count=0
    for ch in text:
        if ch.isdigit():
            count+=1
    return count
print(count_d("123mayurHGwand9099"))