def removespace(text,old,new):
    result=""
    for ch in text:
        if ch==old:
            result+=new
        else:
            result+=ch
    return result
print(removespace("mayurGawa tre"," ",""))




def remove(text):
    return text.replace(" ","")
print(remove("Mayur Gawa tre"))