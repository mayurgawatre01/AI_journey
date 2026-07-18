def special(text):
    count=0
    for ch in text:
        if not ch.isalpha() and  not ch.isdigit() and ch!=" ":
            count+=1
    return count
print(special("MAyur&*GWatre&*@#(&)"))