def replace(text,old,new):
    result=""
    for ch in text:
        if ch!=old:
            result+=ch
        else:
            result+=new
    return result
print(replace("banananana","a","o"))




def replace2(text,old,new):
    return text.replace(old,new)
print(replace2("banana","a","o"))