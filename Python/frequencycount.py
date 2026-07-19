def char_frequency(text, target):
    count=0
    for ch in text:
        if ch==target:
            count+=1
    return count
    
    
print(char_frequency("banana", "a"))





def count(text,target):
    return text.count(target)
print(count("mayurGawatare","a"))