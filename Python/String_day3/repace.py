def replace(text,old,new):
    return text.replace(old,new)
print(replace("banana","a","o"))




def replace2(text,old,new):
    result=""
    for ch in text:
        if ch==old:
            result+=new
        else:
            result+=ch
    return result
print(replace2("banana","a","o"))