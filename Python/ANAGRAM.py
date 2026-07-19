def anagram(text1,text2):
    
    if sorted(text1.lower())==sorted(text2.lower()):
        return True
    else:
        return False
print(anagram("listen","silent"))